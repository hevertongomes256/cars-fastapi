from typing import Optional

from sqlmodel import Field, SQLModel

from pydantic import validator


class Veiculo(SQLModel, table=True):
    __tablename__: str = 'veiculos'

    id: Optional[int] = Field(default=None, primary_key=True)
    modelo: str
    ano: int
    placa: str
    marca: str
    tipo: str
    descricao: str
    preco_fip: float
    preco_loja: float

    @validator('placa')
    def validar_placa(cls, value: str):
        if len(value) < 8:
            raise ValueError('A placa deve ter 8 digítos.')
        return value
