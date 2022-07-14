palavra = "banana"
palavra_oculta = "_" * len(palavra)
letra_digitada = 'a'

palavra = list(palavra)
palavra_oculta = list(palavra_oculta)


print(palavra_oculta)


for indice, letra in enumerate(palavra):
    if letra == letra_digitada:
        palavra_oculta[indice] = letra
    else:
        print("Letra não está")

print(palavra_oculta)
