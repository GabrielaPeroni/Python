'''1. Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa.
Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$
1.500,00 mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário
total.'''

salario_fixo = float(input("Digite o seu salario: R$"))
vendas = float(input("Digite o valor total das vendas efetuadas: R$"))

comissao = vendas * 0.03

if vendas > 1500:
    comissao = 1500 * 0.03 + (vendas - 1500) * 0.05

salario_total = salario_fixo + comissao
print("\nSeu salario total é: R$",salario_total)

'''2. Escreva um algoritmo para ler as dimensões de um retângulo (base e altura), calcular e
escrever a área do retângulo.'''
base = float(input("Digite a base do triangulo: "))
altura = float(input("Digite a altura do triangulo: "))

area = (base * altura)/ 2
print("\nA area do triangulo e: ",area)

'''3. Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e
escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e
mês com 30 dias.'''
print("=== Digite sua data de nascimento em numeros ===\n\n")

dia = int(input("Dia: "))
mes = int(input("Mes: "))
ano = int(input("Ano: "))

dia_meses = mes * 30
dia_anos = ano * 365
total_dia = dia + dia_meses + dia_anos

print("\nSua idade em dias é: : ",total_dia)
  
'''4. Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após,
calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também testar se
saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão
escrever a mensagem 'Saldo Negativo'.'''
print("=== Preencha os dados abaixo referentes a sua conta ===\n")

conta = int(input("Numero da conta: "))
saldo = float(input("Saldo: R$"))
debito = float(input("Debito: R$"))
credito = float(input("Credito: R$"))

saldo_atual = saldo - debito + credito

print(f"\n=== Detalhes da conta {conta} ===\n")
print("Saldo final - R$", saldo_atual)

if saldo_atual >= 0:
    print("Status - Positivo") # "Saldo positivo"
else:
    print("Status - Negativo") # "Saldo negativo"

'''5. Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de
reajuste. Calcular e escrever o valor do novo salário.'''
salario = float(input("Digite seu salario mensal: "))
taxa = float(input("Digite o percentual de reajuste : "))

reajuste = salario * (taxa/ 100)
salario_novo = salario + reajuste

print("\nTaxa de reajuste: R$", reajuste)
print("Salario final: R$", salario_novo)

'''6. Programa em Python que leia o nome de 2 times e o número de gols marcados na partida
(para cada time). Escrever o nome do vencedor. Caso não haja vencedor deverá ser
impressa a palavra EMPATE.'''
partida = int(input("Qual o numero de partidas ? "))

gol_1 = [0] * partida
gol_2 = [0] * partida

total_1 = 0
total_2 = 0

for i in range(partida):
    print("\n= Partida ", i+1 ," =\n")
    gol_1[i] = int(input("Gols do time 1: "))
    gol_2[i] = int(input("Gols do time 2: "))

    total_1 += gol_1[i]
    total_2 += gol_2[i]

print("\n=== Resultado Final ===\n")
print("Total de gols do Time 1: ", total_1)
print("Total de gols do Time 2: ", total_2)

if total_1 > total_2:
    print("\nTime 1 venceu!")
elif total_1 < total_2:
    print("\nTime 2 venceu!")
else:
    print("\nEmpate!")

'''7. Escreva um programa em Python que recebe um inteiro e informe se é par ou ímpar.'''
num = int(input("Digite um numero: "))

if num %2 == 0:
    print("\nSeu numero é par!")
else:
    print("\nSeu numero é impar!")

'''8. Ler um valor e escrever se é positivo ou negativo (considere o valor zero como positivo).'''
num = int(input("Digite um numero: "))

if num >= 0:
    print("\nSeu numero é positivo!")
else:
    print("\nSeu numero é negativo!")

'''9. Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e
escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota
igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.'''
nota_1 = float(input("Digite sua nota 1a: "))
nota_2 = float(input("Digite sua nota 2a: "))

media = (nota_1 + nota_2) / 2

