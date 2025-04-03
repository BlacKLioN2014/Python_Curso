# utilizamos break para salir de un bucle, cuando se alcanza un número específico
# numero_objetivo = 5
# i =1

# while i <= 10:
#     if i == numero_objetivo:
#         print(f'Numero: {numero_objetivo} encontrado, salimos del bucle')
#         break
#     print(i)
#     i  += 1


e = 1
while e <= 20:
    if  e % 2 == 0:
        print(f'par : {e}')
        e += 1
        continue
    print(f'Impar : {e}')
    e += 1