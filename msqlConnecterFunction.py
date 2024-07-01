import mysql.connector
 
def loadData(sql):
    try:
        conn = mysql.connector.connect(user="root", host="localhost", database="luis_dataan", autocommit=True)
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

citys = loadData("SELECT * FROM city")
#print(citys)
# buscar todas as pessoas e respetivas localidades da BD
persons = loadData("SELECT person.id, person.name, city.name FROM person, city WHERE person.city_id = city.id and person.is_active=1")
print(persons)