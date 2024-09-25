from pydantic import BaseModel
from typing import Optional, List
from model.wine import Wine
import json
import numpy as np

class WineSchema(BaseModel):
    """ Define como um novo vinho a ser inserido deve ser representado
    """
    fixed_acidity: float = 7.4
    volatile_acidity: float = 0.70
    citric_acid: float = 0.04
    residual_sugar: float = 1.9
    chlorides: float = 0.076
    free_sulfur_dioxide: float = 11.0
    total_sulfur_dioxide: float = 34.0
    density: float = 0.9978
    p_h: float = 3.51
    sulphates: float = 0.56
    alcohol: float = 9.4
    
class WineViewSchema(BaseModel):
    """Define como um vinho será retornado
    """
    id: int = 1
    fixed_acidity: float = 7.4
    volatile_acidity: float = 0.70
    citric_acid: float = 0.04
    residual_sugar: float = 1.9
    chlorides: float = 0.076
    free_sulfur_dioxide: float = 11.0
    total_sulfur_dioxide: float = 34.0
    density: float = 0.9978
    p_h: float = 3.51
    sulphates: float = 0.56
    alcohol: float = 9.4
    quality: int = None
    
class WineBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do paciente.
    """
    name: str = "Maria"

class ListaWinesSchema(BaseModel):
    """Define como uma lista de pacientes será representada
    """
    vinhos: List[WineSchema]

    
class WineDelSchema(BaseModel):
    """Define como um vinho para deleção será representado
    """
    name: str = "Maria"
    
# Apresenta apenas os dados de um vinho    
def apresenta_vinho(vinho: Wine):
    """ Retorna uma representação do vinho seguindo o schema definido em
        WineViewSchema.
    """
    return {
        "fixed_acidity": vinho.fixed_acidity,
        "volatile_acidity": vinho.volatile_acidity,
        "citric_acid": vinho.citric_acid,
        "residual_sugar": vinho.residual_sugar,
        "chlorides": vinho.chlorides,
        "free_sulfur_dioxide": vinho.free_sulfur_dioxide,
        "total_sulfur_dioxide": vinho.total_sulfur_dioxide,
        "density": vinho.density,
        "p_h": vinho.p_h,
        "sulphates": vinho.sulphates,
        "alcohol": vinho.alcohol,
        "quality": vinho.quality
    }
    
# Apresenta uma lista de vinhos
def apresenta_vinhos(vinhos: List[Wine]):
    """ Retorna uma representação do vinho seguindo o schema definido em
        WineViewSchema.
    """
    result = []
    for vinho in vinhos:
        result.append({
            "id": vinho.id,
            "fixed_acidity": vinho.fixed_acidity,
            "volatile_acidity": vinho.volatile_acidity,
            "citric_acid": vinho.citric_acid,
            "residual_sugar": vinho.residual_sugar,
            "chlorides": vinho.chlorides,
            "free_sulfur_dioxide": vinho.free_sulfur_dioxide,
            "total_sulfur_dioxide": vinho.total_sulfur_dioxide,
            "density": vinho.density,
            "p_h": vinho.p_h,
            "sulphates": vinho.sulphates,
            "alcohol": vinho.alcohol,
            "quality": vinho.quality
        })

    return {"vinhos": result}

