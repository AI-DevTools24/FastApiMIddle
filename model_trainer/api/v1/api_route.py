from typing import Union, Dict

from fastapi import APIRouter
from http import HTTPStatus

from pydantic import BaseModel

models = {}

router = APIRouter()



class ApiResponse(BaseModel):
    message: str
    data: Union[Dict, None] = None

class ModelListResponse(BaseModel):
    # Список словарей
    models:

# API endpoints
@router.post("/fit", response_model=ApiResponse, status_code=HTTPStatus.CREATED)
async def fit(request:""):
    # Реализуйте логику обучения и сохранения модели.
    # Обратите внимание на формат входных данных.
    # Обучать Нужно логистическую и линейную регрессии.
    return ApiResponse()

@router.post("/load", response_model='')
async def load(request: ''):
    # Реализуйте загрузку обученной модели для инференса.
    return

@router.post("/unload", response_model=UnloadResponse)
async def unload(
):
    # Реализуйте апи выгружающее загруженную модель.
    return

@router.post("/predict")
async def predict(request:):
    # Реализуйте инференс загруженной модели
    return

@router.get("/list_models", response_model='')
async def list_models():
    # Реализуйте получения списка обученных моделей
    return ModelListResponse()


@router.delete("/remove/{model_id}", response_model="")
async def remove():
    # Удаление обученной модели из списка по id модели
    return


# Реализуйте Delete метод remove_all