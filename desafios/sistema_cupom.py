descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "DESCONTO30": 0.30,
}
preços = float(input("Informe o preço do produto: R$ ").strip())
desconto = input("Informe o código do desconto: ").strip().upper()

if desconto in descontos:
    preco_final = preços - (preços * descontos[desconto])
    print(f"Preço final com desconto: R$ {preco_final:.2f}")
else:
    print("Código de desconto inválido.") 