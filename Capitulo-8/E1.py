def main():
    #Creamos nuestro docuemnto.txt
    f = open("mi_fichero.txt", 'x')
    f.close()
    #Aqui lo volvemos a abri y escribimos en el
    f = open("mi_fichero.txt", 'w')
    f.write("Hola como te llamas?\n")
    f.write("Yo me llamo Python\n")
    f.write("Mucho gusto de conocerte\n")
    f.close()



if __name__ == "__main__":
    main()
