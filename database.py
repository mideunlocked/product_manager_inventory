# import mysql.connector
#
# db_conn = mysql.connector.connect(
#     host="localhost",
#     user="python",
#     passwd="1234",
#     database="python_projects",
# )
# db_cursor = db_conn.cursor()
#
#
# def addProduct(name, quantity, price, time):
#     query = "INSERT INTO products (ProductName, Quantity, Price, TimeAdded) VALUES (%s, %s, %s, %s)"
#     val = (name, quantity, price, time)
#     db_cursor.execute(query, val)
#     db_conn.commit()
#
#     if db_cursor.rowcount >= 1:
#         return True
#     else:
#         return False
#
#     db_conn.close()