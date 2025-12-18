import json

equipos = [
    {
        "Nombre": "Real Madrid",
        "país": "España",
        "nivelAtaque": 92,
        "nivelDefensa": 88
    },
    {
        "Nombre": "Manchester City",
        "país": "Inglaterra",
        "nivelAtaque": 94,
        "nivelDefensa": 85
    },
    {
        "Nombre": "Bayern Múnich",
        "país": "Alemania",
        "nivelAtaque": 89,
        "nivelDefensa": 87
    },
    {
        "Nombre": "Liverpool FC",
        "país": "Inglaterra",
        "nivelAtaque": 90,
        "nivelDefensa": 84
    }
]

json_legible = json.dumps(equipos, indent=4, ensure_ascii=False)

print("Lista de Equipos en formato JSON:")
print(json_legible)