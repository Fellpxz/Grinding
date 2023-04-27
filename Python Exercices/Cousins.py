def  prime(number):
    confimed = True
    for i in range(2, number):
        if number % i == 0:
            confimed = False
            break
    
    if confimed:
        print("O número é primo!")
    else:
        print("O número não é primo!")

prime(11)