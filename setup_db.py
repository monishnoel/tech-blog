#!/usr/bin/env python3
"""
Database setup script that creates the database if it doesn't exist.
Run this before running `python run.py init-db`
"""

import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_database():
    """Create the database if it doesn't exist"""
    try:
        # Connect to MySQL server without specifying a database
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            user=os.getenv('DB_USER', 'root'),
            password=os.getenv('DB_PASSWORD', '')
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            db_name = os.getenv('DB_NAME', 'tech_blog_db')
            
            try:
                # Create database if it doesn't exist
                cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
                print(f"✓ Database '{db_name}' created or already exists")
            except Error as err:
                print(f"✗ Error creating database: {err}")
                return False
            finally:
                cursor.close()
                connection.close()
            
            return True
    
    except Error as err:
        print(f"✗ Error connecting to MySQL: {err}")
        return False

if __name__ == "__main__":
    print("Setting up database...")
    if create_database():
        print("\n✓ Database setup complete!")
        print("Now run: python run.py init-db")
    else:
        print("\n✗ Database setup failed!")
        exit(1)
