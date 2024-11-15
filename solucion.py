# Leer el archivo de calificaciones
with open('data/calificaciones.txt', 'r') as file:
    lines = file.readlines()

# Inicializar una lista para almacenar las líneas procesadas
promedios = []

# Procesar cada línea del archivo
for line in lines:
    # Separar la línea en partes
    parts = line.strip().split()
    
    # Obtener el nombre y el apellido
    nombre = parts[0]
    apellido = parts[1]
    
    # Convertir las calificaciones a float y calcular el promedio
    calificaciones = list(map(float, parts[2:]))
    promedio = sum(calificaciones) / len(calificaciones)
    
    # Formatear el resultado
    resultado = f"{apellido.upper()}, {nombre}: {promedio:.1f}"
    promedios.append(resultado)

# Escribir los promedios en el nuevo archivo
with open('data/promedios.txt', 'w') as file:
    for promedio in promedios:
        file.write(promedio + '\n')

# Hacer el commit de la solución
print("Promedios calculados y guardados en data/promedios.txt")