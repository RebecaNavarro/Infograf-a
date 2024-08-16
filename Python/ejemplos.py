def saludo (): 
     print ("hola")
     #tomar en cuenta sangria

print("Hello World")
edad = int(input("Que edad tiene?"))
nombre = "Rebe"
while edad > 0:
    print(f"Usted tiene {edad} años")
    edad = edad -1
    if nombre == "Rebe" and edad == 4:
        break


#for n in range(10,0,-3):
    #print(n)

nombre = "juan"
for char in nombre:
    if char == "a":
        print(char.upper)
        


estudiantes = {
    "sosa" : {
        "edad":30,
        "curso": "A",
        "notas" : {
            "QUI" : 50,
            "MAT" : 40
        }
    },
    "choque" : {
        "edad":30,
        "curso": "A",
        "notas" : {
            "QUI" : 50,
            "MAT" : 40
        }
    },
    "perez" : {
        "edad":30,
        "curso": "A",
        "notas" : {
            "QUI" : 50,
            "MAT" : 40
        }
    }
}

for nombre, datos in estudiantes.items():
    print(nombre,datos)

print("sosa" in estudiantes)

lista_precios = [50,20,21,90,50,60,87]
dias_semana = ["lunes", "martes"]

for dia in dias_semana[:5]:
    print(dia)

# devuelve tuplas:
for dia,precio in zip(dias_semana,lista_precios):
    print(dia, precio)

dias_2 = []

for i, dia in enumerate(dias_semana):
    if i%2==0:
        dias_2.append(dia)

dias_3 = [dia for i, dia in enumerate(dias_semana) if i % 2 == 0]

print(dias_2)

precios_2 = []

for precio in lista_precios:
    if precio > 50:
        precios_2.append(precio)

print(precios_2)