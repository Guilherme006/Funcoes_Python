# Escreva uma função chamada "inverter" que receba uma string como parâmetro e 
# imprime a string invertida.

def inverter(texto):
    return texto[::-1]


texto = input("Digite algo aqui: ")


print(inverter(texto))
