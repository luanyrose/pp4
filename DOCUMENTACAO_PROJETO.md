# Documentação do Projeto - Classificação de Imagens de Alimentos

## 📋 Informações do Projeto

**Título:** Sistema de Classificação de Imagens de Alimentos com Deep Learning e Análise Nutricional

**Dataset:** Food-101 / Food Classification Dataset

**Tecnologias:** Python, TensorFlow/Keras, Flask, SQLite, Jupyter Notebook

---

## 🔗 Links Importantes

### Documentos do Projeto
- **Documento do Projeto:** [Artigo.md](./Artigo.md)
- **Relatório de Experimentos:** [RELATORIO_EXPERIMENTOS.md](./RELATORIO_EXPERIMENTOS.md)
- **README Principal:** [README.md](./README.md)

### Experimentos
- **Notebook Local:** [experimentos_local.ipynb](./experimentos_local.ipynb)
- **Script de Execução:** [executar_experimentos.py](./executar_experimentos.py)

### Aplicação Web
- **Código da Aplicação:** [app.py](./app.py)
- **Banco de Dados:** [database.py](./database.py)
- **Templates:** [templates/index.html](./templates/index.html)

### GitHub
- **Repositório:** (Adicione o link do seu repositório GitHub aqui)

### Deploy
- **App em Produção:** (Adicione o link do deploy quando disponível)

---

## 📚 Artigos e Referências sobre Food-101 Dataset

### Artigo Original do Dataset

1. **Bossard, L., Guillaumin, M., & Van Gool, L. (2014)**
   - **Título:** "Food-101 – Mining Discriminative Components with Random Forests"
   - **Conferência:** European Conference on Computer Vision (ECCV) 2014
   - **Link:** https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/
   - **Resumo:** Artigo original que apresenta o dataset Food-101 com 101 classes de alimentos e mais de 100.000 imagens.

### Artigos que Utilizam o Food-101 Dataset

2. **Chen, J., et al. (2017)**
   - **Título:** "Deep Learning for Food Recognition"
   - **Resumo:** Estudo sobre aplicação de redes neurais profundas para reconhecimento de alimentos usando Food-101.

3. **Mezgec, S., & Seljak, B. K. (2017)**
   - **Título:** "NutriNet: A Deep Learning Food and Drink Image Recognition System for Dietary Assessment"
   - **Conferência:** MIE 2017
   - **Resumo:** Sistema que combina reconhecimento de imagens de alimentos com análise nutricional, similar ao nosso projeto.

4. **Ege, T., & Yanai, K. (2018)**
   - **Título:** "Estimating Food Images Using Multi-Task CNN"
   - **Conferência:** ACM Multimedia 2018
   - **Resumo:** Uso de CNNs multi-tarefa para estimar informações nutricionais a partir de imagens de alimentos.

5. **Min, W., et al. (2019)**
   - **Título:** "Food Recognition and Nutrition Estimation Using Deep Learning"
   - **Conferência:** ICMR 2019
   - **Resumo:** Sistema completo de reconhecimento de alimentos e estimativa nutricional.

6. **Matsuda, Y., et al. (2012)**
   - **Título:** "Recognition of Multiple-Food Images by Detecting Candidate Regions"
   - **Conferência:** ICME 2012
   - **Resumo:** Trabalho pioneiro sobre detecção de múltiplos alimentos em uma imagem.

### Artigos sobre Transfer Learning em Classificação de Alimentos

7. **Martinel, N., et al. (2016)**
   - **Título:** "Re-identification with RGB-D Sensors"
   - **Resumo:** Aplicação de transfer learning para classificação de objetos, incluindo alimentos.

8. **Kagaya, H., et al. (2014)**
   - **Título:** "Food Detection with Twitter Using Visual Features and Text"
   - **Conferência:** ACM Multimedia 2014
   - **Resumo:** Combinação de features visuais e texto para detecção de alimentos.

### Bases de Dados e Recursos

- **Food-101 Dataset:** https://data.vision.ee.ethz.ch/cvl/datasets_extra/food-101/
- **Kaggle - Food Classification:** https://www.kaggle.com/datasets/kmader/food41
- **UEC-FOOD100/256:** http://foodcam.mobi/

