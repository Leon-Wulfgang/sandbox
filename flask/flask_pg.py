import psycopg2
import bleach

DBNAME = "forum"


def get_posts():
    """Return all posts from the 'database', most recent first."""
    db = psycopg2.connect(database=DBNAME)
    dbHandle = db.cursor()
    query = "select content,time from posts order by time desc;"
    dbHandle.execute(query)
    rows = dbHandle.fetchall()
    db.close()
    return rows


def add_post(content):
    """Add a post to the 'database' with the current timestamp."""
    db = psycopg2.connect(database=DBNAME)
    dbHandle = db.cursor()
    dbHandle.execute(
        "insert into posts (content) values (%(content)s) ",
        {'content': bleach.clean(content)}
    )
    db.commit()
    db.close()
