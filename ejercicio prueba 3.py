import numpy as np
import msvcrt
asiento_Normal = 78900; asiento_Vip = 240000; total_pago = 0; total_pago_vip = 0
asientos = []
for i in range (1,42+1):
    asientos.append([i,'libre','nombre','rut','telefono','banco'])
while True:
    print()
    print ("******** Vuelos DUOCUC ********")
    print ("              Menu \n")
    print ("1.- Ver asientos disponibles")
    print ("2.- Comprar asiento")
    print ("3.- Anular vuelo")
    print ("4.- Modificar datos de pasajero")
    print ("5.- Salir\n")
    print ("*********************************************\n")
    opc = int(input("Seleccione opcion: "))
    if opc < 1 or opc > 5:      #delimitando el MENU
        print ()
        print ("ERROR =====> La opcion ingresada es incorrecta, intenta nuevamente")
        print("Presione una tecla para cargar nuevamente el MENU...")
        msvcrt.getch()  #comando para esperar tecla
    print ("")
    print ("*********************************************\n")
    try:
        if opc == 1:
            fila = "|\t"
            for asiento in asientos:
                if asiento [1] == 'libre':
                    fila += str(asiento[0]) + "\t"
                else:
                    fila += "X\t"
                    
                if int(asiento[0]) % 3 == 0 and int(asiento[0]) % 6 != 0:   #genera los cortes y paso de linea
                    fila += "\t"                                            #tabula la matriz
                if int(asiento[0]) % 6 == 0:
                    print(fila + "|")
                    fila = "|\t"
                    if asiento[0] == 30:
                        print("|" + "_" * 25 + "\t\t________________________|")                         #justificacion de matriz
                        print("|" + "_" * 25 + "\t\t________________________|")
                        print("|                                                               |")
            print ()
            print("Presione una tecla para continuar...")
            msvcrt.getch()
        if opc == 2:
            print ("")
            print ("Ingresar datos del pasajero.\n")
            nom_pasajero = str(input("Nombre y Apellidos: "))
            rut = str(input("Ingrese numero de RUT (sin puntos y con guion):"))
            Tel = int (input("Numero telefonico: "))
            banco = (input ("Banco: "))
            print ("")
            print ("**************** Elegir asiento ******************\n")
            print ("   Los asientos del 31 al 42 son VIP ($240.000)\n")
            asiento = int(input("Seleccione asiento: "))
            if asientos[asiento-1][1] != "libre":
                print ("El asiento seleccionado ya esta vendido")
            print ("")
            print ("*********************************************")
            if asiento >= 1 and asiento <= 30 and banco != 'duoc':
                print ("Usted eligio el asiento normal nº",asiento)
                print ("*****************************************")
                print ("")
                print ("El total a pagar es de:",asiento_Normal)
            else:
                if asiento >= 1 and asiento <= 30 and banco == 'duoc':
                    print ("Usted eligio el asiento normal nº",asiento)
                    print ("*****************************************")
                    print ("")
                    pago_desc = asiento_Normal * 0.75
                    print ("Se aplicara un 15% de descuento por pagar con Banco Duoc:",pago_desc)
            if asiento >= 31 and asiento <= 42 and banco != 'duoc':
                print ("Usted eligio el asiento VIP nº",asiento)
                print ("*****************************************")
                print ("")
                print ("El total a pagar es de:",asiento_Vip)
            else:
                if asiento >= 31 and asiento <= 42 and banco == 'duoc':
                    print ("Usted eligio el asiento VIP nº",asiento)
                    print ("*****************************************")
                    print ("")
                    pago_desc = asiento_Vip * 0.75
                    print ("Se aplicara un 15% de descuento por pagar con Banco Duoc:",pago_desc)
            print ("")           
            print ("Desea pagar el importe?")
            print ("1.- SI / 2.- NO")
            opc = int(input())
            if opc == 1:
                print ("Muchas gracias por su compra")
                asientos[asiento-1][1] = "ocupado"
                asientos[asiento-1][2] = nom_pasajero   #nombre pasajero
                asientos[asiento-1][3] = rut            #rut pasajero
                asientos[asiento-1][4] = Tel            #telefono pasajero
                asientos[asiento-1][5] = banco          #banco pasajero
            else:
                print ("No se genero ningun cargo, no se realiza la venta!!")
                print("Presione una tecla para cargar nuevamente el MENU...")
                msvcrt.getch()
        if opc == 3:
            print ("**************Anulacion de vuelo**************\n")
            asiento = int(input("Indique asiento: "))
            if asientos[asiento-1][1] != "libre":
                print ("El asiento seleccionado corresonde a:",asientos[asiento-1][2],"RUT:",asientos[asiento-1][3],"Telefono:",asientos[asiento-1][4] )
                opc = int(input("Seguro desea anular su vuelo?? 1.- SI / 2.- NO: "))
                if opc ==1:
                    asientos[asiento-1][1] != "libre" #ocupado
                    asientos[asiento-1][1] = "libre" #liberado
                    asientos[asiento-1][2] = ""     #nombre pasajero, liberado
                    asientos[asiento-1][3] = ""     #rut pasajero, liberado
                    asientos[asiento-1][4] = ""     #telefono pasajero, liberado
                    asientos[asiento-1][5] = ""     #banco pasajero, liberado
                    print ("Su vuelo fue anulado")
                    print("Presione una tecla para cargar nuevamente el MENU...")
                    msvcrt.getch()
                else:
                    print ("El vuelo no fue anulado")
                    print("Presione una tecla para cargar nuevamente el MENU...")
                    msvcrt.getch()
            else:
                print ("El asiento Nº",asiento,"No esta asignado a ningun pasajero")
                print("Presione una tecla para cargar nuevamente el MENU...")
                msvcrt.getch()
        if opc == 4:
            print("Modificar datos de pasajero\n")
            print ("*********************************************")
            asiento = int(input("Ingrese numero asiento: "))
            if asientos[asiento-1][2] == nom_pasajero:
                if asientos[asiento-1][3] == rut:
                    print ("Este asiento esta asignado a:",nom_pasajero,"RUT:",rut, "Telefono",Tel )
                    opc = int(input("La informacion es correcta?? 1.- SI / 2.- NO: "))
                    if opc == 1:
                        print ("Que opcion desea cambiar\n")
                        print ("1.- Nombre pasajero")
                        print ("2.- Telefono")
                        print ("3.- Desistir")
                        opc = int(input())
                        if opc ==1:
                            nom_pasajero = input("Ingrese el nuevo nombre de pasajero: ")
                            asientos[asiento-1][2] = nom_pasajero
                            print ("Se cambio con exito el nombre del pasajero")
                            print ("el nuevo nombre es:",asientos[asiento-1][2])
                            print("Presione una tecla para continuar...")
                            msvcrt.getch()
                        if opc ==2:
                            telef = int(input("Ingrese nuevo numero telefonico: "))
                            asientos[asiento-1][4] = telef
                            print ("Se cambio con exito el numero de telefono")
                            print ("el nuevo numero es:",asientos[asiento-1][4])
                            print("Presione una tecla para continuar...")
                            msvcrt.getch()
                        if opc == 3:
                            print ("No se realizan modificaciones a los datos del pasajero")
                            print("Presione una tecla para continuar...")
                            msvcrt.getch()
                    else:
                        print ("No se realizan modificaciones a los datos del pasajero")
                        print("Presione una tecla para continuar...")
                        msvcrt.getch()
            if asientos[asiento-1][1] == "libre":
                print ("El asiento ingresado No esta asignado a ningun pasajero")
                print("Presione una tecla para continuar...")
                msvcrt.getch()
        if opc == 5:
            opc = int(input("Realmente desea salir del programa?? 1.- SI / 2.- NO: "))
            if opc ==1:
                print ()
                print("Presione una tecla para salir del programa...")
                print ()
                print ("Hasta luego")
                print ()
                msvcrt.getch()
                print ("*****************************************")
                break
            else:
                print ()
                print("Presione una tecla para cargar nuevamente el MENU...")
                msvcrt.getch()
    except:
        print ("ERROR =====> Datos incorrecto")   


    

