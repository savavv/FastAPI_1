import os

from django.core.asgi import get_asgi_application
from fastapi import FastAPI

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_app.settings')
django_asgi_app = get_asgi_application()

fastapi_app = FastAPI()

@fastapi_app.get("/")
async def read_root():
    return {"Hello": "FastAPI"}

async def application(scope, receive, send):
    if scope['type'] == 'http':
        if scope['path'].startswith('/api'):
            await fastapi_app(scope, receive, send)
        else:
            await django_asgi_app(scope, receive, send)
