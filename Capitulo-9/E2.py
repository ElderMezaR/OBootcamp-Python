from functools import reduce
lista = input('Hola, pasame los elementos de una lista separados por una coma: ')
lista_2 = lista.split(', ')
impares = list(filter(lambda x: int(x)%2 != 0, lista_2))
suma = reduce(lambda x, y: int(x) + int(y), impares)
print(f'Tu lista era: {lista_2} y los numeros impares son: {impares}. Todos ellos suman {suma}')
