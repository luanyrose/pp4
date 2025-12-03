"""
Aplicação web Flask para identificação de alimentos em imagens.
"""

import os
import json
from pathlib import Path
from datetime import datetime
import numpy as np
import pandas as pd

# Tentar importar TensorFlow (opcional)
try:
    import tensorflow as tf
    # TensorFlow 2.20+ - usar tf_keras
    try:
        import tf_keras as keras
        TENSORFLOW_AVAILABLE = True
        print("✓ Usando tf_keras")
    except ImportError:
        try:
            import keras
            keras.config.set_backend('tensorflow')
            TENSORFLOW_AVAILABLE = True
            print("✓ Usando keras com backend tensorflow")
        except:
            keras = tf.keras
            TENSORFLOW_AVAILABLE = True
            print("✓ Usando tf.keras diretamente")
except ImportError:
    TENSORFLOW_AVAILABLE = False
    tf = None
    keras = None
    print("⚠️ TensorFlow não disponível. App funcionará em modo básico.")
except Exception as e:
    TENSORFLOW_AVAILABLE = False
    tf = None
    keras = None
    print(f"⚠️ Erro ao carregar TensorFlow: {e}")
    print("⚠️ App funcionará em modo básico.")

from flask import Flask, render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image
import io

from database import NutritionDB

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Criar pasta de uploads
Path(app.config['UPLOAD_FOLDER']).mkdir(exist_ok=True)

# Inicializar banco de dados
db = NutritionDB()

# Carregar modelos
BASE_DATA_DIR = Path.cwd()
MODEL_OUTPUT_DIR = BASE_DATA_DIR / "modelos_treinados"

# Variáveis globais para modelos
food_model = None
food_class_names = None

def load_models():
    """Carrega os modelos treinados."""
    global food_model, food_class_names
    
    # Verificar se TensorFlow está disponível
    try:
        import tensorflow as tf
    except ImportError:
        print("⚠️ TensorFlow não está disponível. App funcionará em modo básico.")
        food_model = None
        food_class_names = None
    
    if food_model is None:  # Só tentar carregar se ainda não foi definido
    # Carregar modelo Food-101
     if TENSORFLOW_AVAILABLE and tf is not None:
        food_model_path = MODEL_OUTPUT_DIR / "food101_classifier.keras"
        if food_model_path.exists():
            try:
                food_model = keras.models.load_model(food_model_path)
                print(f"✓ Modelo Food-101 carregado")
            except Exception as e:
                print(f"✗ Erro ao carregar modelo Food-101: {e}")
                food_model = None
        else:
            food_model = None
    else:
        food_model = None
        
        # Carregar classes
        class_names_path = MODEL_OUTPUT_DIR / "food101_class_names.npy"
        if class_names_path.exists():
            try:
                food_class_names = np.load(class_names_path, allow_pickle=True).tolist()
                print(f"✓ {len(food_class_names)} classes carregadas")
            except Exception as e:
                print(f"✗ Erro ao carregar classes: {e}")
                food_class_names = None
    

