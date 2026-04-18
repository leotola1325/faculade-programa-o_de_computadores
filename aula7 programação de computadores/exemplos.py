from random import*
num = randint(0,1000)
i = 0
controle =  0 
while controle == 0:
    i += 1
    x = int(input("digite um numero inteiro: "))
    if num == x:
        print(f"Parabens voce acertou o numero  em {i} tentativas")
        controle = 1
    elif num > x :
        print("o numero pensado e maior")
    else:
        print("o numero pensado e menor")






