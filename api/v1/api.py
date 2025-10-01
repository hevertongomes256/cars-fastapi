from fastapi import APIRouter

from api.v1.endpoints import veiculo


api_router = APIRouter()
api_router.include_router(veiculo.router, prefix='/veiculos', tags=["veiculos"])
