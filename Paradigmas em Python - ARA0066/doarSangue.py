'''11. Para doar sangue é necessário ter entre 18 e 67 anos. Faça um aplicativo na linguagem
Python que pergunte a idade de uma pessoa e diga se ela pode doar sangue ou não.'''
idade = int(input("Digite sua idade: "))

if idade >= 18 and idade <= 67:
    print("Meus parabens, sua idade te permite doar sangue!")
elif idade < 18:
    print("Infelizmente voce é muito novo para doar sangue..")
else:
    print("Infelizmente voce ultrapassou a idade para doar sangue..")
