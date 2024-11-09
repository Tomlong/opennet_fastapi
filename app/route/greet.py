from fastapi import APIRouter, Query
from loguru import logger
from app.model.response import GreetResponse


greet_router = APIRouter(tags=['greet'])


@greet_router.get('/')
def greet(name: str = Query(default='World')):
    logger.info(f'greet name: {name}')
    return GreetResponse(name=name).response_format()
