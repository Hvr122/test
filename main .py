from fastapi import FastApi,HTTPException

from google import genai
from pydantic import BaseModel
import os 

app= FastApi(title = " Test")

client = genai.Client(api_key="AIzaSyDTaNzoCzyDTMdEwWgr0YT-b_Lggq5kF9c")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain how AI works in a few words",
)

class PromtRequest(BaeModel):
    prompt: str

@app.post("https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent")

async def generate_text(request:PromtRequest):
    try:
        response=client.models.generate_content(
            model=MODEL,
            contents=request.prompt
        )
        text=getattr(response,"text",None)
        if not text:
            text=str(response)
        return {"response":text}
    except Exception as e:
        raise HTTPException(status_code=500,details=str(e))

