import math
#1 - desenvolva um programa  em python que solicite  os valores dos lados de um retangulo e calcule e mostre seu perimetro  e sua area 
print(f''' 
               valor 1
    ----------------------------
    |                          | valor 2
    |                          |
    |                          |
    ----------------------------
    
      ''')
lado1 = float(input("digite a medida do lado 1: "))
lado2 = float(input("digite a medida do lado 2: "))
perimetro =  (lado1*2)+ (lado2*2)
area = lado2*lado1
print(f''' ================    resultado ================
      perimetro = {perimetro}
      area = {area}
      ''')

#2 - escreva um programa em python que solicite ao usuario o salario atual e mostre o salario acrescido de 5% de comissao

print(" =============== salario ==============")
salario = float(input("digite seu salario : "))
aumento =  salario * 0.05                                                       # converter porcentagem
total = salario + aumento

print(f"seu salario total com o acrescimo de 5% é :  {total}")



#3 - escreva um programa  que peca ao usuario a distancia entre duas cidades e o tempo de viagem. o programa devera calcular e exibir  a velocidade 
# media de um carro que vai de uma cidade para outra utilize  a formula          vm =  distancia  / tempo 


print(" ==============  velocidade  ===============")
distancia = float(input("digite a distancia entre as duas cidades em kilometros:  "))
tempo = float(input("digite o tempo de viagem entre as duas cidades em minutos:     "))
tempo_horas = tempo/60
velocidade = distancia / tempo_horas
print(f"a velocidade media e : {velocidade:.0f}km/h")

#4 protgrama que calcule  as duas raizes uma equação de 2 grau 

print("===================  equação de 2 grau  ================")

A = int(input("digite o valor de A =  "))
B = int(input("digite o valor de B =  "))
C = int(input("digite o valor de C =  "))

#b ao quadrado -4.a.c
quadrado = B**B
delta = quadrado(-4*A*C)
raiz_delta = math.sqrt(delta)

x1 = (-B + raiz_delta) / (2*A)
x2 = (-B - raiz_delta) / (2*A)

print(f''' ========= resultado =========
      delta = {delta}
      raiz de delta = {raiz_delta}
      x1 = {x1}
      x2 = {x2}
      
      ''')
