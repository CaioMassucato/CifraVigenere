#!/usr/bin/python3
# -*- coding: utf-8 -*-

from functools import reduce
from Constantes import IC_portugues, IC_ingles, frequenciasIngles, frequenciasPortugues, dicionario

# Encontra os fatores de um dado número n
def Fatores(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

# Agrupa as letras dados uma cifra, um ponto de partida e um intervalo
def Agrupa(cifra, start, tamanhosProvaveis):
    cifra = cifra.replace(" ", "")

    print("---------------- Menu de Opções ----------------")
    for opcao in range(len(tamanhosProvaveis)):
        print(opcao+1, " - ", tamanhosProvaveis[opcao][0])
    print("------------------------------------------------")
    print()

    escolha = int(input("Qual o tamanho a ser testado? "))
    print()
    if escolha == 1:
        skip = tamanhosProvaveis[0][0]
    elif escolha == 2:
        skip = tamanhosProvaveis[1][0]
    elif escolha == 3:
        skip = tamanhosProvaveis[2][0]
    else:
        skip = -1
        print("Programa finalizado. Escolha inválida ou nenhuma escolha.")
        print()
        return 0

    grupoLetras = ""
    grupos = {}
    grupo = 0
    while grupo < skip:
        for index in range(grupo, len(cifra), skip):
            if cifra[index] != " ":
                grupoLetras += cifra[index]
        grupos[grupo] = grupoLetras
        grupoLetras = ""
        grupo += 1

        

    print("---------------- Grupos Selecionados ----------------")
    print()
    for grupo, valor in grupos.items():
        print("Grupo ", grupo, ": ", valor)
        print()
    print("-----------------------------------------------------")
    return grupos, skip

# Calcula a frequência de cada letra no grupo
def OcorrenciasLetras(grupo):
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
        frequencias[indice] = (valor/len(grupo))

    print("---------------- Frequência de cada letra do grupo ----------------")
    print()
    print(frequencias)
    print()
    return frequencias

# Encontra sequências de caracteres repetidos na mensagem cifrada
# para então calcular os fatores das distâncias entre as repetições
# para aproximar o tamanho da chave
def SequenciasRepetidas(string):
    fatores = {}
    repetidas = []
    indexRepetidas = []
    partida = 0
    
    string = string.replace(" ", "")
    if(len(string) > 3):
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
    else:
        fatores[1] = 1
        fatores[2] = 1
        fatores[3] = 1
            

    print("---------------- Tamanhos de chave mais prováveis: ----------------")
    print()
    fatoresSorted = sorted(fatores.items(), key=lambda x: x[1], reverse=True)
    fatoresSorted = fatoresSorted[1:4]
    for i in fatoresSorted: print(fatoresSorted.index(i)+1, "º: Tamanho ", i[0], " com ", i[1], " ocorrências")
    print("-------------------------------------------------------------------")
    print()

    return fatoresSorted

# Calcula o indice de concorrencia do grupo selecionado
def CalculaCI(frequencias, tamanhoChave):

    ciGrupo = 0
    for frequencia, valor in frequencias.items():
        ciLetra = valor**2
        ciGrupo += ciLetra
    ciMedio = ciGrupo / tamanhoChave

    return ciMedio

# Calcula o score Chi Quadrado para as ocorrências
def ChiQuadrado(ocorrencias, tamanhoMensagem, frequenciaLingua):
  scoreChiQuadrado = {}
  for char in frequenciaLingua.keys():
    frequenciaEsperada = frequenciaLingua[char]
    ocorrenciaEsperada = frequenciaEsperada * tamanhoMensagem
    ocorrenciaCaracter = ocorrencias.get(char, 0)
    erro = ocorrenciaCaracter - ocorrenciaEsperada
    erroNormalizado = erro * erro / ocorrenciaEsperada
    scoreChiQuadrado[char] = erroNormalizado

  scoreTotal = 0
  for charScore in scoreChiQuadrado.values():
    scoreTotal += charScore

  return scoreTotal

# Calcula o offset para as ocorrencias
def OcorrenciasOffset(ocorrenciasCaracter, offset):
  ocorrenciasOffset = {}
  for char, ocorrencia in ocorrenciasCaracter.items():
    char_i = dicionario.find(char)
    offset_char = dicionario[(char_i - offset) % len(dicionario)]
    ocorrenciasOffset[offset_char] = ocorrencia
  return ocorrenciasOffset

# Chutes da chave
def AdivinhaChave(mensagem, grupos, tamanhoChave, expected_char_dist):
  caracteresChave = []

  # Itera pelos grupos selecionados
  for i, grupo in grupos.items():
    ocorrenciasCaracteres = OcorrenciasLetras(grupo)

    # Calcula o score Chi quadrado para o grupo
    chances = []
    for offset in range(len(dicionario)):
      ocorrenciasOffset = OcorrenciasOffset(ocorrenciasCaracteres, offset)
      score = ChiQuadrado(ocorrenciasOffset, len(mensagem), expected_char_dist)
      chances.append((dicionario[offset], score))

    # Seleciona o melhor score
    chances.sort(key=lambda x:x[1])
    caracteresChave.append(chances[0][0])
  
  keyGuess = "".join(caracteresChave)
  return keyGuess