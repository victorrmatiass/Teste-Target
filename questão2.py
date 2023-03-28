# FUNÇÃO RECURSIVA QUE RETORNA O NÚMERO DE FIBONACCI A DEPENDER DO INDICE DA SEQUENCIA
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# FUNÇAO RECURSIVA PARA VERIFICAR SE O NÚMERO ESTÁ NA SEQUÊNCIA DE FIBONACCI
def pertenceFibonacci(n, incrementador=0):
    numero_fibonacci = fibonacci(incrementador)
    if n == numero_fibonacci:
        return True
    elif n > numero_fibonacci:
        return pertenceFibonacci(n, incrementador+1)
    else:
        return False


# ENTRADA
numero = int(input("Digite um número inteiro não nulo: "))

# SAÍDA
if pertenceFibonacci(numero):
    print(f"{numero} pertence a sequência de fibonacci.")

else:
    print(f"{numero} não pertence a sequência de fibonacci.")
