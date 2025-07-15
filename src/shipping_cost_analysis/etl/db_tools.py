from sqlalchemy import create_engine
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

load_dotenv(override=True)


def get_engine() -> "Engine":
   
    user = os.getenv("DB_USER_LOCAL")
    password = os.getenv("DB_PASSWORD_LOCAL")
    host = os.getenv("DB_HOST_LOCAL")
    port = os.getenv("DB_PORT_LOCAL")
    conn_str = f"postgresql://{user}:{password}@{host}:{port}/{os.getenv("DB_NAME_LOCAL")}"

    return create_engine(conn_str)



