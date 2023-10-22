"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""

import csv
from collections import Counter
with open('data.csv') as f:
    documento = csv.reader(f, delimiter= '\t' )
    datos = list(documento)  # Almacena los datos en una lista 

def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214
    """
    x = 0
    x = sum([int(row[1]) for row in datos])
    return x

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    x = list(tuple(Counter([row[0] for row  in datos]).items()))
    x.sort()
    return x

#print(pregunta_02())

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.
    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]
    """
    x = []
    letras = sorted(set([str(row[0]) for row in datos]))
    for i in letras:
        x.append(sum(([int(row[1]) for row in datos if row[0] == i])))
    l = list(zip(letras,x))
    return l  

#print(pregunta_03())

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.
    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]
    """
    x = list(tuple(Counter([row[2][:][5:7] for row  in datos]).items()))
    x.sort()
    return x

#print(pregunta_04())

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.
    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]
    """
    minimos = []
    maximos = []
    letras = sorted(set([str(row[0]) for row in datos]))
    for i in letras:
        x = (([int(row[1]) for row in datos if row[0] == i]))
        minimos.append(min(x))
        maximos.append(max(x))
    l = list(zip(letras,maximos,minimos))
    return l

#print(pregunta_05())

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.
    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]
    """
    minimos = []
    maximos = []
    l = [elemento.split(":") for row in datos for elemento in row[4].split(",")]
    cad_letras = sorted(set([elemento[0] for elemento in l]))
    for j in cad_letras:
        valores = (([int(i[1]) for i in l if i[0] == j]))
        minimos.append(min(valores))
        maximos.append(max(valores))
    minimos = [min([int(i[1]) for i in l if i[0] == j]) for j in cad_letras]    
    b = list(zip(cad_letras,minimos,maximos))
    return b

#print(pregunta_06())

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 1 y 2. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.
    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]
    """
    x = []
    numeros = sorted(set([int(row[1]) for row in datos]))
    for numero in numeros:
        c = list([row[0] for row in datos if int(row[1]) == numero])
        x.append(c)
    l = list(zip(numeros,x))
    return l

#print(pregunta_07())

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.
    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]
    """
    x = []
    numeros = list(sorted(set([int(row[1]) for row in datos])))
    c = (sorted(set([row[0] for row in datos if int(row[1]) == numero])) for numero in numeros)
    #x.append(c)
    l = list(zip(numeros,c))
    return l

#print(pregunta_08())

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.
    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }
    """
    l = [elemento.split(":")[0] for row in datos for elemento in row[4].split(",")]
    x = dict(sorted(Counter(l).items()))
    return x

#print(pregunta_09())

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.
    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]
    """
    x = [(row[0],len(row[3].split(",")),len(row[4].split(","))) for row in datos]
    return x

#print(pregunta_10())

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.
    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    """
    letras = sorted(list(set([elemento for row in datos for elemento in row[3].split(",")])))
    x = {letra: sum([int(row[1]) for row in datos if letra in row[3]]) for letra in letras }
    return x

#print(pregunta_11())

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.
    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }
    """
    letras = sorted(set([row[0] for row in datos]))
    x = {letra:sum([int(elementos.split(":")[1]) for row in datos for elementos in row[4].split(",") if row[0] == letra]) for letra in letras}
    return x

#print(pregunta_12())