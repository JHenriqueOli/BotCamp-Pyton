# Lista para armazenar os produtos
carrinho = []
total = 0.0

# Número de produtos
n = int(input())

for _ in range(n):
    linha = input().strip()
    
    # Encontra o primeiro espaço para separar nome e preço
    posicao_espaco = linha.find(' ')
    
    # Separa nome e preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    
    # Adiciona ao carrinho e soma ao total
    carrinho.append((item, preco))
    total += preco

# Exibe os itens no formato correto
for item, preco in carrinho:
    print(f"{item}: R${preco:.2f}")

# Exibe o total com duas casas decimais
print(f"Total: R${total:.2f}")