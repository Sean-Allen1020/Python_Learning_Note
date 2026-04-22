from fastapi import FastAPI,HTTPException ,Path, Query
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel, Field

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
                                  description="图书编号在1-100之间")):  # Path(): 为类型注解, ...代表必填
    return {"id": id,
            "title_num": f"当前书编号为{id}"}


# 查询参数
@app.get("/student")  # 默认值
async def get_student(name: str = Query("张三", description="学生姓名", min_length=2, max_length=10),
                      age: int = 18):
    return {"name": name, "age": age}


# 请求体参数
# 定义实体类
class User(BaseModel):
    name: str = Field(..., min_length=2, max_length=10, description="用户名长度需求2-10个字")
    password: str = Field(..., min_length=6, max_length=20, description="密码")


# 请求函数
@app.post("/register")
async def register(user: User):
    return user


# 响应类型
# 装饰器处指定
@app.get("/html", response_class=HTMLResponse)
async def get_html():
    return "<h1>这是标题</h1>"


# 返回处指定
@app.get("/file")
async def get_file():
    file_path = "../2.AI应用基础/resource/MCP协议示意图.png"
    return FileResponse(file_path)


# 响应自定义类型
class Book(BaseModel):
    id: int = Field(..., gt=0, lt=101, description="图书编号在1-100之间")
    title: str


@app.get("/book2/{id}", response_model=Book)
async def get_book2(id: int):
    return {
        "id": id,
        "title": f"id: {id}《Python Web开发实战》"
    }


# 异常处理
@app.get("/book3/{id}")
async def get_book3(id: int):
    if id not in range(1,101):
        raise HTTPException(status_code=404, detail="图书编号不合规")
    return {"id": id,
            "title": f"id: {id}《Python Web开发实战》"}