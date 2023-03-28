import json

# Carregando e lendo o json
with open('dados.json', encoding='utf-8') as dados_json:
    dados = json.load(dados_json)

# Valor minimo inicial é definido como infinito
valor_minimo_com_0 = float("inf")
valor_minimo_sem_0 = float("inf")

# Valor máximo inicial é definido como -1
valor_maximo = -1

# Definindo as variaveis montante e dias uteis para calcular a média
montante = 0
dias_uteis = 0

# Dias com faturamente maior que a media mensal é definido inicialmente como 0
dias_superiores = 0

# Usando apenas um for para realizar todas as comparações de minimo, maximo e adição ao montante para diminuir a complexidade do código
for dia in dados:

    valor_atual = dia['valor']

    # Comparações para os valores mínimos
    if valor_atual < valor_minimo_com_0:
        valor_minimo_com_0 = valor_atual
    if valor_atual < valor_minimo_sem_0 and valor_atual != 0:
        valor_minimo_sem_0 = valor_atual

    # Comparação para o valor máximo
    if valor_atual > valor_maximo:
        valor_maximo = valor_atual

    # Adcionando o valor atual ao montante
    if valor_atual != 0:
        montante += valor_atual
        dias_uteis += 1

# Calculando a media mensal
media_mensal = montante/dias_uteis

# Realizando a comparação de dias com faturamento superior a media mensal
for dia in dados:

    valor_atual = dia['valor']

    if valor_atual > media_mensal:
        dias_superiores += 1


# Saídas
print(
    f'O menor valor de faturamento no mês (considerando os zeros) foi de R${valor_minimo_com_0:.2f}')

print('---------------------------------')

print(
    f'O menor valor de faturamento no mês (desconsiderando os zeros) foi de R${valor_minimo_sem_0:.2f}')

print('---------------------------------')

print(
    f'O maior valor de faturamento no mês foi de R${valor_maximo:.2f}')

print('---------------------------------')

print(
    f'O número de dias no mês em que o valor de faturamento diário foi superior à média mensal foi {dias_superiores} dias.')
