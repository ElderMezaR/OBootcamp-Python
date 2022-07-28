import sqlite3


def buscar_alumno(nombres):
    return curs.execute("SELECT * FROM Alumnos WHERE Nombre = '%s'" %nombres)




conn = sqlite3.connect('Mibase.db')
curs = conn.cursor()
curs.execute("DROP TABLE IF EXISTS ALUMNOS")

tabla = """CREATE TABLE ALUMNOS(
           ID INT PRIMARY KEY,
           Nombre TEXT,
           Apellido TEXT
            );
        """
curs.execute(tabla)

###Creamos una lista con la informacion de cada alumno
alumnos = [
            [1, 'Esteban', 'Reyes'],
            [2, 'Veronica', 'Martinez'],
            [3, 'Alejandro', 'Meza'],
            [4, 'Sebastian', 'Ramos'],
            [5, 'Daniela', 'Palomares'],
            [6, 'Berenice', 'Garcia'],
            [7, 'Dulce', 'Castillo'],
            [8, 'Daniel', 'Torres']
]

###Creamos nuestra tabla
for alumno in alumnos:

    query = '''INSERT INTO ALUMNOS(ID, Nombre, Apellido) VALUES (?,?,?)'''
    rows = curs.execute(query, (alumno[0], alumno[1], alumno[2]))

conn.commit()

### Aqui buscamos al alumno  que deseamos usando su nombre
el_alumno = buscar_alumno('Sebastian')
for i in el_alumno:
    print(i)


curs.close()
conn.close()
