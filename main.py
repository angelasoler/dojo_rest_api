from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/conselhos")
async def root():
    dicas = 'DICAS'
    conselhos = []

    with open(dicas, 'r') as file:
        for line in file:
            conselhos.append(line.strip())
    return {"message": random.choice(conselhos)}