from fastapi import FastAPI

app = FastAPI(title="SIGEH API", description="Sistema Integral de Gestión Hospitalaria")

@app.get("/")
def read_root():
    return {"status": "ok", "message": "API de SIGEH funcionando correctamente en entorno Docker"}