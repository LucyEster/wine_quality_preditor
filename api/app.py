from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import *
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
vinho_tag = Tag(name="Vinho", description="Adição, visualização, remoção e predição de qualidade de vinhos")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de listagem de vinhos
@app.get('/vinhos', tags=[vinho_tag],
         responses={"200": WineViewSchema, "404": ErrorSchema})
def get_vinhos():
    """Lista todos os vinhos cadastrados na base
    Args:
       none
        
    Returns:
        list: lista de vinhos cadastrados na base
    """
    logger.debug("Coletando dados sobre todos os vinhos")
    # Criando conexão com a base
    session = Session()
    # Buscando todos os vinhos
    vinhos = session.query(Wine).all()
    
    if not vinhos:
        # Se não houver vinhos
        return {"pacientes": []}, 200
    else:
        logger.debug(f"%d vinhos econtrados" % len(vinhos))
        print(vinhos)
        return apresenta_vinhos(vinhos), 200


# Rota de adição de vinho
@app.post('/vinho', tags=[vinho_tag],
          responses={"200": WineViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: WineSchema):
    """Adiciona um novo vinho à base de dados
    Retorna uma representação dos vinhos e diagnósticos associados.
        
    Returns:
        dict: representação do vinho e qualidade associada
    """
    # TODO: Instanciar classes

    # Recuperando os dados do formulário
    fixed_acidity = form.fixed_acidity
    volatile_acidity = form.volatile_acidity
    citric_acid = form.citric_acid
    residual_sugar = form.residual_sugar
    chlorides = form.chlorides
    free_sulfur_dioxide = form.free_sulfur_dioxide
    total_sulfur_dioxide = form.total_sulfur_dioxide
    density = form.density
    p_h = form.p_h
    sulphates = form.sulphates
    alcohol = form.alcohol
        
    # Preparando os dados para o modelo
    X_input = PreProcessador.preparar_form(form)
    # Carregando modelo
    model_path = './MachineLearning/models/et_wine_classifier.pkl'
    # modelo = Model.carrega_modelo(ml_path)
    modelo = Model.carrega_modelo(model_path)
    # Realizando a predição
    outcome = int(Model.preditor(modelo, X_input)[0])
    
    vinho = Wine(
        fixed_acidity= fixed_acidity,
        volatile_acidity= volatile_acidity,
        citric_acid= citric_acid,
        residual_sugar= residual_sugar,
        chlorides= chlorides,
        free_sulfur_dioxide= free_sulfur_dioxide,
        total_sulfur_dioxide= total_sulfur_dioxide,
        density= density,
        p_h= p_h,
        sulphates= sulphates,
        alcohol= alcohol,
        quality= outcome
    )
    logger.debug(f"Adicionando vinho com sucesso! Qualidade do vinho: '{outcome}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Checando se paciente já existe na base
        #if session.query(Wine).filter(Wine.id == form.id).first():
        #    error_msg = "Paciente já existente na base :/"
        #    logger.warning(f"Erro ao adicionar paciente '{paciente.name}', {error_msg}")
        #    return {"message": error_msg}, 409
        
        # Adicionando paciente
        session.add(vinho)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado vinho:")
        return apresenta_vinho(vinho), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar vinho, {error_msg}")
        return {"message": error_msg}, 400
    
    
if __name__ == '__main__':
    app.run(debug=True)