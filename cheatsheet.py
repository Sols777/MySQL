import mysql.connector


# try:
#     conn = mysql.connector.connect(user='root' , host='localhost', database='luis_dataan', autocommit=True)
#     cursor = conn.cursor()
# except:
#     print("\nErro: Connection error!\n")
# else:
#     query = '''SELECT p.name ,  c.name 
#                 FROM person p
# 	            INNER JOIN city c on c.id = p.city_id
#                 WHERE p.is_active=1
#              '''
#     cursor.execute(query)
#     myResult = cursor.fetchall()
#     print(myResult)
# finally:
#     conn.close()

# #

# # RETURNAR EM DICIONARIO
# def getModelsFromBrand(brand_id):
#     modelList = []
#     try:
#         conn = mysql.connector.connect(user="root", host="localhost", database="dataanalyst", autocommit=True)
#         cursor = conn.cursor()
#     except:
#         print("\nErro: connection error!\n")
#         return None
#     else:
#         cursor.execute("SELECT brand.name, model.name FROM brand, model WHERE brand.id = model.brand_id and brand.id = %s", (brand_id,))
#         for model in cursor.fetchall():
#             modelList.append({'brand': model[0], 'model' : model[1]})
#         return modelList
#     finally:
#         if conn:
#             conn.close()  

conn = mysql.connector.connect(user='root' , host='localhost', database='python_carros', autocommit=True)
cursor = conn.cursor()

val = [("Opel",),("Toyota",),( "Seat",)]
cursor.executemany("INSERT INTO marca (marca) VALUES (%s)", (val))
print(f"Foi adicionado {cursor.rowcount} registo!")

conn.close()