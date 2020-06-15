from model.conexion_twitter import *
from app_diccionarios import *
from app_textbloob import *
import numpy as np
import pandas as pd


def refrescar_data(texto):
    if texto != "":
        buscar_tweets(texto)
        # run_diccionarios()
        run_textbloob2()
        run_textbloob()


def tabla_coseno_vectorial(texto):
    refrescar_data(texto)
    data = pd.read_csv("results/clasificacion_coseno_vectorial.csv", error_bad_lines=False)
    coseno = np.array(data[:-1])
    id = []
    sentimiento = []
    tweet = []

    for row in coseno:
        id.append(int(row[0]))
        sentimiento.append(row[1])
        tweet.append(row[2])
        datos = {'id': id, 'sentimiento': sentimiento, 'tweet': tweet}
    return datos


def tabla_jaccard(texto):
    refrescar_data(texto)
    data = pd.read_csv("results/clasificacion_jaccard.csv", error_bad_lines=False)
    jaccard = np.array(data[:-1])
    id = []
    sentimiento = []
    tweet = []

    for row in jaccard:
        id.append(int(row[0]))
        sentimiento.append(row[1])
        tweet.append(row[2])
        dato = {'id': id, 'sentimiento': sentimiento, 'tweet': tweet}
    return dato


def tabla_arboles():
    data = pd.read_csv("results/clasificacion_arboles.csv", error_bad_lines=False)
    jaccard = np.array(data[:-1])
    print(jaccard)
    id = []
    sentimiento = []
    tweet = []
    acertividad = []
    for row in jaccard:
        id.append(int(row[0]))
        sentimiento.append(row[1])
        acertividad.append(row[2])
        tweet.append(row[3])
        dato = {'id': id, 'sentimiento': sentimiento, 'tweet': tweet, 'acertividad': acertividad}
    return dato


def tabla_textbloob(texto):
    refrescar_data(texto)
    data = pd.read_csv("results/clasificacion_textbloob.csv", error_bad_lines=False)
    jaccard = np.array(data[:-1])
    id = []
    sentimiento = []
    tweet = []

    for row in jaccard:
        id.append(int(row[0]))
        sentimiento.append(row[1])
        tweet.append(row[2])
        dato = {'id': id, 'sentimiento': sentimiento, 'tweet': tweet}
    return dato
