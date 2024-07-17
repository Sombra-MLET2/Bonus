import uvicorn
from fastapi import FastAPI, Depends


app = FastAPI()


@app.get("/")
async def root():
    return {
        "result": {
            "success": True,
            "team": "Sombra-MLET2"
        }
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.250", port=8000, log_level="info")
