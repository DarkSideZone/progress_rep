from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, sessionmaker, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from decouple import config

DATABASE_URL = config('DATABASE_URL')

class Base(AsyncAttrs, DeclarativeBase):
    pass

engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(engine)

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    products = relationship("Product", back_populates="category")


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