print(f"\n... Nota final: {nota_1 + nota_2}/2  = {media} ...")
if media >= 6:
    print("Status - Aprovado !")
else:
    print(f"Status - Reprovado por {6 - media} pontos.")

'''10. Faça um programa que peça dois números ao usuário e mostre qual o maior e qual o
menor.'''
num_1 = int(input("Digite o primeiro numero: "))
num_2 = int(input("Digite o segundo numero: "))

if num_1 > num_2:
    print(f"{num_1} e maior que {num_1}")
elif num_1 < num_2:
    print(f"{num_2} e maior que {num_1}")
else:
    print("\nOs numeros sao iguais")

'''11. Para doar sangue é necessário ter entre 18 e 67 anos. Faça um aplicativo na linguagem
Python que pergunte a idade de uma pessoa e diga se ela pode doar sangue ou não.'''
idade = int(input("Digite sua idade: "))

if idade >= 18 and idade <= 67:
    print("Meus parabens, sua idade te permite doar sangue!")
elif idade < 18:
    print("Infelizmente voce é muito novo para doar sangue..")
else:
    print("Infelizmente voce ultrapassou a idade para doar sangue..")

'''12. Faça um programa em Python que imprima de 1 a 50 na tela.'''
for i in range(50):
    print(i+1)

'''13. Elabore um código que imprima uma sequência de 1 até 100 somente com os números
pares dessa sequência.'''
for i in range(1,100 + 1):
    if i %2 == 0:
        print(i)
'''14. Crie um algoritmo em Python que, dado um número informado pelo usuário, imprima a
tabuada dele de 1 a 10. Use o formato de apresentação.'''
num = int(input("Digite um numero: "))

print("\n===Tabuada do numero digitado ===\n")

for i in range(1,10 + 1):
    print(f"{num} x {i} = {num * i}")

'''15. Desenvolva um programa em Python, que imprima os números pares entre 1 e 100.'''
for i in range(1, 100):
    if i %2 == 0:
        print(i)
        
'''16. Faça um script em Python que imprima na tela os múltiplos de 5 entre 1 e 100.'''
for i in range(1, 100):
    if i %5 == 0:
        print(i)

'''17. Desenvolva um código em Python que calcule a média aritmética entre 1 e 20.'''
mult = 0

for i in range(1,20 + 1): # 210
    mult += i

print(mult/ 20)

'''18. Escreva um algoritmo em Python que leia o número de litros vendidos e o tipo de
combustível (codificado da seguinte forma: 1 - álcool, 2 - gasolina), calcule e imprima o
valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 3,30 e o
preço do litro do álcool é R$ 2,90. Os cálculos finais são definidos de acordo com a tabela
abaixo:

Alcool   -  Ate 20 litros, desconto de 3% por litro
            acima de 20 litros, desconto de 5% por litro
Gasolina -  Até 20 litros, desconto de 4% por litro
            acima de 20 litros, desconto de 6% por litro'''
num = int(input("Digite qual o tipo de combustivel [1 - Alcool, 2- Gasolina] "))
litro = float(input("Quantos litros foram comprados ? "))

alcool = 2.90
gasolina = 3.30

if num == 1: # Alcool
    if litro <= 20:
        preco = litro * (alcool - (alcool * 0.03))
    else:
        preco = litro * (alcool - (alcool * 0.05))
        
elif num == 2: # Gasolina
    if litro <= 20:
        preco = litro * (gasolina - (gasolina * 0.04))
    else:
        preco = litro * (gasolina - (gasolina * 0.06))
else:
    print("\nOpcao invalida.")

print(f"\nValor a ser pago: R${preco}")

'''19. Faça um script em Python que calcule o fatorial de um número n informado pelo usuário.
O fatorial de um número é calculado pela multiplicação desse número por todos os seus
antecessores até chegar ao número 1. '''
num = int(input("Digite um numero: "))
fat = 1

for i in range(1, num + 1):
    fat *= i

print(f"O fatorial de {num} é: {fat}")