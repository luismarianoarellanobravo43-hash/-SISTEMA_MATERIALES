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