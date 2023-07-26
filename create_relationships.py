"""
Description:
 Creates the relationships table in the Social Network database
 and populates it with 100 fake relationships.

Usage:
 python create_relationships.py
"""
import os
import sqlite3
from faker import Faker
from random import randint, choice
# Determine the path of the database
script_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(script_dir, 'social_network.db')

def main():
    create_relationships_table()
    populate_relationships_table()

def create_relationships_table():
    """Creates the relationships table in the DB"""
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    # Create the sql table named 'relationships' 
    create_relationships_table_query = """
        CREATE TABLE IF NOT EXISTS relationships
        (
         id INTEGER PRIMARY KEY,
         person1_id INTEGER NOT NULL,
         person2_id INTEGER NOT NULL,
         type TEXT NOT NULL,
         start_date DATE NOT NULL,
         FOREIGN KEY (person1_id) REFERENCES people (id),
         FOREIGN KEY (person2_id) REFERENCES people (id)
         );
    """
    # Execute the SQL query to create the 'relationships' table
    cur.execute(create_relationships_table_query)

    con.commit()
    con.close()

    # Hint: See example code in lab instructions entitled "Add the Relationships Table"
    return

def populate_relationships_table():
    """Adds 100 random relationships to the DB"""
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    
    # SQL query that inserts a row of data in the relationships table.
    
    
    # Randomly select first person in a relationship
    for i in range(100):
        add_relationship_query = """
            INSERT INTO relationships
            (
                person1_id,
                person2_id,
                type,
                start_date
            )
        VALUES (?, ?, ?, ?);
     """
        fake = Faker()
        person1_id = randint(1, 200)
        # Loop makes sure person isn't in a relationship with themself
        person2_id = randint(1, 200)
        while person2_id == person1_id:
            person2_id = randint(1, 200)
        # Assigns the nature of their relationship 
        rel_type = choice(('friend', 'spouse', 'partner', 'relative'))
        # Assigns start date
        start_date = fake.date_between(start_date='-50y', end_date='today')
        new_relationship = (person1_id, person2_id, rel_type, start_date)
        cur.execute(add_relationship_query, new_relationship)

    con.commit()
    con.close()
    # Hint: See example code in lab instructions entitled "Populate the Relationships Table"
    return 

if __name__ == '__main__':
   main()