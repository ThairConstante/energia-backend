from fastapi import FastAPI
import uvicorn
from app.core.config import SessionLocal, engine

from app.routes.auth_routes import app as auth_app
from app.routes.user_routes import app as user_app

from app.routes.energy_reading_routes import app as energy_app
from app.routes.temperature_reading_routes import app as temperature_app
from app.routes.sensor_routes import app as sensor_app
from app.routes.sensor_type_routes import app as sensor_type_app
from app.routes.relay_routes import app as relay_app

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_app, tags=['Auth'], prefix='/auth')
app.include_router(user_app, tags=['Users'], prefix='/users')

app.include_router(energy_app, tags=['Lectura Energia'], prefix='/energia')
app.include_router(temperature_app, tags=['Lectura Temperatura'], prefix='/temperatura')
app.include_router(sensor_app, tags=['Censor'], prefix='/censores')
app.include_router(sensor_type_app, tags=['TipoCensor'], prefix='/tipocensores')
app.include_router(relay_app, tags=['Relay'], prefix='/relay')


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
