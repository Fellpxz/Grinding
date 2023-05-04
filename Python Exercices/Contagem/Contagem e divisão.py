#DIFICIL

def soma_divisores(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    return soma

# Solicitação dos limites do intervalo
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))


# Exibição dos pares de números amigos do intervalo
for i in range(inicio, fim+1):
    for j in range(i+1, fim+1):
        if soma_divisores(i) == j and soma_divisores(j) == i:
            print(i, j, "são amigos.")

