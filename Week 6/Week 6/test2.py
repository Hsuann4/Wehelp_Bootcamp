import mysql.connector

conn = mysql.connector.connect(
    user='root', password='Dennis860404_', database='website'
)

cursor = conn.cursor()
query = ("SELECT username FROM member")
cursor.execute(query)
check = cursor.fetchall()
check_list = (list(zip(*check))[0])

print(check)
print(check_list)
