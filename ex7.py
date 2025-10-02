# 1. Solicita a frase ao usuário (no seu caso, 'muita coisa')
frase = input("Digite a frase: ")

# 2. Converte a frase para minúsculas
frase_minuscula = frase.lower()


# 4. Divide a frase em uma lista de palavras
lista_de_palavras = frase_minuscula.split()

# 5. Usa um 'set' para remover palavras repetidas (palavras distintas)
palavras_distintas_set = set(lista_de_palavras)

# 6. Converte o 'set' de volta para uma lista
palavras_distintas_lista = list(palavras_distintas_set)

# 7. Imprime a lista final
print("\nLista de palavras distintas (sem repetição):")
print(palavras_distintas_lista)