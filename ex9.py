preco_original = float(input("Digite o preco do produto: "))
percentual_desconto = int(input("Digite o percentual do desconto: "))

valor_desconto = preco_original * (percentual_desconto / 100)

novo_valor = preco_original - valor_desconto

print("valor com desconto e", novo_valor)

preco_original = float(input("Digite o preco do produto: "))
percentual_aumento = int(input("Digite o percentual do desconto: "))

valor_aumento = preco_original * (percentual_aumento / 100)

novo_valor = preco_original + valor_aumento

print("valor com aumento", novo_valor)
