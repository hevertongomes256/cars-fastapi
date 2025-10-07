from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from models.veiculo import Veiculo as VeiculoModel
from core.deps import get_session

from services.veiculo_services import (
    criar_veiculo_service, get_veiculos_service,
    get_veiculo_by_id_service,
    atualizar_veiculo_service,
    delete_veiculo_service)

router = APIRouter()


# POST veiculo
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=VeiculoModel)
async def post_veiculo(veiculo: VeiculoModel, db: AsyncSession = Depends(get_session)):
    return await criar_veiculo_service(db, veiculo)


# GET veiculos
@router.get('/', response_model=List[VeiculoModel])
async def get_veiculos(db: AsyncSession = Depends(get_session)):
    return await get_veiculos_service(db)


# GET veiculo
@router.get('/{veiculo_id}', response_model=VeiculoModel, status_code=status.HTTP_200_OK)
async def get_veiculo(veiculo_id: int, db: AsyncSession = Depends(get_session)):
    return await get_veiculo_by_id_service(db, veiculo_id)


# PUT veiculo
@router.put('/{veiculo_id}', response_model=VeiculoModel, status_code=status.HTTP_202_ACCEPTED)
async def put_veiculo(veiculo_id: int, veiculo: VeiculoModel, db: AsyncSession = Depends(get_session)):
    return await atualizar_veiculo_service(db, veiculo_id, veiculo)


# DELETE veiculo
@router.delete('/{veiculo_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_veiculo(veiculo_id: int, db: AsyncSession = Depends(get_session)):
    return await delete_veiculo_service(db, veiculo_id)
