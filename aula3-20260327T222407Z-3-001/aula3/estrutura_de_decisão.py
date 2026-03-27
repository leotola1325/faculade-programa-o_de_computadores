#1 escreva um algoritmo que solicite um numero ao usuario caso seja digitado um valor entre 0 e 9 "valor correto", caso contrario mostre "valoor incorreto "
print(' ================= valor correto ======================= ')
num =  int(input("digite um numero: "))
if num >=0 and num <=9 :
    print("valor correto")
else:
    print("valor incorreto ")

# 2#
# Crie um algoritmo que solicite ao usuário o seu turno de trabalho e a quantidade de
# horas trabalhadas, calcule e mostre o valor do salário. Considere os valores de horas a
# seguir, de acordo com o turno de trabalho. Caso o turno seja igual a ‘N’ (utilize um
# caractere para representar) o valor da hora trabalhada é R$ 45,00, caso contrário é R$
# 37,50

print('============== salario  ================')
turno = input("digite o seu turno de trabalho noturno(N) outro horario(qualquer letra): ")
horas = int(input("digite quantas horas voce trabalha: "))

if turno == 'N' :
    salario_not= horas * 45
    print(f"seu salario e: {salario_not}")
else:
    salario_mat = horas * 37.5
    print(f"seu salario e: {salario_mat}")


# 3- Faça um programa em Python que obtenha o valor de uma compra, calcular e mostrar
# o valor da compra considerando o desconto, conforme descrito abaixo:
# para compras acima de R$ 200 a loja dá um desconto de 20%
# para as abaixo disso não tem desconto, mostre o valor da compra.

print(' ================ valor de compra  ==============')
print(" para compras acima de R$ 200 a loja dá um desconto de 20%")
compra =  float(input("digite o valor da compra: "))
if compra >= 200:
    desconto = compra - (compra*0.20)
    print(f"o valor da compra com desconto de 20% e igual a: {desconto}")
else:
    print(f"valor da compra: {compra}")

#4
#  Escreva um programa em Python que solicite ao usuário os valores de três contas de
# consumo (p.ex. água, luz e telefone) e o valor de seu salário. Verifique se o salário é
# suficiente para pagar as três contas, caso não seja apresente a mensagem “Salário
# insuficiente!”. Caso seja, apresente o valor que restou do salário após pagar as contas.
print('========  pagar as contas  ===========')
agua = float(input("digite o valor da conta de agua desse mes: "))
luz = float(input("digite o valor da conta de luz desse mes: "))
telefone = float(input("digite o valor da conta de telefone desse mes: "))
sala = float(input("digite o seu salario: "))

soma = agua + luz + telefone
if sala >=soma:
    sobra = sala-soma
    print(f"o total das contas foi: {soma:.2f} e apos o pagamento sobrou: {sobra:.2f}")
else:
    print("salario insuficiente")