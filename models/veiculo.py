from core.configs import settings

from sqlalchemy import Column, Integer, String, Float


class Veiculo(settings.DBBaseModel):
    __tablename__ = 'veiculos'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    modelo: str = Column(String(100))
    ano: int = Column(Integer)
    placa: str = Column(String(10))
    marca: str = Column(String(100))
    tipo: str = Column(String(100))
    descricao: str = Column(String(255))
    preco_fip: float = Column(Float)
    preco_loja: float = Column(Float)
