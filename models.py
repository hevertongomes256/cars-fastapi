from typing import Optional

from pydantic import BaseModel, validator


class Veiculo(BaseModel):
    id: Optional[int] = None
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


veiculos = [
    Veiculo(id=1, modelo="Fiat Uno", ano=2021, placa="ABC-1234", marca="Fiat", tipo="Carro", descricao="Volkswagen Gol", preco_fip=85000.0, preco_loja=95000.0),
    Veiculo(id=2, modelo="Chevrolet Onix", ano=2020, placa="DEF-5678", marca="Chevrolet", tipo="Carro", descricao="Chevrolet Onix", preco_fip=120000.0, preco_loja=130000.0),
    Veiculo(id=3, modelo="Volkswagen Gol", ano=2019, placa="GHI-7890", marca="Volkswagen", tipo="Carro", descricao="Volkswagen Gol", preco_fip=75000.0, preco_loja=85000.0),
    Veiculo(id=4, modelo="Ford Ka", ano=2018, placa="JKL-9012", marca="Ford", tipo="Carro", descricao="Ford Ka", preco_fip=65000.0, preco_loja=75000.0),
    Veiculo(id=5, modelo="Renault Kwid", ano=2017, placa="MNO-1234", marca="Renault", tipo="Carro", descricao="Renault Kwid", preco_fip=45000.0, preco_loja=55000.0),
]

# Para testes

# Veiculo(modelo="Hyundai HB20", ano=2016, placa="PQR-3456", marca="Hyundai", tipo="Carro", descricao="Hyundai HB20", preco_fip=55000.0, preco_loja=65000.0),
# Veiculo(modelo="Ford Ka", ano=2015, placa="STU-4567", marca="Ford", tipo="Carro", descricao="Ford Ka", preco_fip=50000.0, preco_loja=60000.0),
# Veiculo(modelo="Chevrolet Onix", ano=2014, placa="VWX-5678", marca="Chevrolet", tipo="Carro", descricao="Chevrolet Onix", preco_fip=95000.0, preco_loja=105000.0),
# Veiculo(modelo="Renault Kwid", ano=2013, placa="YZA-7890", marca="Renault", tipo="Carro", descricao="Renault Kwid", preco_fip=40000.0, preco_loja=50000.0),
# Veiculo(modelo="Volkswagen Gol", ano=2012, placa="BCD-9012", marca="Volkswagen", tipo="Carro", descricao="Volkswagen Gol", preco_fip=60000.0, preco_loja=70000.0)
