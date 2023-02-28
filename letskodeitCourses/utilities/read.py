import csv

def GetData(fileName):

    # Crea un lista vacia para almacenar las filas que seran recibidas por el archivo ".csv"
    rows= []
    # Abre el archivo CSV en modo de leer
    dataFile = open(fileName, "r")
    # Crea el  CSV leector desde el archvio CSV
    reader = csv.reader(dataFile)
    # Salta el "header"
    next(reader)
    # Añade las filas del leector
    for row in reader:
        rows.append(row)
    return rows
