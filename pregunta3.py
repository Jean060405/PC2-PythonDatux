#EJERCICIO 3
while True: 
    rpta = input("¿Desea ingrresar un numero?").upper()
    if rpta == "SI" :
        try : 
            num = int(input("Ingresar un numero"))
            print ("el numero es" , num)
        except ValueError:
            print("el numero ingresado no es correcto, ingrese denuevo")
            continue 
    elif rpta == "NO" :
        break 
    else :
        print('respuesta ingresada invalida')