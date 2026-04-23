from contextlib import asynccontextmanager
from fastapi import FastAPI
from datetime import datetime

from sqlalchemy import DateTime, func, String, Float
from sqlalchemy.ext.asyncio import create_async_engine  # 导入创建异步引擎包
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column  # 导入基类包，字段类型包，字段映射包

# 数据库连接： mysql+aiomysql://数据库账号:数据库密码@数据库地址:端口/数据库名称?字符集
ASYNC_DATABASE_URL = "mysql+aiomysql://root:123@localhost:3306/fastapi_test?charset=utf8"

# 1. 创建异步引擎TimestampMixin
async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=True,  # 输出SQL日志
    pool_size=10,  # 连接池大小
    max_overflow=20  # 连接池溢出大小
)


# 2. 定义模型类： 基类 + 表对应的模型类
# 基类： 公共字段 --> 创建时间，更新时间
class Base(DeclarativeBase):
    create_time: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now(), default=func.now(),
                                                  comment="创建时间")
    update_time: Mapped[datetime] = mapped_column(DateTime, insert_default=func.now(), default=func.now(),
                                                  onupdate=func.now(), comment="更新时间")


# 书籍表模型类：id，书名，作者，价格，出版社
class Book(Base):
    # 设置表名
    __tablename__ = "book"
    # 设置字段
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(225), comment="书名")
    author: Mapped[str] = mapped_column(String(225), comment="作者")
    price: Mapped[float] = mapped_column(Float, comment="价格")
    publish: Mapped[str] = mapped_column(String(225), comment="出版社")


# 3. 创建表
# 定义建表函数
async def create_tables():
    # 获取异步引擎，创建事务，建表
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)   # 基类元数据创建表

# 建表时机：FastAPI启动时创建
@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield

app = FastAPI(lifespan=lifespan)