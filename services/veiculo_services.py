from fastapi import HTTPException
from fastapi import status

from fastapi import Response

from sqlalchemy.future import select
from core.deps import get_session

from typing import List

from models.veiculo import Veiculo as VeiculoModel, CriarAtualizarVeiculo


async def criar_veiculo_service(db: get_session, veiculo: CriarAtualizarVeiculo):
    query = select(VeiculoModel).where(VeiculoModel.placa == veiculo.placa)
    result = await db.execute(query)
    existe_veiculo = result.scalar_one_or_none()

    if existe_veiculo:
        raise HTTPException(status_code=400, detail="Já existe um veículo com essa placa.")

    novo_veiculo = VeiculoModel.from_orm(veiculo)
    db.add(novo_veiculo)
    await db.commit()
    await db.refresh(novo_veiculo)
    return novo_veiculo


async def get_veiculos_service(db: get_session):
    query = select(VeiculoModel)
    result = await db.execute(query)
    veiculos: List[VeiculoModel] = result.scalars().all()
    return veiculos


async def get_veiculo_by_id_service(db: get_session, veiculo_id: int):
    query = select(VeiculoModel).filter(VeiculoModel.id == veiculo_id)
    result = await db.execute(query)
    veiculo = result.scalar_one_or_none()

    if not veiculo:
        raise HTTPException(detail='Veiculo não encontrado', status_code=status.HTTP_404_NOT_FOUND)

    return veiculo


async def atualizar_veiculo_service(db: get_session, veiculo_id: int, dados: CriarAtualizarVeiculo):
    query = select(VeiculoModel).filter(VeiculoModel.id == veiculo_id)
    result = await db.execute(query)
    veiculo_up = result.scalar_one_or_none()

    if not veiculo_up:
        raise HTTPException(status_code=404, detail="Veículo não encontrado.")

    dados_dict = dados.dict(exclude_unset=True)

    for key, valeu in dados_dict.items():
        setattr(veiculo_up, key, valeu)

    db.add(veiculo_up)
    await db.commit()
    await db.refresh(veiculo_up)

    return veiculo_up


async def delete_veiculo_service(db: get_session, veiculo_id: int):
    query = select(VeiculoModel).filter(VeiculoModel.id == veiculo_id)
    result = await db.execute(query)
    veiculo_del = result.scalar_one_or_none()

    if veiculo_del:
        await db.delete(veiculo_del)
        await db.commit()

        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(detail='Veículo não encontrado.',
                            status_code=status.HTTP_404_NOT_FOUND)
