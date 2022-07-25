
import pickle
class vehiculo:
    ventanas = None
    modelo = None
    puertas = None

    def __init__(self, ventanas, puertas, modelo):
        self.ventanas = ventanas
        self.puertas = puertas
        self.modelo = modelo
    def getModelo(self):
            return self.modelo
    def getPuertas(self):
            return self.puertas
    def getVentanas(self):
            return self.ventanas
        
miAuto = vehiculo(4, 5, "Jeep-Compass")

#Aqui fuardamos nuestro objeto en un archivo bin
f = open('datos.bin', 'wb')
pickle.dump(miAuto, f)
f.close()

#Aqui lo abrimos de nuevo
f = open('datos.bin', 'rb')
mi_Auto_Cargado = pickle.load(f)
f.close()

print("Esto obtuve de cargar el archivo:")
print(mi_Auto_Cargado.getModelo(), "este es el modelo")
print(mi_Auto_Cargado.getPuertas(), "puertas")
print(mi_Auto_Cargado.getVentanas(),"ventanas" )

