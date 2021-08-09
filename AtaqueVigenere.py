#!/usr/bin/python3
# -*- coding: utf-8 -*

from CifraVigenere import cifracao, decifracao

# Agrupa as letras dados uma cifra, um ponto de partida e um intervalo
def Agrupa(cifra, start, skip):
    grupoLetras = ""
    for index in range(start, len(cifra), skip):
        grupoLetras += cifra[index]

    print("Grupo de Letras Selecionadas ::")
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
    print(frequencias)
    print()
    return frequencias

# Encontra sequências de caracteres repetidos na mensagem cifrada
def SequenciasRepetidas(string):
    repetidas = []
    partida = 0
    
    while partida <= len(string):
        for x in range(1, len(string)):
            substring = string[partida:x]

            # Testa caracter a caracter os matches com mais de 3 caracteres
            if len(substring) > 3 and string[x:].find(substring) != -1:
                substringAux = substring
                # print(substringAux)
            
            # Se a substring é maior que 3, não possui um match e a substring-1
            # possui um match, guarda a substring -1 na lista e move o contador
            # de varredura para depois dessa sequência que possui um match
            elif len(substring) > 3 and string[x:].find(string[partida:x-1]) != -1:
                repetidas.append(string[partida:x-1])
                partida = x
                print("Substrings repetidas :: ")
                print(repetidas)
                print()
            
            if x == (len(string) -1):
                partida +=1
    return 0

# Testes
cifraTeste = cifracao()
SequenciasRepetidas(cifraTeste)
grupo1 = Agrupa(cifraTeste, 0, 3)
FrequenciaLetras(grupo1)