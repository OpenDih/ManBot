import os
from dotenv import load_dotenv
import mysql.connector as lewd

load_dotenv()


# just run it for First time setup to create the Database and Table

conn = lewd.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PW")
)

cursor = conn.cursor()

# Create database if not exists
cursor.execute("CREATE DATABASE IF NOT EXISTS discord_bot")

# Select DB
cursor.execute("USE discord_bot")

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_pairs (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_message TEXT,
    bot_reply TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()
conn.close()

print("Database and table created successfully.")
