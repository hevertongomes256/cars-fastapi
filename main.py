from typing import List

from fastapi import Path
from fastapi import Response

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status

from models.veiculo import Veiculo, veiculos


app = FastAPI(
    title='API para uso de carros da Geek University',
    version='0.0.1',
    description='Uma API para estudo do FastAPI'
)


@app.get('/veiculos',
    description='Retorna todos os veículos da loja',
    summary="Retorna os carros da loja",
    response_model=List[Veiculo],
    response_description='Veiculos Retornados com Sucesso!')
async def get_veiculos():
    return veiculos


@app.get('/veiculo/{veiculo_id}')
async def get_veiculo(veiculo_id: int = Path(default=None, title='ID do veículo', description='Deve ser entre 1 e 5', gt=0, lt=6)):
    try:
        veiculo = veiculos[veiculo_id-1]
        return veiculo
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Veículo não encontrado.')


@app.post('/veiculos', status_code=status.HTTP_201_CREATED, response_model=Veiculo)
async def post_veiculo(veiculo: Veiculo):
    next_id: int = len(veiculos) + 1
    veiculo.id = next_id
    veiculos.append(veiculo)
    return veiculo


@app.put('/veiculos/{veiculo_id}')
async def put_veiculo(veiculo_id: int, vericulo_parse: Veiculo):
    for veiculo in veiculos:
        if veiculo_id == veiculo.id:
            veiculos[veiculo_id-1] = vericulo_parse
            del vericulo_parse.id
            return vericulo_parse
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Veiculo com id {veiculo_id} não encontrado!')


@app.delete('/veiculos/{veiculo_id}')
async def delete_veiculo(veiculo_id: int):
    veiculo_delete = None
    for veiculo in veiculos:
        if veiculo.id == veiculo_id:
            veiculo_delete = veiculo
            break
    if veiculo_delete:
        veiculos.remove(veiculo_delete)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Veiculo com id {veiculo_id} não encontrado!')

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)
