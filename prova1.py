alunos = (
    {"nome": "Ana", "notas": [8, 7, 9]},
    {"nome": "Bruno", "notas": [5, 6, 7]},
    {"nome": "Carla", "notas": [9, 9, 10]},
    {"nome": "Diego", "notas": [6, 5, 6]},
    {"nome": "Elisa", "notas": [7, 8, 7]},
    {"nome": "Felipe", "notas": [10, 9, 10]},
    {"nome": "Gustavo", "notas": [4, 6, 5]},
    {"nome": "Helena", "notas": [8, 9, 8]},
    {"nome": "Igor", "notas": [7, 7, 6]},
    {"nome": "Julia", "notas": [9, 8, 9]},
)

# Inicializa as variáveis para armazenar o aluno com a maior média
melhor_aluno = None
maior_media = -1 # Começa com um valor bem baixo para garantir que a primeira média seja maior

# 1. Percorre a lista de alunos
for aluno in alunos:
    # 2. Calcula a média do aluno atual
    notas = aluno["notas"]
    media_atual = sum(notas) / len(notas)

    # 3. Verifica se a média atual é maior que a maior média encontrada até agora
    if media_atual > maior_media:
        maior_media = media_atual
        melhor_aluno = aluno

# --- Exibe o Resultado ---

if melhor_aluno:
    # Formata a média com duas casas decimais
    maior_media_formatada = f"{maior_media:.2f}"

    print("--- Resultado ---")
    print(f"O aluno com a maior média é: {melhor_aluno['nome']}")
    print(f"Suas notas foram: {melhor_aluno['notas']}")
    print(f"A maior média é: {maior_media_formatada}")
else:
    print("A lista de alunos está vazia.")