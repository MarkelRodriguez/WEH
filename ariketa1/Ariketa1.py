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

    # Recupera todos los resultados de la consulta
    resultados = cursor.fetchall()

    # Procesa y muestra los resultados
    for fila in resultados:
        print(f"DNI: {fila[0]}, Izena: {fila[1]}")

    # Cierra la conexión a la base de datos
    conexion.close()


def erabiltzaileakSartu(dni, izena):
    insert_query = "INSERT INTO erabiltzailea (Dni, edad) VALUES ("+dni +"," + izena+" )"
    cursor.execute(insert_query)
    # Confirma los cambios en la base de datos
    conexion.commit()

    # Cierra la conexión a la base de datos
    conexion.close()




print("1. izen berria sartu")
print("2. izen guztiak atera")
print("3. eguneratu")
print("4. ezabatu")
opcion = input('sartu eragiketa bat:')
if opcion == '1':

elif opcion == '2':
    edad = input('Digita tu edad: ')
    if edad.isnumeric():
        print('Tu edad es {}'.format(edad))
    else:
        print('Has digitado una edad no valida...')
elif opcion == '3':
    email = input('Digita tu email: ')
    if email.find('@')>=0 and email.find('.')>=0:
        print('Tu e-mail es {}'.format(email))
    else:
        print('Has digitado un email no valido...')
else:
    print('Debes digitar un numero entre 1 y 3')
    print('=-='*20)


def erabiltzaileaSartu():
"""

