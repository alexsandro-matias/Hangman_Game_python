import os
import platform
import random

board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


def sorteio_palavra():
    with open("words.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


def limpando_tela():
    sistema = descobrindo_sistema_operacional()
    if sistema == "Windows":
        os.system("cls")
    elif sistema == "Linux":
        os.system("clear")
    else:
        print("Sistema Operacional não identificado")


def descobrindo_sistema_operacional():
    return platform.system()


quantidade_erros = 0
palavra = sorteio_palavra()
quantidade_letras = len(palavra)
maximo_erros = len(board)
palavra_oculta = "_" * quantidade_letras
letras_erradas = []
letras_corretas = []

# Já que as strings são imutáveis,
# se faz necessária a conversão das palavras para lista
palavra = list(palavra)
palavra_oculta = list(palavra_oculta)


def hide_word():
    print("Palavra:", palavra_oculta)


def perdeu_jogo():
    print('\nGame over! Você perdeu.')
    print('A palavra era', str("".join(palavra)).upper())


def ganhou_jogo():
    print('\nParabens por ter acertado.', str("".join(palavra)).upper())


while True:
    print(board[quantidade_erros])
    hide_word()
    print("Letras erradas: ", letras_erradas)
    print("Letras corretas: ", letras_corretas)
    letra_digitada = input("Digite uma letra: ")

    if letra_digitada in palavra:
        letras_corretas.append(letra_digitada)

        for indice, letra in enumerate(palavra):
            if letra == letra_digitada:
                palavra_oculta[indice] = letra

        if palavra == palavra_oculta:
            ganhou_jogo()
            break

    else:
        letras_erradas.append(letra_digitada)
        quantidade_erros = quantidade_erros + 1
        if quantidade_erros == maximo_erros:
            perdeu_jogo()
            break
    limpando_tela()

print('Foi bom jogar com você! Agora vá estudar!\n')
