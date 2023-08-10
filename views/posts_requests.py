import sqlite3
from models import Post
def get_all_posts():
    
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        # Write the SQL query to get the information you want
        db_cursor.execute("""
            SELECT
                p.id,
                p.user_id,
                p.title,
                p.category_id,
                p.publication_date,
                p.image_url,
                p.content,
                p.approved
            FROM Posts p
                """)
        
        posts = []

        dataset = db_cursor.fetchall()
        for row in dataset:
            post = Post(row['id'], row['user_id'], row['title'], row['category_id'], row['publication_date'], row['image_url'], row['content'], row['approved'])
            posts.append(post.__dict__)

    return posts