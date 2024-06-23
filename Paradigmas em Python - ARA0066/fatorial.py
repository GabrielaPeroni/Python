'''19. Faça um script em Python que calcule o fatorial de um número n informado pelo usuário.
O fatorial de um número é calculado pela multiplicação desse número por todos os seus
antecessores até chegar ao número 1. '''
num = int(input("Digite um numero: "))
fat = 1

for i in range(1, num + 1):
    fat *= i

print(f"O fatorial de {num} é: {fat}")
