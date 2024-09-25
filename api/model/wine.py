from sqlalchemy import Column, Integer, DateTime, Float
from datetime import datetime
from typing import Union

from  model import Base

class Wine(Base):
    __tablename__ = 'wines'
    
    #columns
    id = Column(Integer, primary_key=True)
    fixed_acidity= Column("FixedAcidity", Float)
    volatile_acidity = Column("VolatileAcidity", Float)
    citric_acid = Column("CitricAcid", Float)
    residual_sugar = Column("ResidualSugar", Float)
    chlorides = Column("Chlorides", Float)
    free_sulfur_dioxide = Column("FreeSulfurDioxide", Float)
    total_sulfur_dioxide = Column("TotalSulfurDioxide", Float)
    density = Column("Density", Float)
    p_h = Column("PH", Float)
    sulphates = Column("Sulphates", Float)
    alcohol = Column("Alcohol", Float)

    #outcome
    quality = Column("Quality", Integer, nullable=True) 

    data_insercao = Column(DateTime, default=datetime.now())

    
    def __init__(self, fixed_acidity:float, volatile_acidity:float,
                  citric_acid:float, residual_sugar:float, chlorides:float,
                  free_sulfur_dioxide:float, total_sulfur_dioxide:float,
                  density:float, p_h:float, sulphates:float, alcohol:float, quality:int, 
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Vinho

        """
        self.fixed_acidity = fixed_acidity
        self.volatile_acidity = volatile_acidity
        self.citric_acid = citric_acid
        self.residual_sugar = residual_sugar
        self.chlorides = chlorides
        self.free_sulfur_dioxide = free_sulfur_dioxide
        self.total_sulfur_dioxide = total_sulfur_dioxide
        self.density = density
        self.p_h = p_h
        self.sulphates = sulphates
        self.alcohol = alcohol
        self.quality = quality

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao