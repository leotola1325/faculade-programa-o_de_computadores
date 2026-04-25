# Exercícios de fixação
# 1- Faça um método que receba como parâmetros o Km inicial, Km final, quantidade de
# litros gastos e preço do litro. Calcule e mostre:
# - Distância percorrida;
# - Consumo médio;
# - Valor gasto;
# Faça um programa principal que solicite para o usuário o valor da quilometragem inicial,
# final, a quantidade de litros gastos e o preço do litro e mostre a distância percorrida, o
# consumo médio e o valor gasto, para isso utilize o método definido acima.

import funcoes
kmi = float(input('digite o valor de kilometro inicial: '))
kmf = float(input('digite o valor de kilometro final: '))
litros = float(input('digite o valor de litros gastos : '))
precolitro = float(input('digite o valor do preço por litro: '))
funcoes.calculo(kmi, kmf, litros, precolitro)




# 2- Escreva um método com retorno que receba como parâmetros os lados de um
# retângulo, calcula e retorna o valor de sua área.
# area = lado*lado
# Faça um programa principal que solicite os valores dos lados de um retângulo ao usuário,
# e utilizando a função definida acima, calcule e mostre o valor de área.



print('''
            lado1
      =======================
      |                     |   lado2
      |                     |
      =======================
''')
lado1 = int(input("digite o valor da lado1: "))
lado2 = int(input("digite o valor do lado2: "))
print(f"o valor da area do retangulo é: {funcoes.area(lado1,lado2)} metros quadrados")


# 3- Construir um método que receba como parâmetros o valor de uma compra e a
# quantidade de parcelas e calcula e retorna o valor da parcela, sabendo que a loja
# acrescenta 5% de juros para as compras parceladas.
# No algoritmo principal, solicite para o usuário o valor de uma compra e a quantidade de
# parcelas e utilizando o método descrito acima, mostre o valor da parcela.
# Exercícios de fixação
# Exercícios de fixação

valorCompra = float(input("digite o valor da compra: "))
quantiParcelas = float(input("digite a quantidades de parcelas: "))
print(f''' ======== resultado ========
      valor = {valorCompra}
      parecelas = {quantiParcelas}x
      valor das parcelas com juros = {funcoes.valor_parcela(valorCompra,quantiParcelas)}
''')






# 4- Elabore um programa para calcular a velocidade de três objetos diferentes (com
# velocidade constante).
# Conhecemos (são dados digitados pelo usuário), para cada objeto, a distância percorrida
# e o tempo que necessitou para percorrer essa distância.
# Utilize um método geral que calcule e retorne a velocidade de um objeto, fornecidos
# como parâmetros os dados de distância e tempo.