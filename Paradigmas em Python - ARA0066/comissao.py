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
