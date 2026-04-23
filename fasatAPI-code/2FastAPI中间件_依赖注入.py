from fastapi import FastAPI, Query, Depends

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


# 依赖项
async def common_params(
        page: int = Query(1, description="页码"),
        pagesize: int = Query(10, description="页大小")
):
    return {"page": page, "pagesize": pagesize}

@app.get("/pages")
async def get_pages(common: dict = Depends(common_params)):
    return common