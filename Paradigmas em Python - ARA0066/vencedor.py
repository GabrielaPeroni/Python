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
