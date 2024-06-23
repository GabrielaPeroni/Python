'''14. Crie um algoritmo em Python que, dado um número informado pelo usuário, imprima a
tabuada dele de 1 a 10. Use o formato de apresentação.'''
num = int(input("Digite um numero: "))

print("\n===Tabuada do numero digitado ===\n")

for i in range(1,10 + 1):
    print(f"{num} x {i} = {num * i}")
