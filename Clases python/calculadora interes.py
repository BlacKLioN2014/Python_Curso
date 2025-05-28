monto = int(input("ingresa el monto deseado: "))
tiempo = float(input("ingresa el tiempo estimado: "))
tasa = float(input("ingresa la tasa: "))

# M * T * T
calcular_interes =  monto * tiempo * tasa / 100
# print("El interes seria de: " + str(calcular_interes))
# print("Monto inicial: $" + str(monto) + " Tiempo (años) : " + str(tiempo) + " Tasa de interes: " + str(tasa) + "% Resultado final: $" + str(calcular_interes))
print(f"Monto inicial: {monto} ,Tiempo (años): {tiempo}, Tasa de interes: {tasa}%, Resultado final: ${calcular_interes}")