'''5. Escreva um algoritmo para ler o salário mensal atual de um funcionário e o percentual de
reajuste. Calcular e escrever o valor do novo salário.'''
salario = float(input("Digite seu salario mensal: "))
taxa = float(input("Digite o percentual de reajuste : "))

reajuste = salario * (taxa/ 100)
salario_novo = salario + reajuste

print("\nTaxa de reajuste: R$", reajuste)
print("Salario final: R$", salario_novo)
