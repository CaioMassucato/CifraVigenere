#!/usr/bin/python3
# -*- coding: utf-8 -*


from CifraVigenere import cifracao, decifracao
from functools import reduce

# Encontra os fatores de um dado número n
def Fatores(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

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
# para então calcular os fatores das distâncias entre as repetições
# para aproximar o tamanho da chave
def SequenciasRepetidas(string):
    repetidas = []
    indexRepetidas = []
    partida = 0
    
    while partida <= len(string):
        for x in range(1, len(string)):
            substring = string[partida:x]

            # Testa caracter a caracter os matches com mais de 3 caracteres
            if len(substring) > 3 and string[x:].find(substring) != -1:
                substringAux = substring
            
            # Se a substring é maior que 3, não possui um match e a substring-1
            # possui um match, guarda a substring -1 na lista e move o contador
            # de varredura para depois dessa sequência que possui um match
            elif len(substring) > 3 and string[x:].find(string[partida:x-1]) != -1:
                repetidas.append(string[partida:x-1])
                indexRepetidas.append(string[x:].index(string[partida:x-1]) + 1)

                # Calcula os fatores de cada distância entre repetições
                fatoresAux = []
                fatores = {}
                for numero in indexRepetidas:
                    fatoresAux.append(Fatores(numero))
                
                # Organiza o número de ocorrências para cada fator
                for conjunto in fatoresAux:
                    for valor in conjunto:
                        if valor in fatores:
                            fatores[valor] += 1
                        else:
                            fatores[valor] = 1

                partida = x
            
            if x == (len(string) -1):
                partida +=1

    print("Fatores e suas ocorrências::")
    fatoresSorted = sorted(fatores.items(), key=lambda x: x[1], reverse=True)
    for i in fatoresSorted[1:20]: print(i[0], ": ", i[1])
    print()

    return fatores

# Testes
cifraTeste = cifracao()
SequenciasRepetidas(cifraTeste)
grupo1 = Agrupa(cifraTeste, 0, 3)
FrequenciaLetras(grupo1)