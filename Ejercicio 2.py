'''Realiza el código para calcular el determinante de una matriz cuadrada de [3 x 3],
regla de Sarrus de forma recursiva y de forma iterativa.'''

lista = []
for l in range(1, 4):
    for c in range(1, 4):
        matriz = int(input(f'\033[31mType a value [{l}, {c}] '))
        lista.append(matriz)
primero = (lista[0] * lista[4] * lista[8])
segundo = (lista[1] * lista[5] * lista[6])
tercero = (lista[2] * lista[3] * lista[7])
primero2 = (lista[2] * lista[4] * lista[6])
segundo2 = (lista[0] * lista[5] * lista[7])
tercero2 = (lista[1] * lista[3] * lista[8])
sum1 = ((primero + segundo + tercero) - (primero2 + segundo2 + tercero2))
print(f'\033[34mThe result is =\033[m')
for c in range(len(lista)):
    print(f'[{lista[c] }]',end='\n' if c == 2 or c == 5 else "")
print(f'\n\033[1;34mdet(a) =  \033[1;35m{sum1}',end='')