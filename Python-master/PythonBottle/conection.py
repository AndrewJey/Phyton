import pymysql

def conectar():
    conection = pymysql.connect(host='localhost', port=3306, user='root', passwd='12345', db='exposicion')
    return conection
