from textblob import TextBlob
from controller.csv import *
import pandas as pd

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
