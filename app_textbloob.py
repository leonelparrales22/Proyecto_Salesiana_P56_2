from classifier import SentimentClassifier
from textblob import TextBlob
from controller.csv import *
import pandas as pd


def run_textbloob():
    # EXTRACCIÓN DE TWEETS
    data = pd.read_csv("results/clasificacion_coseno_vectorial.csv", error_bad_lines=False)
    tweets = data[data.columns[2]]

    data = []
    for contador, texto in enumerate(tweets):
        eb = TextBlob(texto)
        eb = eb.translate(to="en")
        sentimiento = eb.sentiment[0]
        if sentimiento < 0:
            data.append(str(contador + 1) + ";" + "NEGATIVO" + ";" + str(texto))
        if sentimiento > 0:
            data.append(str(contador + 1) + ";" + "POSITIVO" + ";" + str(texto))
        if sentimiento == 0:
            data.append(str(contador + 1) + ";" + "NEUTRO" + ";" + str(texto))

    toCSV("results/clasificacion_textbloob.csv", data)
    print("Resultados Generados!")


def run_textbloob2():
    # EXTRACCIÓN DE TWEETS
    data = pd.read_csv("results/clasificacion_coseno_vectorial.csv", error_bad_lines=False)
    tweets = data[data.columns[2]]
    clf = SentimentClassifier()
    data = []
    for contador, texto in enumerate(tweets):
        sentimiento = clf.predict(texto)
        sentimiento_texto = ""
        if 0 <= sentimiento <= 0.4:
            sentimiento_texto = "NEGATIVO"
        if 0.6 <= sentimiento <= 1:
            sentimiento_texto = "POSITIVO"
        if 0.4 < sentimiento < 0.6:
            sentimiento_texto = "NEUTRO"
        data.append(str(contador + 1) + ";" + sentimiento_texto + ";" + str(texto))
    toCSV("results/clasificacion_textbloob.csv", data)
    print("Resultados Generados!")

# run_textbloob()
# run_textbloob2()
