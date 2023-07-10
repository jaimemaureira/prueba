
descripcion = 0;
material =[]; descripcion =[]; umb =[]; cant_recep =[]; equiv_cajas =[]; fecha_recep =[]
tiempo_rev_caja =[]; proveedor =[]; cajas_sin_etiq =[]
bodega1 =[]; bodega2 =[]; bodega3 =[]
bodega = ([material,descripcion,umb,cant_recep,equiv_cajas,fecha_recep,tiempo_rev_caja,
              proveedor,cajas_sin_etiq])
#bodega2.append([material,descripcion,umb,cant_recep,equiv_cajas,fecha_recep,tiempo_rev_caja,
              #proveedor,cajas_sin_etiq])
#bodega3.append([material,descripcion,umb,cant_recep,equiv_cajas,fecha_recep,tiempo_rev_caja,
              #proveedor,cajas_sin_etiq])
while True:
    print ()
    print ("Menu Alejandra Store")
    print ("****************************\n")
    print ("1.- Ingreso de mercaderia")
    print ("2.- Productos")
    print ("3.- Salida o venta mercaderia")
    print ("4.- Salir\n")
    opc = int (input("Elija su opcion: "))
    if opc == 1:
        while True:
            codigo = (input("Ingrese codigo del producto: "))
            if len(codigo) == 8:
                material.append(codigo)
                descripcion.append(input("Ingrese descripcion del producto: "))
                umb.append(input("Ingrese UMB: "))
                cant_recep.append(input("Ingrese cantidad recepcionada: "))
                equiv_cajas.append(input("Ingrese equivalencia en cajas: "))
                fecha_recep.append(input("Ingrese fecha de recepcion: "))
                tiempo_rev_caja.append(input("Ingrese tiempo de revision X caja: "))
                proveedor.append(input("Ingrese nombre del proveedor: "))
                cajas_sin_etiq.append(input("Ingrese cantidad de cajas sin etiquetar: "))
                print ()
                print ("***************************************\n")
                print ("A que bodega corresponde estos productos?:")
                print ("***************************************\n")
                print ("1.- Productos peligrosos")
                print ("2.- Productos alto valor")
                print ("3.- Productos perecibles")
                opc = int(input("Ingrese su opcion: "))
                if opc == 1:
                    bodega1.append(bodega)
                    print ("Se guardo la informacion en la bodega de Productos peligrosos")
                    print (bodega1)
                elif opc == 2:
                    bodega.append([material,descripcion,umb,cant_recep,equiv_cajas,fecha_recep,tiempo_rev_caja,
              proveedor,cajas_sin_etiq])
                    print ("Se guardo la informacion en la bodega de Productos alto valor")
                elif opc == 3:
                    bodega.append([material,descripcion,umb,cant_recep,equiv_cajas,fecha_recep,tiempo_rev_caja,
              proveedor,cajas_sin_etiq])
                    print ("Se guardo la informacion en la bodega de Productos perecibles")
                
            else:
                print("El codigo debe ser de 8 caracteres")
            
    if opc == 2:
        print ()
        print ("    Seleccione bodega para ver productos")
        print ("***********************************************\n")
        print ("1.- Productos peligrosos")
        print ("2.- Productos alto valor")
        print ("3.- Productos perecibles\n")
        opc == int(input("Ingrese su opcion: "))
        if opc == 1:
            print("seguro deseas continuar?")
        
            
            




