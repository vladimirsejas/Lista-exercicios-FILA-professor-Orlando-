def filtrar_nomes_vogal_direto():
    # Lista de nomes para teste (substitua ou peça input do usuário se preferir)
    lista_de_nomes = ["Ana", "Bruno", "Elias", "Carla", "Igor", "Olga", "Zeca"]
    
    # Definindo as vogais em minúsculo
    VOGAIS = ['a', 'e', 'i', 'o', 'u']
    
    # Lista para guardar o resultado
    nomes_com_vogal = []

    # Loop principal
    for nome in lista_de_nomes:
        # Pega a primeira letra e a converte para minúscula
        primeira_letra = nome[0].lower()
        
        # Checa se a primeira letra está na lista de vogais
        if primeira_letra in VOGAIS:
            # Se for vogal, adiciona à lista de resultados
            nomes_com_vogal.append(nome)

    # Exibição do resultado
    print(f"Lista original: {lista_de_nomes}")
    
    if nomes_com_vogal:
        print(f"Nomes que começam com vogal: {nomes_com_vogal}")
    else:
        print("Nenhum nome da lista começa com vogal.")

# Executa o programa
filtrar_nomes_vogal_direto()