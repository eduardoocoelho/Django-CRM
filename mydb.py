import pymysql

dataBase = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '123456'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm_db")

print("All Done!")
