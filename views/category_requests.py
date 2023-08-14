import sqlite3
import json
from models import Category


def get_all_categories():
    # Open a connection to the database
    with sqlite3.connect("./loaddata.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.label
        FROM Categories a
            """)

        # Initialize an empty list to hold all animal representations
        categories = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
    for row in dataset:

        # Create an animal instance from the current row
        category = Category(row['id'], row['label'])


        # Add the dictionary representation of the location to the animal

        # Add the dictionary representation of the animal to the list
        categories.append(category.__dict__)

    return categories




def get_single_category(id):
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.label
        FROM Categories a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        category = Category(data['id'], data['label'])

        return category.__dict__
    



def create_category(new_category):
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Categories
            (label)
        VALUES
            (?);
        """, (new_category['label'], ))

        category_id = db_cursor.lastrowid

        new_category['id'] = category_id

    return new_category

