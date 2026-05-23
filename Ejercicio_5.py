#Matriz de horas trabajadas por cada integrante del equipo
matriz_horas = [
    ["Carlos Pérez", 8, 9, 8, 8, 10],
    ["Ana María Gómez", 8, 8, 8, 7, 8],
    ["Luis Rodríguez", 9, 9, 10, 8, 8],
    ["Laura Beltrán", 8, 8, 8, 8, 8]
]


def procesar_horarios(matriz):

    print("REPORTE DE HORAS SEMANALES")

    print("-" * 30)
    
    for recurso in matriz:
        nombre = recurso[0]
        total_horas = sum(recurso[1:])
        
        if total_horas > 40:
            clasificacion = "Sobretiempo"
        else:
            clasificacion = "Horario Estándar"
            
        print(f"{nombre}: {total_horas} horas ({clasificacion})")

    print("-" * 30)

procesar_horarios(matriz_horas)