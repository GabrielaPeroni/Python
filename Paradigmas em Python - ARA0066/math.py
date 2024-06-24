import math

def soma(): #soma
    num = float(input("\nQuantos numeros deseja somar ? "))
    somas = []

    if num < 2:
        print("E necessário pelo menos dois numeros.")
    else:
        for i in range(num):
            somas.append(float(input(f"{i+1} numero -> ")))

        print(math.fsum(somas))

def sub(): # Subtracao
    num = float(input("\nQuantos numeros deseja subtrair ? "))

    if num < 2:
        print("E necessário pelo menos dois numeros.")
    else:
        result = float(input(f"1 numero -> "))
        for i in range(1,num):
            subtracao = float(input(f"{i+1} numero -> "))
            result -= subtracao

        print(result)

def mult(): # Multiplicacao
    num = float(input("\nQuantos numeros deseja multiplicar ? "))
    multiplicacao = []

    if num < 2:
        print("E necessário pelo menos dois numeros.")
    else:
        for i in range(num):
            multiplicacao.append(float(input(f"{i+1} numero -> ")))

        print(math.prod(multiplicacao))

def div(): # Divisao
    num = float(input("\nQuantos numeros deseja dividir ? "))

    if num < 2:
        print("E necessário pelo menos dois numeros.")
    else:
        result = float(input(f"1 numero -> "))

        for i in range(1,num):
            divisao = float(input(f"{i+1} numero -> "))
            result /= divisao

        print(result)

def exp(): # Potencia
    x = float(input("\nDigite a base --> "))
    y = float(input("\nDigite o expoente --> "))

    print(math.pow(x, y)) # X^y

def raiz(): # Raiz
    raiz = float(input("\nDigite o numero --> "))
    print(math.sqrt(raiz))

def fat(): # Fatorial
    fatorial = float(input("\nDigite o numero --> "))   
    print(math.factorial(fatorial))

def log(): # Log
    base = float(input("\nDigite a base do logaritmo --> "))
    num = float(input("\nDigite o numero --> "))

    print(math.log(num, base))


print("======= CALCULADORA =======\n\n")

print("Selecione a operacao desejada:\n")
print("\n[1] Soma \n[2] Subtracao \n[3] Multiplicacao")
print("\n[4] Divisao \n[5] Potenciacao \n[6] Fatorial")
print("\n[7] Raiz Quadrada \n[8] Log")

num = int(input("\n--> "))

print("Resultado da conta ")
match num:
    case 1:
        soma()
    case 2:
        sub()
    case 3:
        mult()
    case 4:
        div()
    case 5:
        exp()
    case 6:
        fat()
    case 7:
        raiz()
    case 8:
        log()
    case _:
        print("Operacao invalida!\nPor favor, selecione um numero de 1 a 8.")