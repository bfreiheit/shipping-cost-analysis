import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from shipping_cost_analysis.models.schema import Base

load_dotenv(override=True)


def get_engine() -> "Engine":

    user = os.getenv("DB_USER_LOCAL")
    password = os.getenv("DB_PASSWORD_LOCAL")
    host = os.getenv("DB_HOST_LOCAL")
    port = os.getenv("DB_PORT_LOCAL")
    conn_str = (
        f"postgresql://{user}:{password}@{host}:{port}/{os.getenv("DB_NAME_LOCAL")}"
    )

    return create_engine(conn_str)


def drop_all_tables():
    engine = get_engine()
    print("Dropping all tables...")
    Base.metadata.drop_all(bind=engine)
    print("All tables dropped.")

def create_all_tables():
    engine = get_engine()
    print("Creating all tables...")
    Base.metadata.create_all(bind=engine)
    print("All tables created.")



