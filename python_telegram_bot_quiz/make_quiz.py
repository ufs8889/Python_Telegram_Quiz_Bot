import sqlite3
import random

def get_random_question():
    # Connect to the SQLite database
    conn = sqlite3.connect('quiz_data.db')
    cursor = conn.cursor()
    
    # Generate a random ID between 1 and 100
    random_id = random.randint(1, 613)
    
    # Query the database for the question with the random ID
    cursor.execute('SELECT * FROM quiz WHERE id = ?', (random_id,))
    question = cursor.fetchone()
    
    # Close the database connection
    conn.close()
    
    return question

def shuffle_answers(question):
    # Convert the question tuple to a list to make it mutable
    question_list = list(question)
    
    # Extract the answers from the question
    answers = question_list[1:]  # Assuming answers are in columns 1 to 4
    
    # Shuffle the answers
    random.shuffle(answers)
    
    return answers

