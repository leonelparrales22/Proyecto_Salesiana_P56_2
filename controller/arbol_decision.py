from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from controller.distancias import *


def clasificacion_arbol_de_desicion(tweets, respaldo, sentimiento):
    tweets = np.array(tweets)

    diccionario = crearDiccionario(tweets)
    bolsa = bolsa_de_palabras(diccionario, tweets)
    bolsa = bolsa.transpose()
    print(bolsa.shape)
    bolsa = np.append(bolsa.transpose(), np.array([respaldo]), axis=0)
    bolsa = bolsa.transpose()

    # Separo todos los datos con las características y las etiquetas o resultados
    X = bolsa
    Y = sentimiento
    # Separo los datos de "train" en entrenamiento y prueba para probar los algoritmos
    c_X_train, c_X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3)
    print('Son {} datos para entrenamiento y {} datos para prueba'.format(c_X_train.shape[0], c_X_test.shape[0]))

    X_train = c_X_train[:, :-1]
    X_test = c_X_test[:, :-1]
    X_train = X_train.astype(np.float)
    X_test = X_test.astype(np.float)

    # Modelo de Árboles de Decisión Clasificación
    algoritmo = DecisionTreeClassifier()
    algoritmo.fit(X_train, y_train)
    Y_pred = algoritmo.predict(X_test)
    print('Precisión Árboles de Decisión Clasificación: {}'.format(algoritmo.score(X_train, y_train)))

    contador = 0
    data = []
    for x, y in zip(c_X_train, Y_pred):
        data.append(str(contador + 1) + ";" + y.replace('\n', ' ') + ";" + str(x[-1]))
        contador += 1
    return data
