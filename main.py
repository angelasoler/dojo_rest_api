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

last_conselho = ""

@app.get("/conselhos")
async def root():
    global last_conselho 
    dicas = 'DICAS'
    conselhos = []

    with open(dicas, 'r') as file:
        for line in file:
            conselhos.append(line.strip())

    novo_conselho = random.choice(conselhos)
    while novo_conselho == last_conselho:
        novo_conselho = random.choice(conselhos)

    last_conselho = novo_conselho  
    return {"message": novo_conselho}