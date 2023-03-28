# Dicionario para armazenar o faturamento por estado. 'ESTADO' : [Faturamento,percentual]
# O percentual é inicialmente 0
faturamentos_por_estados = {'SP': [67836.43, 0], 'RJ': [36678.66, 0],
                            'MG': [23229.88, 0], 'ES': [27165.48, 0], 'OUTROS': [19849.53, 0]}

# Calculando o faturamento total
faturamento_total = 0
for valores in faturamentos_por_estados.values():
    faturamento_total += valores[0]

# Calculando e imprimindo os percentuais
print("PERCENTUAL")

for estado, valores in faturamentos_por_estados.items():
    # Arredondando o faturamento para duas casas decimais
    percentual = round(valores[0]/faturamento_total, 2)

    # Adicionando o percentual ao estado
    faturamentos_por_estados[estado] = [valores[0], percentual]

    print(f"{estado}: {int(percentual*100)}%")
