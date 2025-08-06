# Entrada
email = input()

# Regras
tem_arroba = "@" in email
nao_comeca_ou_termina_com_arroba = not (email.startswith("@") or email.endswith("@"))
nao_tem_espaco = " " not in email
tem_dominio_valido = email.endswith("@gmail.com") or email.endswith("@outlook.com")

# Validação final
if tem_arroba and nao_comeca_ou_termina_com_arroba and nao_tem_espaco and tem_dominio_valido:
    print("E-mail válido")
else:
    print("E-mail inválido")