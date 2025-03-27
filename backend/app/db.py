from databases import Database
import os

DATABASE_URL = os.getenv("DB_URL")
database = Database(DATABASE_URL)