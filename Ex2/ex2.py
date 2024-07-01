# imports
import mysql.connector
import beaupy
# functions
def getAllRacas():
    valList = []
    try:
        conn = mysql.connector.connect(user="root", host="localhost", database="python_ex2animais", autocommit=True)
        cursor = conn.cursor()
    except:
        print("\nErro: connection error!\n")
        return None
    else:
        cursor.execute("SELECT nome FROM raca")
        for val in cursor.fetchall():
            valList.append({'nome': val[0]})
        return valList
    finally:
        if conn:
            conn.close()  
#
def getAllAnimais():
    valList = []
    try:
        conn = mysql.connector.connect(user="root", host="localhost", database="python_ex2animais", autocommit=True)
        cursor = conn.cursor()
    except:
        print("\nErro: connection error!\n")
        return None
    else:
        cursor.execute('''SELECT a.nome , a.especie , a.dono , r.nome FROM animal a
                            RIGHT JOIN raca r 
                            ON r.id = a.raca_id
                       ''')
        for val in cursor.fetchall():
            valList.append({'nome': val[0], 'especie' : val[1], 'dono' : val[2] , 'raca' : val[3]})
        return valList
    finally:
        if conn:
            conn.close()  
#
def InsertRacas(raca):
    try:
        conn = mysql.connector.connect(user="root", host="localhost", database="python_ex2animais", autocommit=True)
        cursor = conn.cursor()
    except:
        print("\nErro: connection error!\n")
        return None
    else:
        cursor.execute("INSERT INTO raca (nome) values (%s)", (raca,))
        print(f"Foi adicionado {cursor.rowcount} registo!")
    finally:
        if conn:
            conn.close()              
#           
def InsertAnimais(nome , especie , dono , raca_id):
    try:
        conn = mysql.connector.connect(user="root", host="localhost", database="python_ex2animais", autocommit=True)
        cursor = conn.cursor()
    except:
        print("\nErro: connection error!\n")
        return None
    else:
        cursor.execute("INSERT INTO animal (nome , especie , dono , raca_id) values (%s,%s,%s,%s)", (nome , especie , dono , raca_id,))
        print(f"Foi adicionado {cursor.rowcount} registo!")
    finally:
        if conn:
            conn.close()  
#     
def getAnimalByDono(dono):
    valList = []
    try:
        conn = mysql.connector.connect(user="root", host="localhost", database="python_ex2animais", autocommit=True)
        cursor = conn.cursor()
    except:
        print("\nErro: connection error!\n")
        return None
    else:
        cursor.execute(f'''SELECT a.nome , a.especie , a.dono , r.nome FROM animal a
                            RIGHT JOIN raca r 
                            ON r.id = a.raca_id
                            WHERE a.dono LIKE "{dono}"
                       ''')
        for val in cursor.fetchall():
            valList.append({'nome': val[0], 'especie' : val[1], 'dono' : val[2] , 'raca' : val[3]})
        return valList
    finally:
        if conn:
            conn.close()  
#
def Menu():
    listaMenu = ("1 - Inserir raca" , "2 - Inserir animal", "3 - Lista animais" , "4 - Listar animais por dono" , "5 - Sair" )
    while True:
        op = int(beaupy.select(listaMenu, cursor="->", cursor_style='green', return_index=True))+1
        match op:
            case 1:
                InsertRacas(input("Raca: "))
            case 2:
                racasList = getAllRacas()
                op = int(beaupy.select(racasList, cursor="->", cursor_style='green', return_index=True))+1
                nome , especie , dono , raca_id = input("Nome: ") ,input("Especie: ") , input("Dono: ") , op 
                InsertAnimais(nome , especie , dono , raca_id)
            case 3:
                print(getAllAnimais())
            case 4:
                dono = input('Dono: ')
                print(getAnimalByDono(dono))
            case 5:
                break
            case _:
                print("\nErro!\n")                
# CALL FUNCTION
Menu()
