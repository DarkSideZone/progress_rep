from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship, sessionmaker, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from decouple import config

DATABASE_URL = config('DATABASE_URL')

class Base(AsyncAttrs, DeclarativeBase):
    pass

engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(engine)

class StockIn(Base):
    __tablename__ = 'stock_in'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    timestamp = Column(DateTime, server_default=func.now(), nullable=False)

    product = relationship("Product", back_populates="stock_in_records")


class StockOut(Base):
    __tablename__ = 'stock_out'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    timestamp = Column(DateTime, server_default=func.now(), nullable=False)

    product = relationship("Product", back_populates="stock_out_records")


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    price = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=True)

    category = relationship("Category", back_populates="products")
    stock_in_records = relationship("StockIn", back_populates="product")
    stock_out_records = relationship("StockOut", back_populates="product")    


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    products = relationship("Product", back_populates="category")


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)