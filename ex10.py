# A matriz (lista de listas) que vamos usar. É uma matriz 3x3.
matriz = [
    [1, 2, 3],  # Linha 0
    [4, 5, 6],  # Linha 1
    [7, 8, 9]   # Linha 2
]

# Variável para guardar a soma dos elementos
soma_diagonal = 0

# 1. Loop para percorrer as linhas (e colunas)
# A função range(len(matriz)) nos dá os números 0, 1 e 2,
# que são os índices (posições) que queremos acessar.
for i in range(len(matriz)):
    
    # 2. Acessa o elemento da diagonal principal
    # Acessamos a posição onde o índice da linha (i) é igual ao da coluna (i).
    elemento = matriz[i][i]
    
    # 3. Adiciona o elemento à soma total
    soma_diagonal = soma_diagonal + elemento
    
    # Opcional: Mostra o que está sendo somado a cada passo
    print(f"Somando o elemento na posição [{i}][{i}]: {elemento}")


# 4. Exibe o resultado final
print("\n-------------------------")
print(f"A soma da diagonal principal é: {soma_diagonal}")