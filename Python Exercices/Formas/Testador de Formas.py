#Building a Square!

#Using While in Functions!

import time

# INICIAR WHILE

while True:
    #VERIFICAÇÃO
    #POSSIBILIDADES DE ERROS
    try:
        #INPUT DA VARIAVEL PRINCIPAL
        n = int(input("Digite um número natural: "))
        #CONDIÇÕES DE FUNCIONAMENTO PARA ESSE CÓDIGO 
        #COMO NÃO TEM EU COMENTEI

        #if n < 2:
            #print("O valor precisa ser maior ou igual a 2 para prosseguir com a aplicação!")
           #continue
    except ValueError:
        print("Valor inválido. Certifique-se de que o valor inserido seja um número.")
        continue

    #CÓDIGO PRINCIPAL   
    for i in range(1, n+1, 2):
        espacos = " " * ((n - i) // 2)
        asteriscos = "*" * i
        linha = espacos + asteriscos + espacos
        print(linha)

    # Metade inferior do losango
    for i in range(n-2, 0, -2):
        espacos = " " * ((n - i) // 2)
        asteriscos = "*" * i
        linha = espacos + asteriscos + espacos
        print(linha)

    #SCRIPT DA REPETIÇÃO DA APLICAÇÂO
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