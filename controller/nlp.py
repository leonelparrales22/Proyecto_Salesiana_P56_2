from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import re


def normalizacion(textos):
    for i, texto in enumerate(textos):
        texto = texto.lower()
        texto = re.sub("[^A-Za-z0-9’áéíóúÁÉÍÓÚ]+", ' ', texto)
        textos[i] = texto
    return textos


def tokenizacion(textos):
    for i, texto in enumerate(textos):
        textos[i] = texto.strip().split()
    return textos


def deleteStopWords(textos):
    sw = stopwords.words('spanish')
    for i, texto in enumerate(textos):
        copia = texto[:]
        for palabra in copia:
            if palabra in sw:
                texto.remove(palabra)
    return textos


def stemming(textos):
    stemmer = PorterStemmer()
    for texto in textos:
        for i, palabra in enumerate(texto):
            texto[i] = stemmer.stem(palabra)
    return textos


def nlp(texto):
    texto = normalizacion(texto)
    texto = tokenizacion(texto)
    texto = deleteStopWords(texto)
    texto = stemming(texto)
    return texto


def stemming2(textos):
    stemmer = PorterStemmer()
    for i, palabra in enumerate(textos):
        palabra = palabra.strip()
        palabra = stemmer.stem(palabra)
        textos[i] = palabra
    return textos


def create_dictionary(texto):
    texto = normalizacion(texto)
    texto = stemming2(texto)
    return texto
