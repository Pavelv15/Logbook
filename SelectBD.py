import sqlite3
i = True
while i == True :
    zapros = input('Введите запрос(Для завершение введите stop >')
    if zapros == 'stop':
        i = False
    else:
        con = sqlite3.connect('db.sqlite3')
        def sql_fetch(con,zapros):
            objectSql = con.cursor()
            objectSql.execute(zapros)
            rows = objectSql.fetchall()
            for row in rows:
                print(row)
        sql_fetch(con,zapros)
