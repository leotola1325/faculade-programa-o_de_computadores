# 1- Faça um programa em Python que escreva a mensagem
# “ Engenharia de software - Unicsul” na tela.
print(" ================ exercicio 1  ==================")
print("Engenharia de software- Unicsul ")


# 2- Faça um programa em Python que solicite ao usuário a
# sua profissão e mostre na tela a informação digitada.
print(" ================ exercicio 2  ==================")
profissao = input("digite sua profissão: ")
print(f"sua profissão é:  {profissao}")


# 3- Faça um programa em Python que solicite ao usuário a
# sua idade e apresente a informação na tela.
print(" ================ exercicio 3  ==================")                                                 #    ---------> todos exercicios do 1 ao 5
idade = int(input("digite sua idade: "))                                                                      # - topicos importes 
print(f"você tem : {idade} anos")                                                                             # - declaração de variavel,  print, int, input.

# 4- Faça um programa em Python que solicite o último
# sobrenome do usuário e mostre na tela a mensagem:
# “Família” e na sequência o sobrenome digitado.
print(" ================ exercicio 4  ==================")
sobrenome = input("digite seu sobrenome: ")
print(f"prazer menbro da familia {sobrenome}")


# 5- Faça um programa em Python que solicite o esporte
# favorito de uma pessoa e apresente-o na tela.
print(" ================ exercicio 5  ==================")
nome = input("digite seu nome: ")
esporte = input("digite seu esporte favorito:  ")

print(f"prazer {nome} pelo que voce falou seu esporte favorito é {esporte}")



# 6-  todas informações pessoais
print(f'''
      
 ========  informações pessoais  ============
        
nome: {nome} {sobrenome}
idade: {idade}
curso: Engenharia de software - Unicsul
profissão: {profissao}
esporte favorito: {esporte}
''')
