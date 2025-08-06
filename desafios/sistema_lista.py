def adicionar_ao_carrinho(lista_de_produtos):
    carrinho = []
    total = 0.0

    for produto in lista_de_produtos:
        nome = produto["nome"]
        preco = produto["preco"]

        carrinho.append(produto)
        total += preco

    # Exibir produtos no carrinho
    print("Produtos adicionados ao carrinho:")
    for item in carrinho:
        print(f"- {item['nome']}: R$ {item['preco']:.2f}")

    print(f"\nTotal da compra: R$ {total:.2f}")

# Exemplo de entrada: lista de produtos
produtos = [
    {"nome": "Arroz", "preco": 25.90},
    {"nome": "Feijão", "preco": 8.50},
    {"nome": "Óleo", "preco": 7.30},
    {"nome": "Açúcar", "preco": 4.75}
]

# Executar função
adicionar_ao_carrinho(produtos)