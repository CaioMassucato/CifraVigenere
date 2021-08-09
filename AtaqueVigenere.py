#!/usr/bin/python3
# -*- coding: utf-8 -*

from CifraVigenere import cifracao, decifracao


cifraEx = "euqueroatacaraalemanhaaoamanhecer"


# Agrupa as letras dada uma cifra, um ponto de partida e um intervalo
def Agrupa(cifra, start, skip):
    grupoLetras = ""
    for index in range(start, len(cifra), skip):
        grupoLetras += cifra[index]

    print("Grupo de Letras Selecionadas ::")
    print()
    print(grupoLetras)
    print()
    return grupoLetras

# Calcula a frequência de cada letra no grupo
def FrequenciaLetras(grupo):
    ocorrencias = {}
    indices = ocorrencias.keys()

    # Calcula a ocorrência de cada letra. Ex: "letra 'a' aparece 3 vezes"
    for letra in grupo:
        if letra in indices:
            ocorrencias[letra] += 1
        else:
            ocorrencias[letra] = 1
    
    frequencias = {}

    # Calcula a frequencia de cada letra com base na ocorrência
    for indice in indices:
        valor = ocorrencias.get(indice)
        frequencias[indice] = (valor/len(grupo)) * 100

    print("Frequência de cada letra do grupo ::")
    print()
    print(frequencias)
    print()
    return frequencias

def repeats(string):
    partida = 0
    while partida <= len(string):
        for x in range(1, len(string)):
            substring = string[partida:x]

            if len(substring) > 2 and string[x:].find(substring) != -1:
                print(substring)
                print()
            
            if x == (len(string) -1):
                partida +=1

    print(string)

# Testes
cifraTeste = cifracao()
print(cifraTeste)
print()
repeats(cifraTeste)
print()
grupo1 = Agrupa(cifraTeste, 0, 3)