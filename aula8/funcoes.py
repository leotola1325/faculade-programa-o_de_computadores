#1 - exercicio
def calculo(kmi, kmf, litros, precolitro):
    distancia = kmf-kmi
    consumo = distancia / litros
    gasto = litros*precolitro
    print(f'''  =========== valores  ==========
          distancia = {distancia}
          consumo Medio = {consumo:.2f}km\L
          gasto = {gasto:.2f}
          ''')

#2 - exercicio
def area(lado1, lado2):
    area = lado1*lado2
    return area

#3 - exercicio
def valor_parcela(valorCompra, quantiParcelas):
    valor_parcela_semjuros = valorCompra/quantiParcelas
    valor_parcela = (valor_parcela_semjuros*0.05)+valor_parcela_semjuros
    return valor_parcela


#4 - exercicio
# 4- Elabore um programa para calcular a velocidade de três objetos diferentes (com
# velocidade constante).
# Conhecemos (são dados digitados pelo usuário), para cada objeto, a distância percorrida
# e o tempo que necessitou para percorrer essa distância.
# Utilize um método geral que calcule e retorne a velocidade de um objeto, fornecidos
# como parâmetros os dados de distância e tempo.
