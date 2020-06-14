from controller.diccionarios import *
from controller.distancias import *
from controller.nlp import *
from controller.csv import *
import pandas as pd


def run_diccionarios():
    # GENERACION DE DICCIONARIOS
    negativas = diccionario_negativo()
    positivas = diccionario_positivo()

    # EXTRACCIÓN DE TWEETS
    data = pd.read_csv("model/tweets.csv")
    tweets = data[data.columns[1]]
    respaldo = tweets
    # tweets = tweets[:20]

    # NLP
    tweets = tweets.values.tolist()
    tweets = nlp(tweets)

    # CLASIFICACION
    data = clasificacion_coseno_vectorial(tweets, respaldo, positivas, negativas)
    toCSV("results/clasificacion_coseno_vectorial.csv", data)
    data = clasificacion_jaccard(tweets, respaldo, positivas, negativas)
    toCSV("results/clasificacion_jaccard.csv", data)
    print("Resultados Generados!")
