from classifier import SentimentClassifier
from textblob import TextBlob
from controller.csv import *
import pandas as pd


def run_textbloob():
    # EXTRACCIÓN DE TWEETS
    data = pd.read_csv("model/tweets.csv", error_bad_lines=False)
    tweets = data[data.columns[1]]
    contador = 1
    contador_positivos = 0
    contador_negativos = 0
    contador_neutros = 0
    data = []
    for texto in tweets:
        eb = TextBlob(texto)
        eb = eb.translate(to="en")
        sentimiento = eb.sentiment[0]
        if sentimiento < 0:
            data.append(str(contador) + ";" + "NEGATIVO" + ";" + str(texto))
        if sentimiento > 0:
            data.append(str(contador) + ";" + "POSITIVO" + ";" + str(texto))
        if sentimiento == 0:
            data.append(str(contador) + ";" + "NEUTRO" + ";" + str(texto))
        contador += 1
    contador = contador - 1
    contador_positivos = contador_positivos / contador
    contador_negativos = contador_negativos / contador
    contador_neutros = contador_neutros / contador
    data.append(str(contador_positivos) + ";" + str(contador_negativos) + ";" + str(contador_neutros))
    toCSV("results/clasificacion_textbloob.csv", data)
    print("Resultados Generados!")


def run_textbloob2():
    # EXTRACCIÓN DE TWEETS
    data = pd.read_csv("model/tweets.csv", error_bad_lines=False)
    tweets = data[data.columns[1]]
    clf = SentimentClassifier()
    data = []
    contador = 1
    contador_positivos = 0
    contador_negativos = 0
    contador_neutros = 0
    for texto in tweets:
        print(texto)
        sentimiento = clf.predict(texto)
        sentimiento_texto = ""
        if 0 <= sentimiento <= 0.4:
            sentimiento_texto = "NEGATIVO"
            contador_negativos += 1
        if 0.6 <= sentimiento <= 1:
            sentimiento_texto = "POSITIVO"
            contador_positivos += 1
        if 0.4 < sentimiento < 0.6:
            sentimiento_texto = "NEUTRO"
            contador_neutros += 1
        data.append(str(contador) + ";" + sentimiento_texto + ";" + str(texto).replace('\n', ' '))
        contador += 1
    contador = contador - 1
    contador_positivos = contador_positivos / contador
    contador_negativos = contador_negativos / contador
    contador_neutros = contador_neutros / contador
    data.append(str(contador_positivos) + ";" + str(contador_negativos) + ";" + str(contador_neutros))
    toCSV("results/clasificacion_textbloob.csv", data)
    print("Resultados Generados!")


def run_textbloob3():
    ########VADER#########
    # !pip install vadersentiment
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    import pandas as pd
    data = pd.read_csv("model/TWEETS/tweets.csv", error_bad_lines=False)
    tweets = data[data.columns[1]]
    analyzer = SentimentIntensityAnalyzer()
    contador_positivos = 0
    contador_negativos = 0
    contador_neutros = 0
    contador = 1
    for texto in tweets:
        sentimiento = analyzer.polarity_scores(texto)['compound']
        sentimiento_texto = ""
        if 0 <= sentimiento <= 0.4:
            sentimiento_texto = "NEGATIVO"
            contador_negativos += 1
            print(str(sentimiento))
        if 0.6 <= sentimiento <= 1:
            sentimiento_texto = "POSITIVO"
            contador_positivos += 1
            print(str(sentimiento))
        if 0.4 < sentimiento < 0.6:
            sentimiento_texto = "NEUTRO"
            contador_neutros += 1
            print(str(sentimiento))
        # data.append(str(contador) + ";" + sentimiento_texto + ";" + str(texto).replace('\n', ' '))


# run_textbloob()
# run_textbloob2()
# run_textbloob3()
