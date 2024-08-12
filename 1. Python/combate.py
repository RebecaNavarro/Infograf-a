import random

numero_rand = random.random()

HP1 = int(input("Vida del personaje 1 (entre 50 y 100)"))
HP2 = int(input("Vida del personaje 2 (entre 50 y 100)"))
danio_ataque_1 = 45
danio_ataque_2 = 48
dodge_prob_1 = float(input("Probabilidad de daño del personaje 1 (entre 0 y 1)"))
dodge_prob_2 = float(input("Probabilidad de daño del personaje 2 (entre 0 y 1)"))

for i in range (10):
    if random.random() < dodge_prob_1:
        print("esquiva")
    else:
        print("ouch")

contador = 10

while contador > 0:
    if HP1 <= 0:
        print("Personaje 2 gana")
        break
    if HP2 <= 0:
        print("Personaje 1 gana")
        break
    for i in range (10):
        if random.random() < dodge_prob_1:
            print("esquiva")   
        else:
            print("ouch")
            HP1 = HP1 - danio_ataque_2 
    for i in range (10):
        if random.random() < dodge_prob_1:
            print("esquiva")   
        else:
            print("ouch")
            HP2 = HP2 - danio_ataque_1
    contador= contador -1
