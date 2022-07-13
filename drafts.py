palavra = "texto"
quantidade_erros = 0
quantidade_letras = len(palavra)

palavra_oculta = " _ " * quantidade_letras

palavra_oculta = list(palavra_oculta)
palavra = list(palavra)

letra_digitada = 'e'

if letra_digitada in palavra:
    for letra in palavra:
        if str(letra_digitada) == letra:
            posicao = palavra_oculta.index(letra)
            palavra_oculta[posicao] = letra


else:
    quantidade_erros += 1

print(type(palavra_oculta))

# for i in palavra:
#     print(i)
