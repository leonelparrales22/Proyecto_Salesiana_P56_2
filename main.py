from flask import Flask, render_template, request
from visualizar import *
import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import matplotlib.pyplot as plt

app = Flask(__name__)


@app.route('/plot_coseno.png')
def plot_coseno():
    fig = create_figure("Coseno Vectorial", "results/clasificacion_coseno_vectorial.csv")
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/plot_jaccard.png')
def plot_jaccard():
    fig = create_figure("Jaccard", "results/clasificacion_jaccard.csv")
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/plot_textblood.png')
def plot_textblood():
    fig = create_figure("TextBlob", "results/clasificacion_textbloob.csv")
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_figure(titulo, ruta):
    data = pd.read_csv(ruta, error_bad_lines=False)
    data = data.values.tolist()
    data = data[-1]
    labels = 'Neutros', 'Negativos', 'Positivos'
    sizes = [data[2], data[1], data[0]]
    explode = (0, 0, 0)
    fig, ax1 = plt.subplots()
    fig.suptitle('Clasificación de Tweets - ' + titulo, fontsize=16)
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    return fig


@app.route('/')
def index() -> 'html':
    return render_template("index.html")


@app.route('/textblood', methods=['GET', 'POST'], strict_slashes=False)
def textblood():
    texto = parametro_texto()
    return render_template("textblood.html", title="Clasificacion TextBlood", tabla=tabla_textbloob(texto))


@app.route('/regresion', strict_slashes=False)
def regresion():
    return render_template("regresion.html", title="Clasificacion Arboles", tabla=tabla_arboles())


@app.route('/coseno', methods=['GET', 'POST'])
def coseno() -> 'html':
    texto = ""
    if request.method == "POST":
        texto = request.form['tweet']
    return render_template('coseno.html', title="Clasificacion Coseno Vectorial", tabla=tabla_coseno_vectorial(texto))


@app.route('/jaccard', methods=['GET', 'POST'])
def jaccard() -> 'html':
    texto = parametro_texto()
    return render_template('jaccard.html', title="Clasificacion Jaccard", tabla=tabla_jaccard(texto))


def parametro_texto():
    texto = ""
    if request.method == "POST":
        texto = request.form['tweet']
    return texto


if __name__ == '__main__':
    app.run(debug=True)
