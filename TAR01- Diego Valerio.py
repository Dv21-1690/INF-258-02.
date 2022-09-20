x = int(input("Ingresa tu primer valor: " ))
y = int(input("Ingresa tu segundo valor: " ))

opcion = 0 

while opcion != 15:
    print("""
    Selecciona la opración a realizar:

    1 - Suma
    2 - Resta
    3 - Mutiplicación
    4 - División
    5 - Nueva operación 
    6-  Exit
    """)

    opcion = int(input())
    if opcion == 1:
        print(" ")
        print("Resultado: ", x, "+", y, "=", x+y)

    if opcion == 2:
        print(" ")
        print("Resultado: ", x, "-", y, "=", x-y) 

    if opcion == 3:
        print(" ")   
        print("Resultado: ", x, "*", y, "=", x*y)

    if opcion == 4:
        print(" ")
        print("Resultado: ", x, "/", y, "=", x/y)

    if opcion == 5:
        x = int(input("Ingresa tu primer valor: " ))
        y = int(input("Ingresa tu segundo valor: " ))

    if opcion == 6:
        print("Muchas gracias. Matricula: 21-1690, Diego Valerio")
        exit()




        