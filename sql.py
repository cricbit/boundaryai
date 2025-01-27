import os
import pandas as pd

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import text


load_dotenv()

engine = create_engine(os.environ.get("POSTGRES_URL"))

def list_tables() -> list[str]:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'"))
        return [dict(row._mapping) for row in result.all()]

def list_columns(table_name: str) -> list[dict]:
    with engine.connect() as connection:
        result = connection.execute(text(f"SELECT column_name, data_type, character_maximum_length FROM information_schema.columns WHERE table_name = '{table_name}' AND table_schema = 'public'"))
        return [dict(row._mapping) for row in result.all()]

def execute_query(query: str):
    with engine.connect() as connection:
        result = connection.execute(text(query))
        df = pd.DataFrame(result.fetchall(), columns=result.keys())
        # Convert DataFrame to a list of dictionaries for JSON serialization
        return df.to_dict('records')
