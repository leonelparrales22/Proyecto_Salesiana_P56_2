import numpy as np
import copy
import math


def crearDiccionario(matriz):
    diccionario = []
    for row in matriz.flatten():
        for element in row:
            if not element in diccionario:
                diccionario.append(element)
    return diccionario


def bolsa_de_palabras(diccionario, matriz):
    frecuencias = []
    for element in diccionario:
        aux = []
        for row in matriz:
            frecuencia = row.count(element)
            aux.append(frecuencia)
        frecuencias.append(aux)
    frecuencias = np.array(frecuencias)
    return frecuencias


def pesado_tf(matriz):
    for element in np.nditer(matriz, op_flags=['readwrite']):
        if element == 0:
            resultado = 0
        else:
            resultado = 1 + math.log10(element)
        element[...] = resultado
    return matriz


def pesado_idf(frecuencias):
    idf = []
    for column in frecuencias.transpose():
        contador = 0
        for value in column:
            if value > 0:
                contador += 1
        # CAMBIAR EL 1 POR EL CERO
        contador = math.log10(frecuencias.shape[0] / contador)
        idf.append(contador)
    return idf


def tf_idf2(tf, idf):
    resultado = np.multiply(tf, idf)
    return np.array(resultado)


def long_normalizado(matriz):
    for column in matriz:
        contador = 0
        for value in column:
            contador = contador + value ** 2
        modulo = math.sqrt(contador)
        for element in np.nditer(column, op_flags=['readwrite']):
            if modulo > 0:
                element[...] = element / modulo
            else:
                element[...] = 0
    return matriz


def distancia_similitud(matriz):
    contador = 0
    for x, y in zip(matriz[0], matriz[1]):
        contador = contador + x * y
    # if posicion == posicion2:
    #     aux.append(1)
    # else:
    #     aux.append(round(contador, 2))
    return contador


def coseno_vectorial(frecuencias):
    tf = pesado_tf(copy.deepcopy(frecuencias))
    idf = pesado_idf(copy.deepcopy(frecuencias))
    tf_idf = tf_idf2(tf, idf)
    long_norm = long_normalizado(tf_idf)
    resultado = distancia_similitud(long_norm)
    resultado = np.array(resultado)
    return resultado


def similitud_coseno_vectorial(vector):
    vector.append(['comodin'])
    array = np.array(vector)
    diccionario = crearDiccionario(array)
    frecuencias = bolsa_de_palabras(diccionario, array)
    frecuencias = frecuencias.transpose()
    frecuencias = frecuencias.astype(float)
    return coseno_vectorial(frecuencias)


def clasificacion_coseno_vectorial(tweets, respaldo, diccionario_positivo, diccionario_negativo):
    data = []
    contador = 1
    for x, y in zip(tweets, respaldo):
        textos = [x, diccionario_positivo]
        similitud_positiva = similitud_coseno_vectorial(textos)
        textos = [x, diccionario_negativo]
        similitud_negativa = similitud_coseno_vectorial(textos)
        # CLASIFICADOR:
        if similitud_positiva > similitud_negativa:
            sentimiento = "POSITIVO"
        if similitud_positiva < similitud_negativa:
            sentimiento = "NEGATIVO"
        if similitud_positiva == similitud_negativa:
            sentimiento = "NEUTRO"
        data.append(str(contador) + ";" + sentimiento + ";" + y.replace('\n', ' '))
        contador += 1
    return data


def jaccard(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return len(s1.intersection(s2)) / len(s1.union(s2))


def clasificacion_jaccard(tweets, respaldo, diccionario_positivo, diccionario_negativo):
    data = []
    contador = 1
    for x, y in zip(tweets, respaldo):
        similitud_positiva = jaccard(x, diccionario_positivo)
        similitud_negativa = jaccard(x, diccionario_negativo)
        # CLASIFICADOR:
        if similitud_positiva > similitud_negativa:
            sentimiento = "POSITIVO"
        if similitud_positiva < similitud_negativa:
            sentimiento = "NEGATIVO"
        if similitud_positiva == similitud_negativa:
            sentimiento = "NEUTRO"
        data.append(str(contador) + ";" + sentimiento + ";" + y.replace('\n', ' '))
        contador += 1
    return data
