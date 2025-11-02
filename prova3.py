

# Média mínima para aprovação
MEDIA_APROVACAO = 7.0

# Inicializa os contadores
aprovados_count = 0
reprovados_count = 0

# --- 1. Entrada de Dados ---

# Solicita a quantidade de alunos
while True:
    try:
        quantidade_alunos = int(input("Digite a quantidade de alunos na turma: "))
        if quantidade_alunos > 0:
            break
        else:
            print("A quantidade deve ser positiva. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

# Inicializa o contador do loop WHILE
aluno_atual = 1

print("\n" + "="*30)
print(f"Média de aprovação exigida: {MEDIA_APROVACAO}")
print("="*30)


# --- 2. Loop Principal (Usando WHILE) ---
while aluno_atual <= quantidade_alunos:
    print(f"\n--- Aluno {aluno_atual} ---")
    
    # Leitura das notas (simplificada, sem validação de 0 a 10)
    try:
        nota1 = float(input("Digite a 1ª nota: "))
        nota2 = float(input("Digite a 2ª nota: "))
        
        # 3. Calcula a média
        media = (nota1 + nota2) / 2
        
        # 4. Verifica status
        if media >= MEDIA_APROVACAO:
            aprovados_count += 1
            status = "APROVADO(A)"
        else:
            reprovados_count += 1
            status = "REPROVADO(A)"
            
        print(f"Média: {media:.2f}. Status: {status}")
        
        # Incrementa o contador para ir para o próximo aluno
        aluno_atual += 1
        
    except ValueError:
        # Se o usuário digitar algo que não é um número
        print("Erro: Digite apenas números para as notas. Tente novamente para este aluno.")


# --- 5. Resultado Final ---
print("\n" + "===" * 10)
print("RESUMO FINAL DA TURMA")
print("===" * 10)
print(f"Total de alunos: {quantidade_alunos}")
print(f"Alunos APROVADOS: {aprovados_count}")
print(f"Alunos REPROVADOS: {reprovados_count}")
print("=" * 30)