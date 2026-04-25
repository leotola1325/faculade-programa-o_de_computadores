def somadevalores(a,b):
    a = a + b
    return a # valor da soma local gravada 

a = int(input('digite o valor de A : '))
b = int(input('digite o valor de B : '))
print(somadevalores(a,b))                          #'parametros por valor' e nao por referencia armezena local
print(a) #nao altera valor de 'A' pois a soma e somente da função la armazenado