def allowed_file(filename):
    """Verifica se o arquivo tem extensão permitida."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def preprocess_image(image_path, target_size=(224, 224)):
    """Preprocessa imagem para o modelo."""
    if not TENSORFLOW_AVAILABLE or keras is None:
        # Fallback usando PIL
        img = Image.open(image_path)
        img = img.resize(target_size)
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, 0)
        return img_array
    
    img = keras.utils.load_img(image_path, target_size=target_size)
    img_array = keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    return img_array

def predict_food(image_path):
    """Prediz a classe de comida na imagem."""
    if food_model is None or food_class_names is None:
        # Modo fallback: tentar identificar por nome do arquivo ou usar classe genérica
        filename = Path(image_path).stem.lower()
        # Mapear alguns padrões comuns
        food_keywords = {
            'pizza': 'pizza',
            'burger': 'hamburger',
            'apple': 'apple_pie',
            'chicken': 'chicken_curry',
            'rice': 'fried_rice',
            'sushi': 'sushi',
            'cake': 'cheesecake'
        }
        for keyword, food_name in food_keywords.items():
            if keyword in filename:
                return food_name, 0.5  # Confiança baixa para modo fallback
        return 'unknown_food', 0.3
    
    try:
        img_array = preprocess_image(image_path)
        predictions = food_model.predict(img_array, verbose=0)
        predicted_idx = np.argmax(predictions[0])
        confidence = float(predictions[0][predicted_idx])
        food_name = food_class_names[predicted_idx]
        return food_name, confidence
    except Exception as e:
        print(f"Erro na predição: {e}")
        # Fallback
        return predict_food(image_path)  # Recursão com fallback


@app.route('/')
def index():
    """Página principal."""
    return render_template('index.html')

@app.route('/api/upload', methods=['POST'])
def upload_image():
    """Endpoint para upload de imagem e predição."""
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nenhum arquivo selecionado'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{timestamp}_{filename}"
        filepath = Path(app.config['UPLOAD_FOLDER']) / filename
        file.save(filepath)
        
        # Predizer comida
        food_name, confidence = predict_food(str(filepath))
        
        resultado = {
            'imagem': filename,
            'alimento_reconhecido': food_name,
            'confianca': confidence
        }
        
        return jsonify(resultado)
    
    return jsonify({'error': 'Tipo de arquivo não permitido'}), 400

@app.route('/api/refeicao', methods=['POST'])
def criar_refeicao():
    """Cria uma nova refeição."""
    data = request.json
    
    refeicao_id = db.criar_refeicao(
        nome=data.get('nome'),
        imagem_path=data.get('imagem'),
        alimento_reconhecido=data.get('alimento_reconhecido'),
        confianca=data.get('confianca')
    )
    
    # Adicionar itens
    for item in data.get('itens', []):
        alimento_id = item.get('alimento_id')
        quantidade = item.get('quantidade', 1.0)
        if alimento_id:
            db.adicionar_item_refeicao(refeicao_id, alimento_id, quantidade)
        else:
            # Se não tem ID, buscar pelo nome
            nome_alimento = item.get('nome')
            if nome_alimento:
                alimento = db.buscar_alimento(nome_alimento)
                if alimento:
                    db.adicionar_item_refeicao(refeicao_id, alimento['id'], quantidade)
                else:
                    # Criar alimento se não existir
                    alimento_id = db.adicionar_alimento(nome_alimento, {})
                    db.adicionar_item_refeicao(refeicao_id, alimento_id, quantidade)
    
    refeicao = db.obter_refeicao(refeicao_id)
    return jsonify(refeicao)

@app.route('/api/refeicoes', methods=['GET'])
def listar_refeicoes():
    """Lista todas as refeições."""
    refeicoes = db.listar_refeicoes()
    return jsonify(refeicoes)

@app.route('/api/refeicao/<int:refeicao_id>', methods=['GET'])
def obter_refeicao(refeicao_id):
    """Obtém uma refeição específica."""
    refeicao = db.obter_refeicao(refeicao_id)
    if refeicao:
        return jsonify(refeicao)
    return jsonify({'error': 'Refeição não encontrada'}), 404

@app.route('/api/alimento/manual', methods=['POST'])
def adicionar_alimento_manual():
    """Adiciona um alimento manualmente."""
    data = request.json
    
    alimento_id = db.adicionar_alimento_manual(
        nome=data['nome'],
        calorias=data.get('calorias', 0),
        proteinas=data.get('proteinas', 0),
        carboidratos=data.get('carboidratos', 0),
        gorduras=data.get('gorduras', 0)
    )
    
    return jsonify({'alimento_id': alimento_id, 'mensagem': 'Alimento adicionado com sucesso'})

@app.route('/api/alimentos', methods=['GET'])
def listar_alimentos():
    """Lista todos os alimentos."""
    alimentos = db.listar_alimentos()
    return jsonify(alimentos)

@app.route('/api/buscar-alimento', methods=['GET'])
def buscar_alimento():
    """Busca um alimento por nome."""
    nome = request.args.get('nome', '')
    if not nome:
        return jsonify({'error': 'Nome não fornecido'}), 400
    
    alimento = db.buscar_alimento(nome)
    if alimento:
        return jsonify({
            'id': alimento['id'],
            'nome': alimento['nome']
        })
    
    return jsonify({'error': 'Alimento não encontrado'}), 404

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serve arquivos de upload."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    print("Carregando modelos...")
    load_models()
    print("Iniciando servidor Flask...")
    app.run(debug=True, host='0.0.0.0', port=5000)

