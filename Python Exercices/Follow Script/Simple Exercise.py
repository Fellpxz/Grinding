while True:
    try:
        c = float(input("Digite o valor em Celcius: "))
    except ValueError:
        print("Não foi possível prosseguir com a aplicação. Certifique-se de que o valor inserido seja um número." )
        continue

    fahrenheit = ((c * 1.8) + 32)
    print("O valor em graus fahrenheit: ", fahrenheit,"°" )


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