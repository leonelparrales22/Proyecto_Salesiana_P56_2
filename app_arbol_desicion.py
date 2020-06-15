from controller.arbol_decision import *
from controller.csv import *
from controller.nlp import *
import pandas as pd

# EXTRACCIÓN DE TWEETS
data = pd.read_csv("results/final.csv", error_bad_lines=False)
tweets = data[data.columns[2]]
sentimiento = data[data.columns[1]]
sentimiento = sentimiento.values.tolist()

# NLP
respaldo = tweets.values.tolist()
tweets = tweets.values.tolist()
tweets = nlp(tweets)

# CLASIFICACION
data = clasificacion_arbol_de_desicion(tweets, respaldo, sentimiento)

# PASAR A CSV
toCSV2("results/clasificacion_arboles.csv", data)
print("Resultados Generados!")