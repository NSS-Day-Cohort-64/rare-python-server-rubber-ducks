import sqlite3
from models import Post
from models import User
def get_all_posts():
    
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        # Write the SQL query to get the information you want
        db_cursor.execute("""
            SELECT
                p.id,
                p.user_id,
                p.category_id,
                p.title,
                p.publication_date,
                p.image_url,
                p.content,
                p.approved,
                u.first_name,
                u.last_name,
                u.email,
                u.bio,
                u.username,
                u.password,
                u.profile_image_url,
                u.created_on,
                u.active
            FROM Posts p
            JOIN Users u
                ON u.id = p.user_id
            ORDER BY u.created_on DESC
                """)
        
        posts = []

        dataset = db_cursor.fetchall()
        for row in dataset:
            post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row['publication_date'], row['image_url'], row['content'], row['approved'])
            user = User(row['id'], row['first_name'], row['last_name'], row['email'], row['bio'], row['username'], row['password'], row['profile_image_url'], row['created_on'], row['active'])
            
            post.user = user.__dict__
            posts.append(post.__dict__)

    return posts

def get_posts_by_user(user_id):
    with sqlite3.connect("./loaddata.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            p.approved,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.password,
            u.profile_image_url,
            u.created_on,
            u.active
        FROM Posts p
        JOIN Users u
            ON u.id = p.user_id
        WHERE p.user_id = ?
        """, (user_id, ))

        posts = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            post = Post(row['id'], row['user_id'], row['category_id'], row['title'], row['publication_date'], row['image_url'], row['content'], row['approved'])
            user = User(row['id'], row['first_name'], row['last_name'], row['email'], row['bio'], row['username'], row['password'], row['profile_image_url'], row['created_on'], row['active'])

            post.user = user.__dict__

            posts.append(post.__dict__)

    return posts