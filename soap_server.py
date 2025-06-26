from fastapi import FastAPI, Request, Response
import os
import uvicorn

app = FastAPI()

@app.get("/")
async def hello_world():
    return {"message": "hello world"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("soap_server:app", host="0.0.0.0", port=port, reload=True)