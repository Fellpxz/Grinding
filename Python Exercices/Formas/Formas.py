#FORMAS
#Pedido do N
n = int(input("Digite um número natural: "))


#Triangulo COMPLETO
for i in range(1, n+1):
    linha = "*" * (2*i - 1)
    print(linha.center(2*n - 1))


#Triangulo OCO
for i in range(1, n+1):
    if i == 1 or i == n:
        linha = "*" * (2*i - 1)
        print(linha.center(2*n - 1))
    elif i == 2:
        middle = "*" + " " * (i - 1) + "*"
        print(middle.center(2*n - 1))
    else:
        espacos = " " * (i - 2)
        final = "*" + espacos + " " + espacos + "*"
        print(final.center(2*n - 1))

#Quadrado OCO
for i in range(1, n + 1):
        if i == 1 or i == n:
            print("*" * n)
        else:
            print("*" + " " * (n-2) + "*")    


#Quadrado COMPLETO
for i in range(1, n + 1):
    print("*" * n)


#ZigZag
for i in range(n):
    if i % 2 == 0:
        print("O")
    else:
        print(" O")

#LOSANGO (FUNCIONAR APENAS COM IMPAR)
for i in range(1, n + 1, 2):
    superior = "O" * i
    print(superior.center(n))

for i in range(n-2, 0, -2):
    inferior = "O" * i
    print(inferior.center(n))