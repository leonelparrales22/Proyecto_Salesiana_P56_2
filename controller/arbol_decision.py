from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from controller.distancias import *


def clasificacion_arbol_de_desicion(tweets, respaldo, sentimiento):
    tweets = np.array(tweets)

    diccionario = crearDiccionario(tweets)
    bolsa = bolsa_de_palabras(diccionario, tweets)
    bolsa = bolsa.transpose()
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

    print(y_test)

    # Modelo de Árboles de Decisión Clasificación
    algoritmo = DecisionTreeClassifier()
    algoritmo.fit(X_train, y_train)
    Y_pred = algoritmo.predict(X_test)
    print('Precisión Árboles de Decisión Clasificación: {}'.format(algoritmo.score(X_train, y_train)))

    contador = 1
    data = []
    contador_correctos = 0
    contador_incorrectos = 0
    contador_positivos = 0
    contador_negativos = 0
    contador_neutros = 0
    for x, y, z in zip(c_X_train, Y_pred, y_test):
        if y == "POSITIVO":
            contador_positivos += 1
        if y == "NEGATIVO":
            contador_negativos += 1
        if y == "NEUTRO":
            contador_neutros += 1

        if y == z:
            validacion = "CORRECTO"
            contador_correctos += 1
        else:
            validacion = "INCORRECTO"
            contador_incorrectos += 1
        data.append(
            str(contador) + ";" + y.replace('\n', ' ') + ";" + validacion + ";" + str(x[-1]))
        contador += 1
    contador = contador - 1
    contador_incorrectos = contador_incorrectos / contador
    contador_positivos = contador_positivos / contador
    contador_negativos = contador_negativos / contador
    contador_neutros = contador_neutros / contador
    data.append(str(contador_incorrectos) + ";" + str(contador_positivos) + ";" + str(
        contador_negativos) + ";" + str(contador_neutros))
    return data
