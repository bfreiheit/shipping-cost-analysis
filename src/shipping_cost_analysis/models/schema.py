from sqlalchemy import (
    CheckConstraint,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Region(Base):
    __tablename__ = "dim_region"
    order_state = Column(String(2), primary_key=True)
    state = Column(String)
    region = Column(String)

    # Relationship
    customers = relationship("Customer", back_populates="region")
    # Add constraint
    __table_args__ = (
        CheckConstraint(
            "char_length(order_state) = 2", name="check_order_state_length"
        ),
    )


class Customer(Base):
    __tablename__ = "dim_customer"
    customer_id = Column(Integer, primary_key=True)
    order_city = Column(String)
    order_postal = Column(String)
    order_state = Column(String(2), ForeignKey("dim_region.order_state"))
    latitude = Column(Float)
    longitude = Column(Float)

    # Relationship
    transactions = relationship("Transactions", back_populates="customer")
    region = relationship("Region", back_populates="customers")


class Product(Base):
    __tablename__ = "dim_product"
    stock_code = Column(String, primary_key=True)
    weight = Column(Float)
    landed_cost = Column(Float)
    shipping_cost_1000_r = Column(Float)
    description = Column(String)
    category = Column(String)

    # Relationship
    transactions = relationship("Transactions", back_populates="product")


class Transactions(Base):
    __tablename__ = "fact_transactions"
    id = Column(Integer, primary_key=True)
    transaction_date = Column(DateTime)
    customer_id = Column(Integer, ForeignKey("dim_customer.customer_id"))
    stock_code = Column(String, ForeignKey("dim_product.stock_code"))
    invoice_no = Column(Integer)
    quantity = Column(Integer)
    sales = Column(Float)
    unit_price = Column(Float)

    # Relationships
    customer = relationship("Customer", back_populates="transactions")
    product = relationship("Product", back_populates="transactions")


class Ecommerce(Base):
    __tablename__ = "ecommerce"
    id = Column(Integer, primary_key=True)

    customer_id = Column(Integer)
    order_city = Column(String)
    order_postal = Column(String)
    order_state = Column(String(2))
    latitude = Column(Float)
    longitude = Column(Float)

    transaction_date = Column(DateTime)
    customer_id = Column(Integer)
    stock_code = Column(String)
    invoice_no = Column(Integer)
    quantity = Column(Integer)
    sales = Column(Float)
    unit_price = Column(Float)

    weight = Column(Float)
    landed_cost = Column(Float)
    shipping_cost_1000_r = Column(Float)
    description = Column(String)
    category = Column(String)

    state = Column(String)
    region = Column(String)
