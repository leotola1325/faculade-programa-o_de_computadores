#  ==============   meu codigo    =======================
# num1 = int(input("digite um numero: "))
# num2 = int(input("digite um numero: "))
# somar = num1 + num2
# print(f' a soma de {num1} + {num2} é igual a = {somar}')

#  ================ codigo do github copilot ================== exemplo 1
# def somar(a, b):
#     return a + b

# # Example usage:
# num1 = int(input("Digite um número: "))
# num2 = int(input("Digite outro número: "))
# resultado = somar(num1, num2)
# print(f"O resultado da soma é: {resultado}")

#  =========== exemplo 2  ==========================
# Imprime números pares de 0 a 10     ---------   No Python, a função range(start, stop, step) gera uma sequência de números que inclui o valor inicial (start), mas exclui o valor final (stop).
# for num in range(0, 11, 2):
#     print(num)


# =========== exemplo 3 ==================
# Solicita um número ao usuário e calcula o fatorial
# num = int(input("Digite um número para calcular o fatorial: "))
# fatorial = 1

# for i in range(1, num + 1):
#     fatorial *= i

# print(f"O fatorial de {num} é {fatorial}")


#    ===================== exemplo 4 ======================
# def media(lista):
#     return sum(lista)/len(lista)
# aponte os erros que esse programa pode gerar e explique cada um o proque e como arrumar


#  ============================ exemplo 6  ================================
# a = 0 
# for i in range(10):
#     a += i 
# print(i,a)


# b = sum(range(10))
# print(b)

#  =============================  exemplo 7  ================================
lista  = int(input("digite uma lista de numeros numero em sequencia separados por virgula: "))
def numeros_impares(lista):
    return [x for x in lista if x % 2 != 0]
print(numeros_impares(lista))
# IA: 
