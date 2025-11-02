def elevar_ao_quadrado_simples():
    # 1. Lista original de números (os dados de entrada)
    numeros_originais = [4, 6, 9, 11, 2]
    
    # 2. Lista de resultados (começa vazia, será preenchida)
    quadrados = []
    
    # Exibe a lista original
    print(f"Lista original: {numeros_originais}")

    # 3. Lógica: Percorrer e calcular
    
    # Para cada número ('num') na lista original...
    for num in numeros_originais:
        
        # Calcula o quadrado: num ** 2 significa num multiplicado por ele mesmo
        resultado = num ** 2
        
        # Adiciona o resultado à nossa nova lista usando .append()
        quadrados.append(resultado)

    # 4. Exibição do resultado
    print(f"Lista de quadrados: {quadrados}")

# Executa o programa
elevar_ao_quadrado_simples()