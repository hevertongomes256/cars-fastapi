from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.veiculo import Veiculo as VeiculoModel
from core.deps import get_session


router = APIRouter()


# POST veiculo
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=VeiculoModel)
async def post_veiculo(veiculo: VeiculoModel, db: AsyncSession = Depends(get_session)):
    novo_veiculo = VeiculoModel(
        modelo=veiculo.modelo,
        ano=veiculo.ano,
        placa=veiculo.placa,
        marca=veiculo.marca,
        tipo=veiculo.tipo,
        descricao=veiculo.descricao,
        preco_fip=veiculo.preco_fip,
        preco_loja=veiculo.preco_loja
    )

    db.add(novo_veiculo)
    await db.commit()

    return novo_veiculo


# GET veiculos
@router.get('/', response_model=List[VeiculoModel])
async def get_veiculos(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(VeiculoModel)
        result = await session.execute(query)
        veiculos: List[VeiculoModel] = result.scalars().all()
        return veiculos


# GET veiculo
@router.get('/{veiculo_id}', response_model=VeiculoModel, status_code=status.HTTP_200_OK)
async def get_veiculo(veiculo_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(VeiculoModel).filter(VeiculoModel.id == veiculo_id)
        result = await session.execute(query)
        veiculo = result.scalar_one_or_none()

        if veiculo:
            return veiculo
        else:
            raise HTTPException(detail='Veiculo não encontrado', status_code=status.HTTP_404_NOT_FOUND)


# PUT veiculo
@router.put('/{veiculo_id}', response_model=VeiculoModel, status_code=status.HTTP_202_ACCEPTED)
async def put_veiculo(veiculo_id: int, veiculo: VeiculoModel, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(VeiculoModel).filter(VeiculoModel.id == veiculo_id)
        result = await session.execute(query)
        veiculo_up = result.scalar_one_or_none()

        if veiculo_up:
            veiculo_up.modelo = veiculo.modelo
            veiculo_up.ano = veiculo.ano
            veiculo_up.placa = veiculo.placa
            veiculo_up.marca = veiculo.marca
            veiculo_up.tipo = veiculo.tipo
            veiculo_up.descricao = veiculo.descricao
            veiculo_up.preco_fip = veiculo.preco_fip
            veiculo_up.preco_loja = veiculo.preco_loja

            await session.commit()

            return veiculo_up
        else:
            raise HTTPException(detail='Veículo não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)


# DELETE veiculo
@router.delete('/{veiculo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_veiculo(veiculo_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(VeiculoModel).filter(VeiculoModel.id == veiculo_id)
        result = await session.execute(query)
        veiculo_del = result.scalar_one_or_none()

        if veiculo_del:
            await session.delete(veiculo_del)
            await session.commit()

            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Veículo não encontrado.',
                                status_code=status.HTTP_404_NOT_FOUND)
