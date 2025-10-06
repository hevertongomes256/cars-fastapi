from typing import Optional

from pydantic import BaseModel, validator

# Schema separado


class VeiculoSchema(BaseModel):
    id: Optional[int] = None
    modelo: str
    ano: int
    placa: str
    marca: str
    tipo: str
    descricao: str
    preco_fip: float
    preco_loja: float

    class Config:
        orm_mode = True

    @validator('placa')
    def validar_placa(cls, value: str):
        if len(value) < 8:
            raise ValueError('A placa deve ter 8 digítos.')
        return value

    @validator('preco_fip')
    def validar_preco_fip(cls, value: float):
        if value <= 0.0:
            raise ValueError('o valor da tabela fipe deve ser maior que zero!')
        return value

    @validator('preco_loja')
    def validar_preco_loja(cls, value: float):
        if value <= 0.0:
            raise ValueError('o valor do veiculo deve ser maior que zero!')
        return value