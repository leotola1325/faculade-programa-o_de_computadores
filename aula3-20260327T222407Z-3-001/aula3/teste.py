#4
#  Escreva um programa em Python que solicite ao usuário os valores de três contas de
# consumo (p.ex. água, luz e telefone) e o valor de seu salário. Verifique se o salário é
# suficiente para pagar as três contas, caso não seja apresente a mensagem “Salário
# insuficiente!”. Caso seja, apresente o valor que restou do salário após pagar as contas.
print('========  pagar as contas  ===========')
agua = float(input("digite o valor da conta desse mes: "))
luz = float(input("digite o valor da conta desse mes: "))
telefone = float(input("digite o valor da conta desse mes: "))
sala = float(input("digite o seu salario: "))

soma = agua + luz + telefone
if sala >=soma:
    sobra = sala-soma
    print(f"o total das contas foi: {soma:.2f} e apos o pagamento sobrou: {sobra:.2f}")
else:
    print("salario insuficiente")