from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
import os

from app.api.views import api_router
from app.conf.settings import settings
from app.database.session import db_lifespan

import warnings
warnings.filterwarnings("ignore")


app = FastAPI(lifespan=db_lifespan)

for folder in ['app/static', 'app/templates']:
    os.makedirs(folder, exist_ok=True)

templates = Jinja2Templates(directory="templates")
app.mount('/static', StaticFiles(directory='app/static'), name='static')


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGIN,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    api_router,
    prefix='/api'
)
