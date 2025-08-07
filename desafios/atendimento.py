n = int(input())

urgentes_idosos = []
urgentes_jovens = []
normais_idosos = []
normais_jovens = []

for _ in range(n):
    entrada = input().strip()
    nome, idade, status = map(str.strip, entrada.split(","))
    idade = int(idade)

    if status == "urgente":
        if idade >= 60:
            urgentes_idosos.append((nome, idade))
        else:
            urgentes_jovens.append((nome, idade))
    else:
        if idade >= 60:
            normais_idosos.append((nome, idade))
        else:
            normais_jovens.append((nome, idade))

# Ordenar idosos por idade decrescente
urgentes_idosos.sort(key=lambda x: -x[1])
normais_idosos.sort(key=lambda x: -x[1])

# Construir ordem final
ordem = [p[0] for p in urgentes_idosos]
ordem += [p[0] for p in urgentes_jovens]
ordem += [p[0] for p in normais_idosos]
ordem += [p[0] for p in normais_jovens]

print("Ordem de Atendimento: " + ", ".join(ordem))  