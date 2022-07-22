class Vehiculo:
    color = "Rojo"
    ruedas = 4
    puertas = 4
class Coche(Vehiculo):
    velocidad = 160
    cilindrada = False

miChoche = Coche()
print("Tu coche es de color:", miChoche.color)
print("tiene: ", miChoche.ruedas, "ruedas")
print("y puertas tiene: ", miChoche.puertas)
print("corre hasta: ", miChoche.velocidad, "Km/h")
print("Es cilindrada?", miChoche.cilindrada)
