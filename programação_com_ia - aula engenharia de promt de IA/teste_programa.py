# crie um sistema em python que funcione como uma loja  terei
# 10 produtos  com seus respectivos precos e eu irei selecionar
# eles   e no final mostrar a soma dos valores  use o no programa o metodo de dicionario


produtos = {
    "1":  {"nome": "Arroz 5kg",          "preco": 25.90},
    "2":  {"nome": "Feijao 1kg",         "preco": 8.50},
    "3":  {"nome": "Macarrao 500g",      "preco": 4.75},
    "4":  {"nome": "Azeite 500ml",       "preco": 22.00},
    "5":  {"nome": "Leite 1L",           "preco": 5.99},
    "6":  {"nome": "Cafe 500g",          "preco": 15.90},
    "7":  {"nome": "Acucar 1kg",         "preco": 4.49},
    "8":  {"nome": "Manteiga 200g",      "preco": 9.80},
    "9":  {"nome": "Farinha 1kg",        "preco": 6.30},
    "10": {"nome": "Oleo de soja 900ml", "preco": 7.99},
}
carrinho = []
def exibir_produtos():
    linhas = "\n".join(f"  [{cod:>2}] {info['nome']:<25} R$ {info['preco']:.2f}" for cod, info in produtos.items())
    print(f"\n===== PRODUTOS =====\n{linhas}\n====================")
def exibir_carrinho():
    if not carrinho:
        print("\n  Carrinho vazio.")
        return
    itens = "\n".join(f"  - {item['nome']:<25} R$ {item['preco']:.2f}" for item in carrinho)
    total = sum(item["preco"] for item in carrinho)
    print(f"\n===== CARRINHO =====\n{itens}\n--------------------\n  TOTAL: R$ {total:.2f}\n====================")
def adicionar_produto():
    exibir_produtos()
    codigo = input("\nDigite o numero do produto: ").strip()
    if codigo in produtos:
        carrinho.append(produtos[codigo])
        print(f"\n  OK! '{produtos[codigo]['nome']}' adicionado!")
    else:
        print(f"\n  Produto nao encontrado.")
def finalizar_compra():
    if not carrinho:
        print("\n  Carrinho vazio.")
        return
    exibir_carrinho()
    print(f"\n  Obrigado pela compra!")
def menu():
    while True:
        print("\n[1] Ver produtos\n[2] Adicionar\n[3] Ver carrinho\n[4] Finalizar\n[0] Sair")
        opcao = input("Escolha: ").strip()
        if opcao == "1": exibir_produtos()
        elif opcao == "2": adicionar_produto()
        elif opcao == "3": exibir_carrinho()
        elif opcao == "4": finalizar_compra(); break
        elif opcao == "0": print("\n  Ate mais!"); break
        else: print("\n  Opcao invalida.")
menu()