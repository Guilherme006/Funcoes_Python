# Escreva uma função chamada "imprime_diagonal" que recebe uma matriz de tamanho 
# 3x3 preenchida com valores quaisquer, e imprime os valores na diagonal principal.

def imprime_diagonal(matriz):
    print(matriz[0][0])
    print(matriz[1][1])
    print(matriz[2][2])


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


imprime_diagonal(matriz)
