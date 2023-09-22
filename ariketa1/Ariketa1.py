import mysql.connector

conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        database="ariketa 1"
    )
cursor = conexion.cursor()

def erabiltzaileakIkusi():
    
    
    select_query = "SELECT * FROM erabiltzailea"

    # Ejecuta la consulta
    cursor.execute(select_query)

    # Recupera todos los resultados de 1la consulta
    resultados = cursor.fetchall()

    # Procesa y muestra los resultados
    for fila in resultados:
        print(f"DNI: {fila[0]}, Izena: {fila[1]}")

    # Cierra la conexión a la base de datos
    conexion.close()


def erabiltzaileakSartu():

    dni = input('sartu Dni-a:')
    izena = input('sartu izena:')
    insert_query = "INSERT INTO erabiltzailea VALUES ('"+ dni + "','" + izena +"')"
    cursor.execute(insert_query)
    # Confirma los cambios en la base de datos
    conexion.commit()

    # Cierra la conexión a la base de datos
    conexion.close()

def erabiltzaileakEzabatu():
    izena = input('sartu ezabatu izena:')
    delete_query = "DELETE FROM erabiltzailea WHERE Izena = '" + izena +"'"
    cursor.execute(delete_query)
    # Confirma los cambios en la base de datos
    conexion.commit()

    # Cierra la conexión a la base de datos
    conexion.close()

def erabiltzaileakEguneratu(izena):
    
    dniBerria = input('sartu Dni berria:')
    izenaBerria = input('sartu izen berria:')

    update_query = "UPDATE erabiltzailea set DNI = '" + dniBerria + "', Izena = '"+izenaBerria + "'WHERE Izena = '" + izena + "'"
    cursor.execute(update_query)
    # Confirma los cambios en la base de datos
    conexion.commit()

    # Cierra la conexión a la base de datos
    conexion.close()


print("1. izen berria sartu")
print("2. izen guztiak atera")
print("3. ezabatu")
print("4. eguneratu")
opcion = input('sartu eragiketa bat:')
if opcion == '1':

    erabiltzaileakSartu()
elif opcion == '2':
    erabiltzaileakIkusi()
elif opcion == '3':
   
   erabiltzaileakEzabatu()
elif opcion == '4':
   izena = input('sartu eguneratu izena:')
   erabiltzaileakEguneratu(izena)
else:
    print('Debes digitar un numero entre 1 y 3')
    print('=-='*20)




