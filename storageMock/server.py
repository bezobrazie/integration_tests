import uvicorn
from fastapi import FastAPI, Response
from fastapi.responses import FileResponse

from config import BASE_DIR

app = FastAPI()


@app.get("/status")
async def root():
    return {"Hello": "World!"}


@app.post("/api/{file_id}")
async def ok(file_id: str):
    print(file_id)
    return Response(status_code=200)


@app.get("/api/{file_id}")
async def get(file_id: str):
    if file_id.startswith('1'):
        return FileResponse(BASE_DIR / 'files' / 'smile.png')
    else:
        return FileResponse(BASE_DIR / 'files' / 'dog.jpg')

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=1151, log_level='info')
