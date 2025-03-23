import mysql.connector
from cred import *

try:
    conn = mysql.connector.connect(
        host=host,
        password=password,
        user=user,
        port=port,
        database =database)
    if conn.is_connected():
        print("connection established...")
except:
    print("Unable to connect...")

curobj = conn.cursor()

# try:
#     curobj.execute("alter table emp add column email varchar(56)")
#     conn.commit()
#     print("table alter success...")
#     curobj.reset()
# except:
#     conn.rollback()
#     print("alter failed!!!")

try:
    curobj.execute("select * from emp")
    rows = curobj.fetchall()
    curobj.reset()
    domain = '@gmail.com'
    for row in rows:
        i = row[1]+'.'+row[2]
        e = i+domain
        print(f"update emp set email='{e}' where eid={row[0]}")
#         try:
#             curobj.execute(f"update emp set email='{e}' where eid={row[0]}")
#             conn.commit()
#             print(f"eid :{row[0]} updated...")
#             curobj.reset()
#         except:
#             conn.rollback()
#             print("Update failed!!!")
#             curobj.reset()
#     print("Congratulatuon, Task working fine...")
except:
    print("Sorry, something went wrong")

try:
    curobj.close()
    conn.close()
    if conn.is_connected() == False:
        print("connection closed successfully...")
except:
    print("connection not closed!!! please close the connection.")
