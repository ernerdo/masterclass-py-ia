from fastapi import FastAPI, HTTPException
from .gemini_ai import gemini_ai_client
from .open_ai import open_ai_client
from .models import PromptRequest

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/ask")
async def ask(body: PromptRequest):
    try:
        if body.ai == "gemini_ai":
            model = gemini_ai_client().GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(body.prompt)
            print(response.text)
            ai_message = response.text
        elif body.ai == "open_ai":
            client = open_ai_client()
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {
                        "role": "user",
                        "content": body.prompt
                    }
                ]
            )
            ai_message = response.choices[0].message.content
        else:
            ai_message = f"AI provider '{body.ai}' is not supported."
    except Exception as e:
       raise HTTPException(status_code=500, detail=str(e))
    return {"message": ai_message}
