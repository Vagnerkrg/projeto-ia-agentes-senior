import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

# Carrega o cofre de chaves local seguro .env
load_dotenv()

app = FastAPI(title="Backend do Agente Bang - Pet Shop")

@app.post("/mock-api")
async def mock_openai_endpoint(request: Request):
    """
    Ponte universal de simulação que intercepta as chamadas do n8n
    e processa o raciocínio automatizado da Bang.
    """
    try:
        dados = await request.json()
        print(f"📥 [Python Backend] Requisição recebida do n8n: {dados}")
        
        # Simula a resposta estruturada do modelo cognitivo de IA
        resposta_mock = {
            "id": "chatcmpl-mock123",
            "object": "chat.completion",
            "created": 1782845000,
            "model": "gpt-4o-mini",
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": "Olá! Eu sou a Bang, sua assistente inteligente. Entendi perfeitamente! Posso sim agendar o Banho do seu pet para amanhã às 14:30. Já estou preparando as ferramentas de confirmação para salvar no banco de dados do Pet Shop! 🐾✨"
                    },
                    "finish_reason": "stop"
                }
            ],
            "usage": {
                "prompt_tokens": 15,
                "completion_tokens": 45,
                "total_tokens": 60
            }
        }
        return JSONResponse(content=resposta_mock, status_code=200)
        
    except Exception as e:
        print(f"❌ [Python Backend] Erro no processamento: {str(e)}")
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)
