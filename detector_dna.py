'''detecta secuencias de 4 caracteres identicos en cada fila de 6 o 4 elementos'''
def detectorDna(dna, contador_de_secuencias):
    for fila in dna:
        if len(fila) == 6:
            for i in range(3):
                if fila[i] == fila[i+1] and fila[i] == fila[i+2] and fila[i] == fila[i+3]:
                    contador_de_secuencias+=1
                    if contador_de_secuencias > 1:
                        return contador_de_secuencias, True
        elif len(fila) == 4: 
            if fila[0] == fila[1] and fila[0] == fila[2] and fila[0] == fila[3]:
                contador_de_secuencias+=1
                if contador_de_secuencias > 1:
                    return contador_de_secuencias, True
    return contador_de_secuencias, False