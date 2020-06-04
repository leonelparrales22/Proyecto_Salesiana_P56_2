from controller.nlp import *
import pandas as pd


def diccionario_positivo():
    return armar_diccionario("model/diccionarios/positivo.csv")


def diccionario_negativo():
    return armar_diccionario("model/diccionarios/negativo.csv")


def armar_diccionario(ruta):
    data = pd.read_csv(ruta)
    diccionario = data[data.columns[0]]
    diccionario = diccionario.values.tolist()
    diccionario = create_dictionary(diccionario)
    return diccionario
