from flask import Flask, render_template, request
import io
import random
import pandas as pd
import numpy as np
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from visualizar import *

app = Flask(__name__)


@app.route('/plot.png')
def plot_png():
    fig = create_figure()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_figure():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    xs = [0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0]
    ys = [10.0, 5.0, 2.0, 1.0, 0.5, 0.2, 0.1]
    axis.plot(xs, ys)
    return fig


@app.route('/')
def index() -> 'html':
    return render_template("index.html")


@app.route('/textblood', strict_slashes=False)
def textblood():
    sentimiento = ['sentimiento']
    tweet = ['tweet']
    return render_template("textblood.html", title="Clasificacion TextBlood", tabla=tabla_textbloob())


@app.route('/regresion', strict_slashes=False)
def regresion():
    sentimiento = ['sentimiento']
    tweet = ['tweet']
    return render_template("regresion.html", title="Clasificacion Arboles", tabla=tabla_arboles())


@app.route('/coseno', methods=['GET'])
def coseno() -> 'html':
    sentimiento = ['sentimiento']
    tweet = ['tweet']
    return render_template('coseno.html', title="Clasificacion Coseno Vectorial", tabla=tabla_coseno_vectorial())


@app.route('/jaccard', methods=['GET'])
def jaccard() -> 'html':
    sentimiento = ['sentimiento']
    tweet = ['tweet']
    return render_template('jaccard.html', title1="Clasificacion Jaccard", tabla=tabla_jaccard())


if __name__ == '__main__':
    app.run(debug=True)
