from shipping_cost_analysis.etl.db_tools import get_engine
from shipping_cost_analysis.models.schema import Base

def main():
    engine = get_engine()   

    with engine.connect() as conn:
        Base.metadata.create_all(conn)    
        print("Tables created.")

if __name__ == "__main__":
    main()
