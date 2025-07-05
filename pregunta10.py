#pregunta10
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
while True:
    fecha = input("Ingrese una fecha (MM/DD/AAAA o Mes D, AAAA): ").strip()
    try:
        if "/" in fecha:
            partes = fecha.split("/")
            mes = int(partes[0])
            dia = int(partes[1])
            año = int(partes[2])
        
        else:
            partes = fecha.replace(",", "").split()
            mes_texto = partes[0].capitalize()
            dia = int(partes[1])
            año = int(partes[2])

            if mes_texto in meses:
                mes = meses.index(mes_texto) + 1
            else:
                raise ValueError 

        if 1 <= mes <= 12 and 1 <= dia <= 31:
            # Imprimir con formato AAAA-MM-DD
            print(f"{año}-{mes:02}-{dia:02}")
            break
        else:
            print("Fecha inválida. Intente de nuevo.")
    
    except (ValueError, IndexError):
        print("Formato incorrecto. Intente nuevamente.")