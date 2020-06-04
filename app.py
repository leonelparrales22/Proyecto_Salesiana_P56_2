from controller.diccionarios import *
from controller.distancias import *
from controller.nlp import *
from controller.csv import *
import pandas as pd

# GENERACION DE DICCIONARIOS
diccionario_negativo = diccionario_negativo()
diccionario_positivo = diccionario_positivo()

# EXTRACCIÓN DE TWEETS
data = pd.read_csv("model/tweets.csv")
tweets = data[data.columns[1]]

# LUEGO BORRAR SOLO PROBANDO CON LOS PRIMEROS 20
respaldo = tweets[:20]
tweets = tweets[:20]
# LUEGO BORRAR SOLO PROBANDO CON LOS PRIMEROS 20

# NLP
tweets = tweets.values.tolist()
tweets = nlp(tweets)

# CLASIFICACION
data = clasificacion_coseno_vectorial(tweets, respaldo, diccionario_positivo, diccionario_negativo)
toCSV("results/clasificacion_coseno_vectorial.csv", data)
data = clasificacion_jaccard(tweets, respaldo, diccionario_positivo, diccionario_negativo)
toCSV("results/clasificacion_jaccard.csv", data)

print("Resultados Generados!")
