
def main():
    import time
    print(time.localtime())
    hora = time.localtime()[3]
    minutos = time.localtime()[4]
    segundos = time.localtime()[5]
    if hora >= 19:
        print("Son las 7, es hora de ir a casa!")
    else:
        horas_faltantes = 18 - hora
        minutos_faltantes = 60 - minutos
        segundos_faltantes = 60 - segundos

        print(f"Faltan {horas_faltantes} horas {minutos_faltantes} minutos y {segundos_faltantes} segundos, para la hora de salida! ")











if __name__ == "__main__":
    main()

