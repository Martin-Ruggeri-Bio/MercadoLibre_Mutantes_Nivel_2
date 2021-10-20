import numpy as np

'''crea una matriz de columnas a partir de una matriz de filas'''
def matrizComlumnas(dna):
    nueva_matriz = []
    for columna in range(6):
        nueva_fila = ""
        for fila in range(len(dna)):
            nueva_fila += dna[fila][columna]
        nueva_matriz.append(nueva_fila)
    return nueva_matriz

'''crea una matriz de diagonales a partir de una matriz de filas'''
def matrizDigonales(dna):
    nuevo_dna = [list(fila) for fila in dna]
    matriz_de_diagonales = np.array(nuevo_dna)
    diags = [matriz_de_diagonales.diagonal(i).tolist() for i in range(-2, 3)]
    return diags
