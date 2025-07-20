import os
import traceback
from typing import List

from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError

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


def recreate_tables(table_classes: List) -> None:
    """
    Deletes and creates tables based on SQLAlchemy-schemas.

    Args:
        table_classes (List): list of SQLAlchemy-schema (e.g. [Customer, Product]).
    """
    engine = get_engine()
    with engine.connect() as conn:
        inspector = inspect(conn)

        for table in table_classes:
            try:
                table_name = getattr(table, "__tablename__", None)
                table_obj = getattr(table, "__table__", None)

                if table_name is None or table_obj is None:
                    raise AttributeError(f"invalid table class: {table}")

                if inspector.has_table(table_name):
                    print(f"Delete table: {table_name}")
                    table_obj.drop(bind=conn)

                print(f"Create table: {table_name}")
                table_obj.create(bind=conn)

            except (AttributeError, SQLAlchemyError) as e:
                print(f"Error for table {table}: {e}")
                traceback.print_exc()
