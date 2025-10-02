numeros = [10, 3, 5, 8, 20, 7, 1]
soma_indices_pares = 0

# Usamos range(len(numeros)) para gerar a sequência de índices: 0, 1, 2, 3, 4, 5, 6
for i in range(len(numeros)):
    
    # 1. Checa se o índice (i) é par
    if i % 2 == 0:
        
        # 2. Acessa o valor da lista usando o índice: numeros[i]
        valor = numeros[i]
        
        # 3. Soma o valor
        soma_indices_pares += valor

print(f"A soma dos valores nos índices pares é: {soma_indices_pares}")