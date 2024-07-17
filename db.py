import mysql.connector
import csv

# Connect to the database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Gani_Kore@172',
    database='dashboard_db'
)

cursor = conn.cursor()

# Load data from CSV
with open('C:/Program Files/MySQL/MySQL Server 9.0/Uploads/Data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        if len(row) == 16:  # Ensure there are 16 columns
            cursor.execute(
                "INSERT INTO data (end, year, citylng, citylat, intensity, sector, topic, insight, swot, url, region, start_year, impact, added, published, city) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                row
            )
        else:
            print(f"Skipping row with incorrect number of columns: {row}")

conn.commit()
cursor.close()
conn.close()
