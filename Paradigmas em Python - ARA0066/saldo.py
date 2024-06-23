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
