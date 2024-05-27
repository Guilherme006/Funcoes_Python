# Escreva uma função chamada "media" que receba uma lista de números como 
# parâmetro e retorne a média desses números.

def media(notas):
    return sum(notas) / len(notas)


quantidade = int(input("Quantas notas deseja inserir? "))
notas = []

for i in range(quantidade):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)


print(f"A média das notas é: {media(notas)}")

