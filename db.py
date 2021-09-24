import pymysql
conn=pymysql.connect(user="root",password="",host="localhost",database="movies")
cursor=conn.cursor()
query='select * from movies;'
r=cursor.execute(query)
data=cursor.fetchall()
print(data)  #array


