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