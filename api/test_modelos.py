from model import *

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros    
url_dados_X = "./MachineLearning/data/X_test_dataset_wine.csv"
colunas_X = ["fixed acidity",
             "volatile acidity",
             "citric acid",
             "residual sugar",
             "chlorides",
             "free sulfur dioxide",
             "total sulfur dioxide",
             "density",
             "pH",
             "sulphates",
             "alcohol"]

url_dados_y = "./MachineLearning/data/y_test_dataset_wine.csv"
colunas_y = ['quality']

# Carga dos dados
dataset_X = Carregador.carregar_dados(url_dados_X, colunas_X)
array_X = dataset_X.values

# Carga dos dados
dataset_y = Carregador.carregar_dados(url_dados_y, colunas_y)
array_y = dataset_y.values

X = array_X[:,:]
y = array_y[:,-1]
    
# Método para testar o modelo de Regressão Logística a partir do arquivo correspondente
# O nome do método a ser testado necessita começar com "test_"
def test_modelo_et():  
    # Importando o modelo de regressão logística
    et_path = './MachineLearning/models/et_wine_classifier.pkl'
    modelo_et = Model.carrega_modelo(et_path)

    # Obtendo as métricas da Regressão Logística
    acuracia_lr = Avaliador.avaliar(modelo_et, X, y)
    
    # Testando as métricas da Regressão Logística 
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_lr >= 0.60 
    # assert recall_lr >= 0.5 
    # assert precisao_lr >= 0.5 
    # assert f1_lr >= 0.5 
 

    

