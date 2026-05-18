from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import os

app = FastAPI(title="SIGEH API")

@app.get("/", response_class=HTMLResponse)
def read_root():
    # Buscamos la ruta exacta del archivo index.html
    current_dir = os.path.dirname(__file__)
    html_path = os.path.join(current_dir, "index.html")
    
    with open(html_path, "r", encoding="utf-8") as file:
        return file.read()

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API de SIGEH funcionando correctamente"}