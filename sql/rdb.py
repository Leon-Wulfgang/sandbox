import psycopg2, bleach
DBNAME = "forum"
def get_posts():
  """Return all posts from the 'database', most recent first."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("select content, time from posts order by time desc")
  posts = c.fetchall()
  db.close()
  return posts
def add_post(content):
  """Add a post to the 'database' with the current timestamp."""
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute("insert into posts values (%s)", (bleach.clean(content),))  # good
  db.commit()
  db.close()

  c.execute(
  """INSERT INTO some_table (an_int, a_date, another_date, a_string)
  VALUES (%(int)s, %(date)s, %(date)s, %(str)s);""",
  {'int': 10, 'str': "O'Reilly", 'date': datetime.date(2005, 11, 18)}
  )
  # http://bleach.readthedocs.org/en/latest/
  bleach.clean(content)


import sqlite3
# Fetch some student records from the database.
db = sqlite3.connect("students")
c = db.cursor()
query = "select name, id from students order by name;"
c.execute(query)
rows = c.fetchall()
# First, what data structure did we get?
print "Row data:"
print rows
# And let's loop over it too:
print
print "Student names:"
for row in rows:
  print "  ", row[0]
db.close()

db = sqlite3.connect("testdb")
c = db.cursor()
c.execute("insert into balloons values ('blue', 'water') ")
db.commit()
db.close()
