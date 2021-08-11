#!/usr/bin/python3
# -*- coding: utf-8 -*-

from CifraVigenere import cifracao, decifracao
from Utils import Agrupa, SequenciasRepetidas, OcorrenciasLetras, CalculaCI, AdivinhaChave
from functools import reduce
from Constantes import frequenciasIngles, frequenciasPortugues

def main():
    modo = input(" 1 -cifrar | 2 - decifrar: ")
    print()
    if modo == '1':
        tipoEntrada = input("Deseja utilizar o texto padrão (1) ou entrar com um texto (2) ?")
        cifracao(tipoEntrada)
    else:
        possuiChave = input("Já possui a chave? 1 - Sim | 2 - Não: ")
        print()
        mensagem = decifracao(possuiChave)
        if possuiChave == "2":
            fatoresOcorrencias = SequenciasRepetidas(mensagem)
            grupos, tamanhoChave = Agrupa(mensagem, 0, fatoresOcorrencias)
            adivinhacao = AdivinhaChave(mensagem, grupos, tamanhoChave, frequenciasIngles)
            print(adivinhacao)
            # for valor, grupo in grupos.items():
            #     # iC = CalculaCI(frequencias, tamanhoChave)
            #     # print(iC)

main()