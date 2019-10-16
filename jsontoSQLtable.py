import json
import sqlite3
import psycopg2
try:
    connection = psycopg2.connect(user="testjiradbuser", password="***",host="127.0.0.1",port="5432",database="testjiradb")
    cursor=connection.cursor()
    id = cursor.lastrowid

    with open('C:\\Users\\Atin_Valiyev\\Desktop\\dba-comm\\behaviour and initializers\\cost-center.txt') as json_file:
        data=json.load(json_file)
        for p in data:

            name=p['Name']
            code=p['Code']
            status=p['Enabled']

            sqlquery="insert into public.\"cost_centers\"(\"id\",\"name\",\"code\",\"status\") values({},'{}','{}',{});".format(id,name,code,status)
            print(sqlquery)
            cursor.execute(sqlquery)
            id=id+1

    connection.commit()
    count=cursor.rowcount
    print(count,"Record inserted successfully into mobile table")
except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into mobile table", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
