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
