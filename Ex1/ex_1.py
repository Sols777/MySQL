import mysql.connector
 
def loadData(sql):
    try:
        conn = mysql.connector.connect(user="root", host="localhost", database="python_carros", autocommit=True)
        cursor = conn.cursor()
    except:
        print("\nErro: connection error!\n")
        return None
    else:
        cursor.execute(sql)
        myResult = cursor.fetchall()
        return myResult
    finally:
        if conn:
            conn.close()
            
            
#print(citys)
# buscar todas as pessoas e respetivas localidades da BD
modelos = loadData(f'''SELECT m1.marca , m2.modelo FROM modelo m2
INNER JOIN marca m1
ON m1.id = m2.marca_id
WHERE m1.marca LIKE "{input('Marca: ')}"
''')
print(modelos)