from fastapi import FastAPI
from app.route.greet import greet_router

app = FastAPI(title='OpenNet FastAPI')
app.include_router(greet_router)
