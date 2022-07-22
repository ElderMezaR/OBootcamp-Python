from tkinter.tix import NoteBook


class Alumno:
    _nombre = None
    _nota = None
    def setNombre(self, nombre):
        self._nombre = nombre
    def setNota(self, nota):
        self._nota = nota

    def getNombre(self):
        print(self._nombre)
    def getNota(self):
        print(self._nota)
    def aprobado(self):
        if self._nota >= 6:
            print(f"Hola {self._nombre}, tu nota final es: {self._nota}, aprobaste!")
        else:
            print(f"Hola {self._nombre} tu nota final es {self._nota}, no aprobaste.")

Yo = Alumno()
Yo.setNombre("Alejandro")
Yo.setNota(5.99)
Yo.aprobado()