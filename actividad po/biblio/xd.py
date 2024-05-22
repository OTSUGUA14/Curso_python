import json

pedidos = {
    "pedidos":[
        {
            "id": 1,
            "nombre": "Juan",
            "productos": ["Mouse", "Teclado"]
        },
        {
            "id": 2,
            "nombre": "Ana",
            "productos": ["Monitor", "Parlantes"]
        },
        {
            "id": 3,
            "nombre": "Carlos",
            "productos": ["Mouse", "Parlantes"]
        }
    ]
}

with open("biblio.json", "w") as archivo:
    json.dump(pedidos, archivo, indent=4)
    
with open("biblio.json", "r") as archivo:
    contenido = json.load(archivo)
    print(contenido)

print(contenido["pedidos"][0])