import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers.test.views import router as test_router


app = FastAPI()

app.mount("/static", StaticFiles())
app.include_router(prefix="/test_router", router=test_router)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, workers=1)