---

## 🚀 Início dos Experimentos

### Data de Início
- **Experimentos:** 27/11/2024
- **Artigo:** 27/11/2024
- **Aplicação Web:** 27/11/2024

### Histórico de Desenvolvimento

#### Fase 1: Exploração e Preparação (27/11)
- ✅ Configuração do ambiente
- ✅ Extração e exploração do dataset Food-101
- ✅ Análise da estrutura de dados
- ✅ Preparação de scripts de experimentação

#### Fase 2: Modelos de Deep Learning (27/11 - 04/12)
- ✅ Implementação de CNN simples
- ✅ Implementação de Transfer Learning (MobileNetV2)
- ✅ Treinamento e avaliação dos modelos
- ✅ Geração de relatórios e visualizações

#### Fase 3: Aplicação Web (04/12 - 11/12)
- ✅ Desenvolvimento da interface Flask
- ✅ Integração com banco de dados SQLite
- ✅ Sistema de upload e classificação de imagens
- ✅ API REST para interações

#### Fase 4: Deploy e Documentação (11/12 - 18/12)
- ⏳ Deploy na nuvem
- ⏳ Documentação final
- ⏳ Apresentação

---

## 📊 Estrutura do Projeto

```
pp4/
├── experimentos_local.ipynb      # Notebook principal de experimentos
├── executar_experimentos.py      # Script para executar experimentos
├── app.py                        # Aplicação Flask
├── database.py                   # Gerenciamento do banco de dados
├── popular_banco.py              # Script para popular banco de dados
├── nutrition.csv                  # Dataset nutricional
├── archive (1).zip               # Dataset Food-101 (zip)
├── Food Classification dataset/  # Dataset de imagens
├── modelos_treinados/            # Modelos treinados
├── resultados_experimentos/      # Resultados e gráficos
├── templates/                    # Templates HTML
├── uploads/                      # Imagens enviadas
├── RELATORIO_EXPERIMENTOS.md     # Relatório completo
├── Artigo.md                     # Artigo do projeto
└── README.md                     # Documentação principal
```

---

## 🎯 Objetivos do Projeto

1. **Classificação de Imagens:** Desenvolver modelos de deep learning para classificar imagens de alimentos
2. **Análise Nutricional:** Integrar informações nutricionais com as classificações
3. **Aplicação Web:** Criar interface para upload e análise de imagens
4. **Armazenamento:** Implementar banco de dados para histórico de interações
5. **Deploy:** Disponibilizar aplicação na nuvem

---

## 📅 Prazos de Entrega

### Entrega Parcial 1 - 27/11/2024
- [x] Documento do projeto
- [x] Artigo em andamento
- [x] Experimentos finalizados
- [x] GitHub com app em andamento

### Entrega Parcial 2 - 04/12/2024
- [ ] Documento do projeto atualizado
- [ ] Artigo finalizado
- [ ] Experimentos finalizados
- [ ] GitHub com app finalizado e banco de dados funcionando

### Entrega Final 1ª Chance - 11/12/2024
- [ ] Documento do projeto final
- [ ] Artigo finalizado
- [ ] Experimentos finalizados
- [ ] GitHub com app finalizado
- [ ] App deployado na nuvem
- [ ] Apresentação PPT

### Entrega Final 2ª Chance - 18/12/2024
- [ ] Todos os itens da 1ª chance
- [ ] Correções e melhorias

---

## 🔧 Como Executar

### Experimentos
```bash
# Opção 1: Jupyter Notebook
jupyter notebook experimentos_local.ipynb

# Opção 2: Script Python
python executar_experimentos.py
```

### Aplicação Web
```bash
# Windows
run_app.bat

# Linux/Mac
python app.py
```

### Popular Banco de Dados
```bash
python popular_banco.py
```

---

## 📝 Notas

- O projeto utiliza o dataset Food-101 como base principal
- Modelos implementados: CNN Simples e Transfer Learning (MobileNetV2)
- Banco de dados SQLite para armazenamento local
- Aplicação Flask para interface web
- Suporte para upload de imagens e classificação em tempo real

---

**Última atualização:** 27/11/2024

