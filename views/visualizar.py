from scipy.interpolate import InterpolatedUnivariateSpline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# def ver():
#     x=[0.1,0.2,0.5,1.0,2.0,5.0,10.0]
#     y=[10.0,5.0,2.0,1.0,0.5,0.2,0.1]

#     f_interp= InterpolatedUnivariateSpline(x,y, k=3)
#     f_interp

#     x1=np.linspace(0.1,10)
#     y_interp=f_interp(x1)
#     plt.plot(x,y,'x',mew=3)
#     grafica=plt.plot(x1,y_interp)

#     return grafica


def ver():
    data = pd.read_csv("../results/clasificacion_coseno_vectorial.csv",error_bad_lines=False)
    coseno = np.array(data)
    id=[]
    sentimiento=[]
    tweet=[]
    
    for row in coseno: 
        id.append(row[0])
        sentimiento.append(row[1])
        tweet.append(row[2])
        datos = {'id':id, 'sentimiento':sentimiento,'tweet': tweet} 
    return datos

def ver1():
    dato = pd.read_csv("../results/clasificacion_jaccard.csv",error_bad_lines=False)
    jaccard = np.array(dato)
    id=[]
    sentimiento=[]
    tweet=[]
    
    for row in jaccard: 
        id.append(row[0])
        sentimiento.append(row[1])
        tweet.append(row[2])
        dato = {'id':id, 'sentimiento':sentimiento,'tweet': tweet} 
    return dato

def ver2():
    dato = pd.read_csv("../results/clasificacion_arboles.csv",error_bad_lines=False)
    jaccard = np.array(dato)
    id=[]
    sentimiento=[]
    tweet=[]
    
    for row in jaccard: 
        id.append(row[0])
        sentimiento.append(row[1])
        tweet.append(row[2])
        dato = {'id':id, 'sentimiento':sentimiento,'tweet': tweet} 
    return dato

def ver3():
    dato = pd.read_csv("../results/clasificacion_textbloob.csv",error_bad_lines=False)
    jaccard = np.array(dato)
    id=[]
    sentimiento=[]
    tweet=[]
    
    for row in jaccard: 
        id.append(row[0])
        sentimiento.append(row[1])
        tweet.append(row[2])
        dato = {'id':id, 'sentimiento':sentimiento,'tweet': tweet} 
    return dato