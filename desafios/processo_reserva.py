def processar_reservas():
    # Entrada dos quartos disponíveis
    quartos_disponiveis = set(map(int, input().split()))

    # Entrada das reservas solicitadas
    reservas_solicitadas = list(map(int, input().split()))

    # Listas para armazenar as reservas processadas
    confirmadas = []
    recusadas = []

    # Processamento das reservas
    for reserva in reservas_solicitadas:
        if reserva in quartos_disponiveis:
            confirmadas.append(reserva)
            quartos_disponiveis.remove(reserva)  # Remove o quarto, pois já foi reservado
        else:
            recusadas.append(reserva)

    # Saída dos resultados conforme especificação
    print("Reservas confirmadas:", ", ".join(map(str, confirmadas)))
    print("Reservas recusadas:", ", ".join(map(str, recusadas)))

# Chamada da função principal
processar_reservas()