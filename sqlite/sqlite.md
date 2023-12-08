```bash

```


```python
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('noco.db')  # Replace 'your_database.db' with your actual database file

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute the query to get table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")

# Fetch all the results
print(cursor.fetchall())


#table info 
cursor.execute(f"PRAGMA table_info(nc_w7o____surrealdb)")
cursor.fetchall()
#nocodb  0-2 hiden  3-  title
[(0, 'id', 'INTEGER', 1, None, 1),
 (1, 'created_at', 'datetime', 0, "'CURRENT_TIMESTAMP'", 0),
 (2, 'updated_at', 'datetime', 0, "'CURRENT_TIMESTAMP'", 0),
 (3, 'title', 'TEXT', 0, None, 0),
 (4, 'title5', 'varchar', 0, None, 0)]


cursor.execute("SELECT * from nc_w7o____surrealdb")
print(cursor.fetchall())
#...
# (2, 'CURRENT_TIMESTAMP', 'CURRENT_TIMESTAMP', '', None),
#  (3, 'CURRENT_TIMESTAMP', 'CURRENT_TIMESTAMP', '', None),
#  (4, 'CURRENT_TIMESTAMP', 'CURRENT_TIMESTAMP', None, None),
#  (5, 'CURRENT_TIMESTAMP', 'CURRENT_TIMESTAMP', 'dsa', None)]


#insert  
# must affirm  datatype matched.
# 手动在nocodb上添加 title5 title6 title7 

import sqlite3
# Connect to the SQLite database
conn = sqlite3.connect('noco.db')  # Replace 'your_database.db' with your actual database file
# Create a cursor object to execute SQL queries
cursor = conn.cursor()
import random
import nanoid
city = ['California','beijing','Sheffield','Birmingham','Glasgow','Dublin','Scotland','Belfast','Manchester']
i=1200000
try:
    while i > 0:
        num = random.randint(0,8)
        if num%3 ==0:
            cursor.execute(f"INSERT INTO nc_w7o____surrealdb (ID,created_at,updated_at,title,title5,title6,title7) \
                VALUES ({i}, 'CURRENT_TIMESTAMP', 'CURRENT_TIMESTAMP','{nanoid.non_secure_generate()}{nanoid.non_secure_generate()}{city[num]}{city[random.randint(0,7)]}-{nanoid.non_secure_generate()}', '{nanoid.non_secure_generate()}', '{city[num]}', '' )")  
        else:
            cursor.execute(f"INSERT INTO nc_w7o____surrealdb (ID,created_at,updated_at,title,title5,title6,title7) \
                VALUES ({i}, 'CURRENT_TIMESTAMP', 'CURRENT_TIMESTAMP', '{nanoid.non_secure_generate()}', '{nanoid.non_secure_generate()}{nanoid.non_secure_generate()}{nanoid.non_secure_generate()}', '{city[random.randint(0,7)]}', '{random.randint(2000,50000)}' )")   
        i -= 1
       
        print(f'execute:{i}')
except:
    i-= 1
    print(f'err:{i}')
conn.commit()
cursor.close()
cursor = conn.cursor()
```