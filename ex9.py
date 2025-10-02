# Lista dos preços originais dos produtos
precos_originais = [15.50, 29.90, 100.00, 5.25, 45.75]

# Taxa de desconto (10% = 0.10)
DESCONTO = 0.10

# Variável para armazenar o total final (começa em zero)
total_com_desconto = 0

print("--- Cálculo do Desconto ---")

# Loop que percorre cada preço na lista
for preco in precos_originais:
    
    # 1. Calcula o valor do desconto (10% do preço)
    valor_do_desconto = preco * DESCONTO
    
    # 2. Calcula o preço do item com desconto
    preco_com_desconto = preco - valor_do_desconto
    
    # 3. Adiciona o preço com desconto ao total geral
    total_com_desconto = total_com_desconto + preco_com_desconto 
    
    # Exibir o cálculo de cada item (opcional, mas bom para aprendizado)
    print(f"Item de R$ {preco:.2f}: Novo preço com desconto de R$ {preco_com_desconto:.2f}")

# Exibe o resultado final
print("\n--------------------------")
print(f"O valor total da compra com 10% de desconto é: R$ {total_com_desconto:.2f}")