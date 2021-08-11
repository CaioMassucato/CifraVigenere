#!/usr/bin/python3
# -*- coding: utf-8 -*

from CifraVigenere import cifracao, decifracao
from Utils import Agrupa, SequenciasRepetidas, FrequenciaLetras
from functools import reduce

def main():
    modo = input(" 1 -cifrar | 2 - decifrar: ")
    print()
    if modo == '1':
        cifracao()
    else:
        possuiChave = input("Já possui a chave? 1 - Sim | 2 - Não: ")
        print()
        mensagem = decifracao(possuiChave)
        if possuiChave == "2":
            fatoresOcorrencias = SequenciasRepetidas(mensagem)
            grupos = Agrupa(mensagem, 0, fatoresOcorrencias)
            for valor, grupo in grupos.items():
                FrequenciaLetras(grupo)

main()