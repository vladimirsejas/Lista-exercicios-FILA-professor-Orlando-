# 1. Lista inicial de 10 números
numeros = [1, 5, 8, 12, 3, 10, 7, 2, 11, 4]

# 2. Cria as duas listas vazias para guardar os resultados
pares = []
impares = []

# 3. Laço que percorre cada número da lista 'numeros'
for numero in numeros:
    # O operador '%' (módulo) calcula o RESTO da divisão.
    # Se o RESTO for 0, o número é PAR.
    if numero % 2 == 0:
        pares.append(numero)  # Adiciona à lista 'pares'
    else:
        impares.append(numero)  # Adiciona à lista 'impares'

# 4. Imprime os resultados
print(f"Lista Original: {numeros}")
print(f"Números Pares: {pares}")
print(f"Números Ímpares: {impares}")