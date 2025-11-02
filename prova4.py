# Lista de meses por extenso
# O primeiro elemento (índice 0) é vazio para que o mês 1 corresponda ao índice 1 (Janeiro)
meses_por_extenso = [
    "", 
    "janeiro", 
    "fevereiro", 
    "março", 
    "abril", 
    "maio", 
    "junho", 
    "julho", 
    "agosto", 
    "setembro", 
    "outubro", 
    "novembro", 
    "dezembro"
]

# --- 1. Entrada de Dados Simples (Sem tratamento de erro) ---

print("Por favor, digite os números da data:")
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

# --- 2. Processamento ---

# Acessa o nome do mês na lista usando o número digitado como índice
# Ex: se o usuário digitar 4, ele pega o item na posição 4 ("abril")
nome_do_mes = meses_por_extenso[mes]

# --- 3. Saída ---

# Monta a string no formato 'dia de mês de ano' usando f-strings
data_formatada = f"{dia} de {nome_do_mes} de {ano}"

print("\n--- Saída ---")
print(data_formatada)

