# 1. A lista original de números
numeros = [15, 7, 42, 10, 30, 5, 25]
print("Lista original:", numeros)

# 2. Encontra o maior e o menor valor

# A função max() encontra o maior valor na lista
maior_valor = max(numeros)

# A função min() encontra o menor valor na lista
menor_valor = min(numeros)

# 3. Remove os valores da lista

# O método .remove() retira a *primeira ocorrência* desse valor da lista.
# É importante remover o maior antes do menor, ou vice-versa, separadamente.
numeros.remove(maior_valor)
numeros.remove(menor_valor)

# 4. Exibe a lista resultante
print("\nMaior valor removido:", maior_valor)
print("Menor valor removido:", menor_valor)
print("\nLista resultante (sem o maior e o menor):", numeros)