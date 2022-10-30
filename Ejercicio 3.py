'''
Dada una lista de las naves (y vehículos) de Star Wars consideraremos a todos como naves y la debes de crear tu
de las que conocemos su nombre, largo, tripulación y cantidad de pasajeros, desarrollar los algoritmos necesarios
para resolver las actividades detalladas a continuación:
• realizar un listado ordenado por nombre de las naves de manera ascendente y por largo de las mismas de manera descendente;
• mostrar toda la información del “Halcón Milenario” y la “Estrella de la Muerte”;
• determinar cuáles son las cinco naves con mayor cantidad de pasajeros;
• indicar cuál es la nave que requiere mayor cantidad de tripulación;
• mostrar todas las naves que comienzan con AT;
• listar todas las naves que pueden llevar seis o más pasajeros;
•  mostrar toda la información de la nave más pequeña y la más grande.'''


import csv

fichero = open('vehicles.csv')
#print(fichero.read())
#print(fichero.readline())
#print(fichero.readline())

#lineas = fichero.readlines()
#print(lineas)
#['Contenido de la primera línea\n', 'Contenido de la segunda línea\n',
#'Contenido de la tercera línea\n', 'Contenido de la cuarta línea']

lineas = fichero.readlines()
#for linea in lineas:
#    print(linea)
ordenados = sorted(lineas)
for linea in lineas:
    print(linea)