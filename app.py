from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    text: str

class Model:
    def predict(self, text):
        ai_keywords = ["as an ai", "language model", "openai", "assistant", "cannot fulfill"]
        if any(word in text.lower() for word in ai_keywords):
            return "AI"
        return "Human"

model = Model()

@app.post("/predict")
async def predict(data: InputData):
    label = model.predict(data.text)
    return {"label": label}
