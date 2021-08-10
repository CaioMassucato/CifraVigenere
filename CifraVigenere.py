#!/usr/bin/python3
# -*- coding: utf-8 -*-

def cifracao():
    dicionario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tamanho_dicionario = len(dicionario)
    mensagem = ""
    chave_cifracao = ""
    mensagem_cifrada = ""

    # Input da mensagem
    mensagem = input("Mensagem a ser cifrada: ").upper()
    print()
    tamanho_mensagem = len(mensagem)

    # Input da chave para cifrar
    chave_cifracao = input("Key para cifrar: ").upper()
    for letra in chave_cifracao:
        if letra not in dicionario:
            print("Chave Inválida, tente novamente.")
            return "Chave inválida"
    print()

    # Repetir a chave até chegar no tamanho da mensagem
    chave_expandida = chave_cifracao
    tamanho_chave_expandida = len(chave_expandida)

    while tamanho_chave_expandida < tamanho_mensagem:
        chave_expandida = chave_expandida + chave_cifracao
        tamanho_chave_expandida = len(chave_expandida)

    index_chave = 0

    for caracter in mensagem:
        if caracter in dicionario:
            # Procura o index da letra no dicionário
            index = dicionario.find(caracter)

            # Percorre encontrando os valores dos caracteres das chaves
            caracter_chave = chave_expandida[index_chave]
            index_caracter_chave = dicionario.find(caracter_chave)
            index_chave += 1

            # Calcula o index do caracter cifrado
            index_cifra = index + index_caracter_chave

            # Se o index cifrado ultrapassa o tamanho do dicionário, da a volta
            if index_cifra >= tamanho_dicionario:
                index_cifra -= tamanho_dicionario

            # Encontra caracter cifrado e monta a cifra
            caracter_cifrado = dicionario[index_cifra]
            mensagem_cifrada += caracter_cifrado
    print("Mensagem Cifrada :: ")
    print(mensagem_cifrada)
    print()
    return(mensagem_cifrada)


def decifracao():
    dicionario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tamanho_dicionario = len(dicionario)
    mensagem = ""
    chave_decifracao = ""
    mensagem_decifrada = ""

    # Input da mensagem
    mensagem = input("Mensagem a ser decifrada: ").upper()
    print()
    tamanho_mensagem = len(mensagem)

    # Input da chave para decifrar
    chave_decifracao = input("Key para decifrar: ").upper()
    for letra in chave_decifracao:
        if letra not in dicionario:
            print("Chave Inválida, tente novamente.")
            return "Chave inválida"
    print()

    # Repete a chave até chegar no tamanho da mensagem
    chave_expandida = chave_decifracao
    tamanho_chave_expandida = len(chave_expandida)

    while tamanho_chave_expandida < tamanho_mensagem:
        chave_expandida = chave_expandida + chave_decifracao
        tamanho_chave_expandida = len(chave_expandida)

    index_chave = 0

    for caracter in mensagem:
        if caracter in dicionario:
            # Procura o index da letra no dicionário
            index = dicionario.find(caracter)

            # Percorre encontrando os valores dos caracteres das chaves
            caracter_chave = chave_expandida[index_chave]
            index_caracter_chave = dicionario.find(caracter_chave)
            index_chave += 1

            # Calcula o index do caracter decifrado
            index_decifra = index - index_caracter_chave

            # Se o index cifrado ultrapassa o tamanho do dicionário, da a volta
            if index_decifra >= tamanho_dicionario:
                index_decifra -= tamanho_dicionario

            # Encontra caractere decifrado e monta a mensagem
            caracter_decifrado = dicionario[index_decifra]
            mensagem_decifrada += caracter_decifrado

    print("Mensagem Decifrada :: ")
    print(mensagem_decifrada)
    print()
    return(mensagem_decifrada)