import pandas as pd
import mysql.connector

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("pl17.csv", encoding='latin1')

# MySQL Connection Parameters
host = 'localhost'  # Corrected hostname
user = 'root'
password = 'Admin@123'
database = 'placementpro'

# Connect to MySQL
conn = mysql.connector.connect(host=host, user=user, password=password, database=database)
cursor = conn.cursor()

# Create the table
create_table_query = """
CREATE TABLE pl2019_2020 (
S_No INT,
Name_of_the_Skill_Enhancement_programme VARCHAR(100),
Category VARCHAR(100),
Year_of_Implementation DATE,
Branches_Covered VARCHAR(100),
Number_of_Students_Attended VARCHAR(100),
Training_for_Batch VARCHAR(100),	
Date DATE,	
no_of_Hours INT
)
"""
cursor.execute(create_table_query)
conn.commit()

# Insert data into the table
for index, row in df.iterrows():
    insert_query = """
    INSERT INTO pl2019_2020 (S_No,	Name_of_the_Skill_Enhancement_programme	,Category,Year_of_Implementation,Branches_Covered,Number_of_Students_Attended,Training_for_Batch,	Date,	no_of_Hours)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_query, tuple(row))
    conn.commit()

# Close the cursor and connection
cursor.close()
conn.close() 
