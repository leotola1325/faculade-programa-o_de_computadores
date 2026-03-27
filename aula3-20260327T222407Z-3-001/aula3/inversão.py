

# Exercícios
# 1- Faça um programa em Python que calcule e mostre o valor do volume do tronco de
# uma pirâmide, para isso o programa deve solicitar ao usuário os valores da altura do
# tronco da pirâmide (h), o valor da base menor (Bmenor) e o da base maior (Bmaior) e
# calcular a seguinte expressão:
# volume =h/3*(Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)
print("============= calcule o volume do tronco de uma piramide  ==========")
h = float(input("digite o valor da altura do tronco de uma piramide:  "))
bmenor = float(input("digite o valor da base menor:  "))
bmaior = float(input("digite o valor da base maior:  "))

volume = h/3*(bmaior**2 + bmenor**2 +(bmaior**2 * bmenor**2)**0.5)

print(f"o volume do tronco de uma piramide e igual a: {volume:.0f}")


# 2- Crie um programa em Python que solicite o valor em horas para o usuário, calcule e
# mostre o valor em minutos, sabendo que 1 hora tem 60 minutos.

print(" =========== conversão de horas para minutos ==============")
horas = int(input("digite um valor em horas para converter em minutos: "))
min = horas * 60
print(f" {horas} horas = {min} minutos")


# 3- Crie um programa em Python que solicite ao usuário a sua idade expressa em anos,
# meses e dias (variáveis separadas). Calcule e mostre a idade expressa apenas em dias.
# Para isso considere 1 ano = 365 dias, 1 mês = 30 dias.
print("========= conversao de idade em dias ===============")
anos = int(input(" digite quantos anos voce tem: "))
messes = int(input("digite quantos messes : "))
dias = int(input("digite quantos dias: "))

con_anos = anos*365
con_messes = messes*30

total = con_anos + con_messes + dias

print(f''' ========== result  =============== 
        voce tem:
       anos = {anos} = {con_anos} dias
       messes = {messes} = {con_messes} dias
       dias = {dias}
       convertendo tudo em dias e igual a = {total} Dias
''')

# 4- Escreva um programa em Python para calcular o valor de uma prestação em atraso
# (prestacao). Para isso, obtenha o valor da prestação (valorPrestacao), a porcentagem de
# multa pelo atraso (multa) e a quantidade de dias de atraso (qtdeDias). Calcular e mostrar o
# valor da prestação atualizado, sabendo que:
# prestacao=valorPrestacao+(valorPrestacao*(multa/100)*qtdeDias)

print("============  valor de prestação em atraso  ===========")
prestação = float(input("digite o valor da prestação: "))
multa = int(input("digite o valor da porcentaem de multa: "))
dias_atraso = int(input("digite o valor de dias de atraso: "))
atual_prestação = prestação + (prestação*(multa/100)*dias_atraso)

print(f"o valor da atual prestação com a multa e igual a:  {atual_prestação} ")
# 5- Faça uma programa em Python que peça do usuário um valor em graus para um
# ângulo. Converta-o para radianos e, usando funções da biblioteca math, imprima o seno,
# cosseno e tangente deste ângulo.
