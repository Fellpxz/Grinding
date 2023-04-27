#Building a Square!

#Using While in Functions!

import time

# Não tem como você colocar um while dentro de uma função como essa!
def squareBuild(n):
    for i in range(n):
        if i == 0 or i == n-1:
            print("*" * n)
        else:
            print("*" + " " * (n-2) + "*")

        time.sleep(1)

while True:
    try:
        n = int(input("Digite um número natural: "))
        if n < 2:
            print("O valor precisa ser maior ou igual a 2 para prosseguir com a aplicação!")
            continue
    except ValueError:
        print("Valor inválido. Certifique-se de que o valor inserido seja um número.")
        continue

    squareBuild(n)

    while True:
        resposta = input("Deseja usar a aplicação novamente? (S/N)").lower()
        if resposta == 'n':
            break
        elif resposta == 's':
            break
        else:
            print("Opção inválida. Digite 'S' para continuar ou 'N' para sair.")
            continue

    if resposta == 'n':
        break
    else:
        continue