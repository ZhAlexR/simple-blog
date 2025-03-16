import os

from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()


MYSQL_USER=os.getenv("MYSQL_USER")
MYSQL_PASSWORD=os.getenv("MYSQL_PASSWORD")
MYSQL_HOST=os.getenv("MYSQL_HOST")
MYSQL_PORT=os.getenv("MY_PORT")
DB_NAME=os.getenv("DB_NAME")

engine = create_engine(f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{DB_NAME}", echo=True)
