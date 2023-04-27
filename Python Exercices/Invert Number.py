def inverte_numero(numero):
    
    # converte o número para uma string e inverte a ordem dos caracteres
    numero_invertido = str(numero)[::-1]
    # converte a string de volta para um número
    numero_invertido = int(numero_invertido)
    return numero_invertido

numero = int(input("Digite um número natural: "))
numero_invertido = inverte_numero(numero)
print("O número invertido é:", numero_invertido)