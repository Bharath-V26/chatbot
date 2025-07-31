from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "healthy"}

@app.post("/chat")
def chat(message: str):
    return {"response": f"You said: {message}"}