from modificador_de_matrices import matrizComlumnas, matrizDigonales
from detector_dna import detectorDna

'''la funcion recibe como argumento la matriz dna
crea un contador de secuencias la cual usa como argumento
para la funcion detector y luego modifico el valor del contador con lo que me devuelve el detector
llama a la funcion MatrizDiagonales
para que modificque la matriz de forma tal que cuando vuelva a llamar 
al detector me evalue las secucencias diagonales ascendentes, luego hace lo 
mismo para evaluar las verticales y las diagonales inferiores, el detector
cada vez que lo llamo evalua si la cantidad de secuencia es mayor a 1 solo 
trabaja si es igual o menor, si es mayor a uno modifica la variable is mutant por un TRUE que 
es lo que devuelve al final esta funcion'''
def isMutant(dna):
    contador_de_secuencias = 0
    is_mutant=False
    while not is_mutant:
        contador_de_secuencias, is_mutant = detectorDna(dna, contador_de_secuencias)
        matriz_de_digonales_descendentes = matrizDigonales(dna)
        contador_de_secuencias, is_mutant = detectorDna(matriz_de_digonales_descendentes, contador_de_secuencias)
        matriz_de_comlumnas = matrizComlumnas(dna)
        contador_de_secuencias, is_mutant = detectorDna(matriz_de_comlumnas, contador_de_secuencias)
        matriz_de_digonales_ascendentes = matrizDigonales(matriz_de_comlumnas)
        contador_de_secuencias, is_mutant = detectorDna(matriz_de_digonales_ascendentes, contador_de_secuencias)
    return is_mutant

if __name__ == "__main__":
    dna = ["ATGCGA","CAGTGC","TTATGT","AGAAGG","CCCCTA","TCACTG"]
    print(isMutant(dna))
