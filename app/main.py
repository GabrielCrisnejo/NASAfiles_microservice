import logging

from fastapi import FastAPI
from api.external_api import api_router
import uvicorn

# Crear la app FastAPI
app = FastAPI(
    title="NASA Ocean Data API",
    description="API para descargar archivos de la NASA",
    version="0.1"
)

app.include_router(api_router)

# Logger para el servicio
logger = logging.getLogger(__name__)

# if __name__ == "__main__":
#     import os
#     port = int(os.getenv("PORT", 8080))
#     uvicorn.run(app, host="0.0.0.0", port=port)
