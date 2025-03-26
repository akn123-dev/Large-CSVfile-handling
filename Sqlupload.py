# -*- coding: utf-8 -*-
"""
Created on Thu Mar 13 12:22:49 2025

@author: Administrator
"""

import os
import mysql.connector

# MySQL connection details (update these)
MYSQL_HOST = "host"
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
MYSQL_DATABASE = "mydb"
MYSQL_TABLE = "table"

# Folder containing chunked CSV files
chunk_folder =  r"your chunks directory"

# Connect to MySQL
conn = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE,
    allow_local_infile=True  # Required to use LOAD DATA LOCAL INFILE
)
cursor = conn.cursor()

# Get all chunked CSV files in sorted order
chunk_files = sorted([f for f in os.listdir(chunk_folder) if f.endswith(".csv")])

for chunk_file in chunk_files:
    chunk_path = os.path.join(chunk_folder, chunk_file).replace("\\", "/")  # Ensure correct path format

    sql_query = f"""
    LOAD DATA LOCAL INFILE '{chunk_path}'
    INTO TABLE {MYSQL_TABLE}
    FIELDS TERMINATED BY ',' 
    ENCLOSED BY '"'
    LINES TERMINATED BY '\\n'
    IGNORE 1 ROWS;
    """

    print(f"🚀 Importing: {chunk_file} ...")
    
    try:
        cursor.execute(sql_query)
        conn.commit()
        print(f"✅ Successfully imported: {chunk_file}")
    except Exception as e:
        print(f"❌ Error importing {chunk_file}: {e}")

# Close MySQL connection
cursor.close()
conn.close()

print("✅ All CSV chunks imported successfully!")
