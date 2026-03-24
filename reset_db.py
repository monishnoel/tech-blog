import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv('DB_HOST', 'localhost'),
    user=os.getenv('DB_USER', 'root'),
    password=os.getenv('DB_PASSWORD', '')
)

cursor = conn.cursor()
db_name = os.getenv('DB_NAME', 'tech_blog_db')

try:
    cursor.execute(f"DROP DATABASE {db_name}")
    print(f"✓ Dropped {db_name}")
except:
    print(f"Database {db_name} doesn't exist")

cursor.execute(f"CREATE DATABASE {db_name}")
print(f"✓ Created {db_name}")

cursor.close()
conn.close()
