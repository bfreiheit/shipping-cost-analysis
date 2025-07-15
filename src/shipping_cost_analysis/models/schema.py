from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'dim_customer'
    customer_id = Column(Integer, primary_key=True)
    order_city = Column(String)
    order_postal = Column(String)
    order_state = Column(String(2), ForeignKey('dim_region.order_state'))
    latitude = Column(Float)
    longitude = Column(Float)

class Product(Base):
    __tablename__ = 'dim_product'
    stock_code = Column(String, primary_key=True)
    weight = Column(Float)
    landed_cost = Column(Float)
    shipping_cost_1000_r = Column(Float)
    description = Column(String)
    category = Column(String)

class Region(Base):
    __tablename__ = 'dim_region'
    order_state = Column(String(2), primary_key=True)
    state = Column(String)
    region = Column(String)

    __table_args__ = (
        CheckConstraint("char_length(order_state) = 2", name="check_order_state_length"),
    )

class Transactions(Base):
    __tablename__ = 'fact_transactions'
    id = Column(Integer, primary_key=True)
    transaction_date = Column(DateTime)
    customer_id = Column(Integer, ForeignKey('dim_customer.customer_id'))
    description = Column(String)
    stock_code = Column(String, ForeignKey('dim_product.stock_code'))
    invoice_no = Column(Integer)
    quantity = Column(Integer)
    sales = Column(Float)
    unit_price = Column(Float)
