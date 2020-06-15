import csv


def toCSV(nombre, contenido):
    myFile = open(nombre, 'w')
    with myFile:
        writer = csv.writer(myFile, delimiter=',')
        writer.writerow(["ItemID", "Sentiment", "SentimentText"])
        for x in contenido:
            writer.writerow(x.split(";"))
    return True


def toCSV2(nombre, contenido):
    myFile = open(nombre, 'w')
    with myFile:
        writer = csv.writer(myFile, delimiter=',')
        writer.writerow(["ItemID", "Sentiment", "Acertividad", "SentimentText"])
        for x in contenido:
            writer.writerow(x.split(";"))
    return True
