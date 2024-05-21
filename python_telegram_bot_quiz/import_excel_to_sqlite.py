import pandas as pd
import sqlite3

# Replace 'your_excel_file.xlsx' with the path to your Excel file
file_path = 'Вопросы Узб 7.xlsx'
database_path = 'quiz_data.db'

# Load the Excel file
excel_data = pd.read_excel(file_path, sheet_name=None)

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect(database_path)
cursor = conn.cursor()

# Drop the table if it exists to ensure we're creating it fresh for this example
cursor.execute('DROP TABLE IF EXISTS quiz')

# Create table with specified column names
cursor.execute('''
CREATE TABLE IF NOT EXISTS quiz (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT,
    right_answer TEXT,
    wrong_answer1 TEXT,
    wrong_answer2 TEXT,
    wrong_answer3 TEXT
)
''')

# Function to insert data into the SQLite database
def insert_data_to_db(data):
    for index, row in data.iterrows():
        question, right_answer, wrong_answer1, wrong_answer2, wrong_answer3 = row
        # Convert any non-string objects to strings
        question = str(question)
        right_answer = str(right_answer)
        wrong_answer1 = str(wrong_answer1)
        wrong_answer2 = str(wrong_answer2)
        wrong_answer3 = str(wrong_answer3)
        cursor.execute('''
        INSERT INTO quiz (question, right_answer, wrong_answer1, wrong_answer2, wrong_answer3)
        VALUES (?, ?, ?, ?, ?)
        ''', (question, right_answer, wrong_answer1, wrong_answer2, wrong_answer3))
    conn.commit()

# Extract the last five columns and insert into the database
for sheet_name, data in excel_data.items():
    last_five_columns = data.iloc[:, -5:]
    last_five_columns.columns = ['question', 'right_answer', 'wrong_answer1', 'wrong_answer2', 'wrong_answer3']
    insert_data_to_db(last_five_columns)

# Close the database connection
conn.close()

print("Data successfully inserted into the SQLite database.")
