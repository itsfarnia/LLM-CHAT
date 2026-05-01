from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()
client = OpenAI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "AI API Server is running"}

@app.post("/chat")
def chat(request: ChatRequest):
    response = client.responses.create(
        model="gpt-5.5",
        input=request.message
    )

    return {
        "user_message": request.message,
        "ai_response": response.output_text
    }