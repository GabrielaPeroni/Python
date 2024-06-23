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
