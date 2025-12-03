"""
Script para corrigir problemas do TensorFlow/Keras
"""
import os
import sys
import subprocess

print("Corrigindo instalação do TensorFlow/Keras...")

# Tentar reinstalar keras completamente
print("\n1. Reinstalando Keras...")
try:
    # Remover pasta do keras se existir
    import shutil
    keras_path = None
    for path in sys.path:
        test_path = os.path.join(path, 'keras')
        if os.path.exists(test_path):
            keras_path = test_path
            break
    
    if keras_path:
        print(f"   Removendo {keras_path}...")
        try:
            shutil.rmtree(keras_path, ignore_errors=True)
        except:
            pass
    
    # Reinstalar keras
    subprocess.check_call([sys.executable, "-m", "pip", "install", "keras", "--force-reinstall", "--no-deps", "--no-cache-dir"])
    print("   ✓ Keras reinstalado")
except Exception as e:
    print(f"   ⚠ Erro: {e}")

# Testar
print("\n2. Testando TensorFlow...")
try:
    import tensorflow as tf
    print(f"   ✓ TensorFlow {tf.__version__}")
    
    # Tentar usar tf.keras diretamente
    try:
        # Evitar importação lazy do keras
        _ = tf.keras.__version__
        print("   ✓ tf.keras acessível")
        
        # Criar modelo de teste
        model = tf.keras.Sequential([tf.keras.layers.Dense(1)])
        print("   ✓ Modelo criado com sucesso!")
        print("\n✅ TensorFlow está funcionando!")
        
    except Exception as e:
        print(f"   ⚠ Erro ao usar tf.keras: {e}")
        print("\n⚠ TensorFlow básico funciona, mas Keras tem problemas.")
        print("   Você pode usar TensorFlow para operações básicas.")
        
except ImportError as e:
    print(f"   ✗ Erro: {e}")

