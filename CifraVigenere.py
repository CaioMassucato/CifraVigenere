#!/usr/bin/python3
# -*- coding: utf-8 -*-

dicionario = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

tamanho_dicionario = len(dicionario)

caracteres_ignorados = r".,-;:()'{}[]/\?!0123456789_=+*@#$%¨&<>~´`"

exemplo_ingles = "This template allows for the presentation of text in a language other than English alongside an English translation of that text. \
                    It is primarily designed for rendering poetic texts and their translations in parallel columns that are responsive to devices with display sizes smaller than a personal computer's screen. \
                    That is, on a large screen the text and translation are displayed side-by-side, reducing unsightly white space, but on a smaller screen they are presented one below the other.  \
                    This template has three parameters. The first two are the original text and translation. The third is reserved for an optional citation of the passage: \
                    Text and translation| (text or translation) | (text or translation) | citation information "

def cifracao():
    mensagem = ""
    chave_cifracao = ""
    mensagem_cifrada = ""

    # Input da mensagem
    #mensagem = input("Mensagem a ser cifrada: ").upper()
    mensagem = exemplo_ingles.rstrip("\n").upper()
    for caracter in mensagem:
        if caracter in caracteres_ignorados:
            mensagem.replace(caracter, "")
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

    print(mensagem)
    for caracter in mensagem:
        if  caracter in dicionario:
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
        elif caracter == " ":
            mensagem_cifrada += " "
            
    print("---------------- Mensagem Cifrada ---------------- ")
    print()
    print(mensagem_cifrada)
    print()
    return(mensagem_cifrada)


def decifracao():
    mensagem = ""
    chave_decifracao = ""
    mensagem_decifrada = ""

    # Input da mensagem
    mensagem = input("Mensagem a ser decifrada: ").upper()
    for caracter in mensagem:
        if caracter in caracteres_ignorados:
            mensagem.replace(caracter, "")
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
        elif caracter == " ":
            mensagem_decifrada += " "

    print("---------------- Mensagem Decifrada ---------------- ")
    print()
    print(mensagem_decifrada)
    print()
    return(mensagem_decifrada)