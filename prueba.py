numero = int(input("ingresa un numero hermano(si quieres salir pon un  numero negativo)"))
valor = 0
suma = 0
while valor == 0:
    if numero >= 1:
        for i in str(numero):
            numero = int(numero)
            suma += int(i)
            total = suma
            print(f"{total}")
            valor += 1 
    else:
        print("Debes ingresar un  numero positivo")
        valor += 1
        