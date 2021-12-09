import mysql.connector

def getConnection(database, host, port, user, passwd):
    return mysql.connector.connect(
      host=host,
      port=port,
      user=user,
      passwd=passwd,
      database=database
    )