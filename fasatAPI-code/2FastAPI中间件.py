from fastapi import FastAPI

app = FastAPI()

# 中间件1
@app.middleware("http")
async def middleware1(request, call_next):
    print("中间件1 start...")
    response = await call_next(request)
    print("中间件1 end...")

    return response

# 中间件2
@app.middleware("http")
async def middleware2(request, call_next):
    print("中间件2 start...")
    response = await call_next(request)
    print("中间件2 end...")

    return response

# 根路由
@app.get("/")
async def root():
    return {"message": "Hello World"}