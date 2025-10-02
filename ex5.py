# 1. Lista inicial de palavras (pode ser qualquer lista de strings)
palavras = ["banana", "uva", "abacaxi", "kiwi", "morango", "manga"]

# 2. Ordena a lista usando o tamanho da palavra (len) como chave (key)
# 'sorted()' cria uma nova lista, sem modificar a original.
palavras_ordenadas = sorted(palavras, key=len)

# 3. Exibe o resultado
print(f"Lista Original: {palavras}")
print(f"Lista Ordenada por Tamanho: {palavras_ordenadas}")