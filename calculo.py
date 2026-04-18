# Versión 1: Banner de Sistema [cite: 18]
print("---------------------------------------------------------")
print("+++++++++++++++ 3D SERVICES S.A. +++++++++++++++")
print("++++++ SISTEMA DE CÁLCULO DE MATERIALES ++++++")
print("---------------------------------------------------------")

# Versión 2: Banner y flujo secuencial [cite: 33, 34]
print("---------------------------------------------------------")
print("+++++++++++++++ 3D SERVICES S.A. +++++++++++++++")
print("++++++ SISTEMA DE CÁLCULO DE MATERIALES ++++++")
print("---------------------------------------------------------")

volumen = float(input("Ingrese el volumen de la pieza (ml): "))
costo_ml = float(input("Ingrese el costo de la resina por ml ($): "))
costo_total = volumen * costo_ml

print(f"\nEl costo total de manufactura es: ${costo_total:.2f}")

# Versión 3: Validador de Impresión [cite: 47, 48]
print("---------------------------------------------------------")
print("+++++++++++++++++++ 3D SERVICES S.A. ++++++++++++++++++++")
print("++++++++++++ SISTEMA DE CÁLCULO DE MATERIALES +++++++++++")
print("---------------------------------------------------------")

capacidad_maxima = 500.0
volumen = float(input("Ingrese el volumen de la pieza (ml): "))

if volumen > capacidad_maxima:
    print("¡Error! La pieza excede la capacidad máxima de la impresora (500 ml).")
    print("Sugerencia: Divida el modelo en partes más pequeñas.")
else:
    costo_ml = float(input("Ingrese el costo de la resina por ml ($): "))
    costo_total = volumen * costo_ml
    print("Estado: ¡Aprobado para impresión!")
    print(f"El costo total será: ${costo_total:.2f}")

    # Versión 4: Gestor de Lotes de Producción
print("---------------------------------------------------------")
print("+++++++++++++++++++ 3D SERVICES S.A. ++++++++++++++++++++")
print("++++++++++++ SISTEMA DE CÁLCULO DE MATERIALES +++++++++++")
print("---------------------------------------------------------")
cantidad_piezas = int(input("¿Cuántas piezas distintas componen el lote?: "))
costo_ml = float(input("Ingrese el costo de la resina por ml ($): "))
volumen_total_lote = 0.0
for i in range(cantidad_piezas):
volumen_pieza = float(input(f"Ingrese el volumen de la pieza {i+1} (ml): "))
volumen_total_lote += volumen_pieza # Acumulador
costo_total_lote = volumen_total_lote * costo_ml
print("\n--- Resumen de Producción ---")
print(f"Total de piezas: {cantidad_piezas}")
print(f"Volumen total requerido: {volumen_total_lote:.2f} ml")
print(f"Costo total del lote: ${costo_total_lote:.2f}")

# Versión 5: Reto adicional - Validaciones y filtros de seguridad
print("---------------------------------------------------------")
print("+++++++++++++++++++ 3D SERVICES S.A. ++++++++++++++++++++")
print("++++++++++++ SISTEMA DE CÁLCULO DE MATERIALES +++++++++++")
print("---------------------------------------------------------")

cantidad_piezas = int(input("¿Cuántas piezas distintas componen el lote?: "))
costo_ml = float(input("Ingrese el costo de la resina por ml ($): "))
volumen_total_lote = 0.0
piezas_aceptadas = 0

for i in range(cantidad_piezas):
    print(f"\n--- Procesando Pieza {i+1} ---")
    volumen_pieza = float(input(f"Ingrese el volumen de la pieza (ml): "))
    
    # Validación 1: No permitir valores negativos o cero [cite: 81]
    if volumen_pieza <= 0:
        print("¡Error! El volumen debe ser un número positivo. Saltando...")
        continue # Salta a la siguiente iteración del ciclo 
        
    # Validación 2: Límite físico de la impresora (500 ml) 
    if volumen_pieza > 500:
        print("¡Error! La pieza excede los 500 ml permitidos. Saltando...")
        continue # No suma esta pieza al lote y continúa con la siguiente 
    
    # Si pasa las validaciones, se acumula
    volumen_total_lote += volumen_pieza
    piezas_aceptadas += 1
    print("Estado: Pieza agregada con éxito.")

# Cálculo final sobre las piezas válidas
costo_total_lote = volumen_total_lote * costo_ml

print("\n=========================================")
print("         RESUMEN DE PRODUCCIÓN")
print("=========================================")
print(f"Piezas aceptadas: {piezas_aceptadas} de {cantidad_piezas}")
print(f"Volumen total acumulado: {volumen_total_lote:.2f} ml")
print(f"Costo total del lote: ${costo_total_lote:.2f}")
print("=========================================")