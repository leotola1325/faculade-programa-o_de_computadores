# 1- Criar um algoritmo que leia a idade de uma pessoa e informe sua classe eleitoral:
# • não-eleitor (abaixo de 16 anos)
# • eleitor obrigatório (entre 18 e 65 anos)
# • eleitor facultativo (entre 16 e 18 anos e maior de 65 anos)
print('===========  Classe Eleitoral  ============')
idade = int(input('digite a sua idade: '))

if idade >= 16 and idade < 18 or idade > 65:
    print(f"sua idade e {idade} e sua classe é: eleitor facultativo('voce pode votar mais nao e obrigatorio')")
elif idade >=18 and idade <= 65: 
    print(f'sua idade e {idade} e sua classe é: eleitor obrigatorio')
else:
    print(f'sua idade é {idade} e sua classe é: não eleitor')

# 2- Ler três valores inteiros (variáveis a, b e c) e efetuar o cálculo da equação de segundo
# grau, apresentando: as duas raízes, quando for possível efetuar o cálculo (delta positivo ou
# zero); a mensagem "Não há raízes reais", se não for possível fazer o cálculo (delta
# negativo); e a mensagem "Não é equação do segundo grau", se o valor de a for igual a
# zero.

import math

print("===================  equação de 2 grau  ================")

A = int(input("digite o valor de A =  "))
B = int(input("digite o valor de B =  "))
C = int(input("digite o valor de C =  "))

#b ao quadrado -4.a.c

delta = B*B-4*A*C

if delta > 0:
    raiz_delta = math.sqrt(delta)
    x1 = (-B + raiz_delta) / (2*A)
    x2 = (-B - raiz_delta) / (2*A)

    print(f''' ========== resultado =========
      delta = {delta}
      raiz de delta = {raiz_delta}
      x1 = {x1}
      x2 = {x2}
      ''')
elif delta == 0:
    print('Não é equação do segundo grau')
else:
    print('não ha raizes reais')

# 3- Um comerciante calcula o valor da venda, tendo em vista a tabela a seguir:
# Crie uma programa que permita digitar o nome do produto e valor da compra, e
# imprimindo o nome do produto e o valor da venda.
# Valor de compra                    Valor de venda
# valor < R$10,00                    lucro de 70%
# R$ 10,00 <= valor < R$ 30,00       lucro de 50%
# R$ 30,00 <= valor < R$ 50,00       lucro de 40%
# valor >= R$50,00                   lucro de 30%

print('================  tabela de lucro  ==============')
print('''
    bolacha     = R$: 4
    salgado     = R$: 6
    brigadeiro  = R$: 10
    bolo        = R$: 40
    sorvete     = R$: 3
    vinho       = R$: 30
''')
produtos = {
    "bolacha": 4,
    "salgado": 6,
    "brigadeiro": 10,
    "bolo": 40,
    "sorvete": 3,
    "vinho": 30
}

produto = input('digite o nome do produto: ')

if produto in produtos:
   valor = produtos[produto]
else:
   print("produto inexistente")

if valor < 10:
   venda = valor * 1.70
elif valor >= 10 and valor < 30:
   venda = valor * 1.50
elif valor >=30 and valor < 50:
   venda = valor * 1.40
else:
   venda = valor * 1.30

print(f''' ===============   resultado   ===============
      produto = {produto}
      valor do produto = {valor}
      valor de venda = {venda}
''')

# 4- Elabore um programa em Python que implemente uma calculadora com as funções de
# somar, subtrair, multiplicar e dividir. O programa deverá solicitar ao usuário os dois
# valores, e perguntar qual a operação pretendida (‘+’, ‘-‘ , ‘*’ ou ‘/’ ) e a seguir calcular e
# mostrar o resultado.

print("================ calculadora ============")

num1 = float(input("digite o valor 1: "))
num2 = float(input("digite o valor 2 : "))
print("digite a formula que voce deseja calcular(+)(-)(*)(/): ")
formula = input("digite a formula: ")

if formula == '+':
    calculo = num1+num2
elif formula == '-':
    calculo = num1-num2
elif formula == '*':
    calculo = num1*num2
elif formula == '/':
    calculo = num1/num2
else:
    print("erro digite alguma opção")

print(f"o resultado de {num1} {formula} {num2} = {calculo}")
