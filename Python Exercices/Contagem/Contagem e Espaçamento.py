#MÉDIO

x = int(input("Numero 1:" ))
y = int(input("Numero 2:" ))

count = 2
num = x

if num % 2 == 0:
    num = num + 1

while num <= y:
    print (num, end=" ")
    count = count + 2
    num = num + count