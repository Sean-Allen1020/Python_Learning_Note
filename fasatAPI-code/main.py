from fastapi import FastAPI, Path

# 创建FastAPI实例
app = FastAPI()


# 运行指令
# uvicorn main:app --reload
# --reload代表在代码修改时自动重新加载服务器

# /docs 访问文档页面：用于查看API文档和测试API

@app.get("/")
async def root():
    return {"message": "Hello World666"}


# 访问/hello 响应结果 msg: 你好，FastAPI
@app.get("/hello")  # 装饰器，指定路由为/hello，方法为GET
async def hello():
    return {"msg": "Hello FastAPI"}  # 返回JSON格式的响应（字典）


# 路径参数
@app.get("/book/{id}")
async def get_book(id: int = Path(...,
                                  gt=0,
                                  lt=101,
                                  description="图书编号在1-100之间")): # Path(): 为类型注解, ...代表必填
    return {"id": id,
            "title_num": f"当前书编号为{id}"}

# 
