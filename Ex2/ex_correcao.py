import mysql.connector
import beaupy
 
def insertRacaDB(raca):
    conn = mysql.connector.connect(user="root", host="localhost", database="dataanalyst", autocommit=True)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO raca (name) VALUES (%s)", (raca,))
    print(f"Foi adicionado {cursor.rowcount} registo(s)!")
    conn.close()
 
def insertAnimalDB(raca_id, nomeAnimal, tipoAnimal, dono):
    conn = mysql.connector.connect(user="root", host="localhost", database="dataanalyst", autocommit=True)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO animal (raca_id, nome, tipo_animal, dono) VALUES (%s, %s, %s, %s)", (raca_id, nomeAnimal, tipoAnimal, dono))
    conn.close()
    return cursor.rowcount
 
def getRaca():
    conn = mysql.connector.connect(user="root", host="localhost", database="dataanalyst", autocommit=True)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM raca")
    myResult = cursor.fetchall()
    conn.close()
    return myResult
 
def getAllAnimals():
    conn = mysql.connector.connect(user="root", host="localhost", database="dataanalyst", autocommit=True)
    cursor = conn.cursor()
    cursor.execute("SELECT animal.nome, animal.tipo_animal, animal.dono, raca.name FROM animal, raca WHERE animal.raca_id = raca.id order by animal.nome")
    myResult = cursor.fetchall()
    conn.close()
    return myResult    
 
def getAllAnimalsDono(dono):
    conn = mysql.connector.connect(user="root", host="localhost", database="dataanalyst", autocommit=True)
    cursor = conn.cursor()
    cursor.execute("SELECT animal.nome, animal.tipo_animal, animal.dono, raca.name FROM animal, raca WHERE animal.raca_id = raca.id AND animal.dono LIKE %s order by animal.nome", (dono,))
    myResult = cursor.fetchall()
    conn.close()
    return myResult    
 
def printAnimal(animal):
    print(f"""
          Nome: {animal[0]}
          Dono: {animal[2]}
          Tipo: {animal[1]} Raça: {animal[3]}
          """)
 
def printAllAnimals():
    listAnimals = getAllAnimals()
    if listAnimals:
        for animal in listAnimals:
            printAnimal(animal)
    else:
        print("\nNão foram encontrados animais!\n")
 
def printAllAnimalsByDono(dono):
    listAnimals = getAllAnimalsDono(dono)
    if listAnimals:
        for animal in listAnimals:
            printAnimal(animal)
    else:
        print(f"\nNão foram encontrados animais do dono {dono}!\n")
 
def insertAnimal():
    print("\nInserir animal\n")
    listRaca = getRaca()
    menuRaca = [raca[1] for raca in listRaca]
    raca_id = beaupy.select(menuRaca, cursor='->', cursor_style='red', return_index = True) + 1
    nomeAnimal = input("Nome do animal: ")
    tipoAnimal = input("Tipo de animal: ")
    dono = input("Dono: ")
    insertedRows = insertAnimalDB(raca_id, nomeAnimal, tipoAnimal, dono)
    print("Animal inserido com sucesso" if insertedRows else "Não foi possível adicionar o animal")
 
def menu():
    while True:
        print("""
            1 - Inserir Raça
            2 - Inserir Animal
            3 - Imprimir animais
            4 - Pesquisar animal por dono
            5 - Sair
            """)
        op = int(input("Indique a opção desejada: "))
        match op:
            case 1:
                print("Inserir raça:")
                insertRacaDB(input("Raça: "))
            case 2:
                insertAnimal()
            case 3:
                printAllAnimals()
            case 4:
                printAllAnimalsByDono(input("Dono: "))
            case 5:
                break
            case _:
                print("\nErro: opção inválida\n")
 
menu()