# Escreva uma função chamada "maior" que receba três números como parâmetros e 
# retorne o maior entre eles.

def maior(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


numero_01 = int(input("Digite o primeiro número: "))
numero_02 = int(input("Digite o segundo número: "))
numero_03 = int(input("Digite o terceiro número: "))


print(maior(numero_01, numero_02, numero_03))
