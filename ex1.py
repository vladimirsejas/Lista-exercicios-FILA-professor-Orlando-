# 1. Lista para guardar os 10 números digitados
numeros = []

print("--- INÍCIO DO PROGRAMA ---")
print("Por favor, digite 10 números inteiros:")

# Loop para ler os 10 números
for i in range(10):
    entrada = input(f"Digite o {i+1}º número: ")
    numero = int(entrada)
      # Adiciona o número à lista 'numeros'

# 2. Listas auxiliares para encontrar os duplicados
numeros_vistos = []
duplicados = []

# 3. Processamento: Verificando cada número da lista
for num in numeros:
    if num in numeros_vistos:
        if num not in duplicados:
            duplicados.append(num)
    else:
        numeros_vistos.append(num)

# 4. Exibição do resultado
print("\n--- RESULTADO ---")
print(f"A lista completa digitada foi: {numeros}")
# ... (restante do código de exibição)