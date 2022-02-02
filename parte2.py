import cProfile
def b(): 
    Catalogo = [{'Codigo': 1, 'Nombre': 'Naranja', 'Precio': 10 }, 
                {'Codigo': 2, 'Nombre': 'Manzana', 'Precio': 15},
                {'Codigo': 3, 'Nombre': 'Pera', 'Precio': 20},
                {'Codigo': 4, 'Nombre': 'Uvas', 'Precio': 25},
                {'Codigo': 5, 'Nombre': 'Fresa', 'Precio': 15},
                {'Codigo': 6, 'Nombre': 'Melon', 'Precio': 12},
                {'Codigo': 7, 'Nombre': 'Sandia', 'Precio': 10},
                {'Codigo': 8, 'Nombre': 'Melocoton', 'Precio': 17},
                {'Codigo': 9, 'Nombre': 'Maracuya', 'Precio': 25},
                {'Codigo': 10, 'Nombre': 'Mandarina', 'Precio': 14}]
    venta =[]
    compra =[]
    opcion = 0
    pt = 0
    cont = 0
    cont1=0
    cont2=0
    tope=0
    
    print("1. Ingresar items de compra")
    print("2. Ingresar uno o mas pagos")
    print("3. Mostrar el total del recibo de compra")
    print("4. Mostras el total de pagos")
    print("5. Mostrar el saldo pendiente de pago ")
    print("6. Promedio de precio por item ")
    print("7. Mostrar producto mas caro ")
    print("8. Imprimir recibo ")
    print("9. Salir \n")
    
    def buscador(x,y):
        for codigo1 in y:
            if codigo1['Codigo'] == x:
                return codigo1
    
    while opcion != 9:
        
        opcion = int(input("Que desea realizar: "))
        if opcion == 1:
            item = int(input("Ingreso el codigo del producto que desea: "))
            if(item >0  and item <10):
                u = buscador(item, Catalogo)
                p = u['Precio']
                pt = p + pt
                cont += 1
                compra.append(u)
                if p > tope:
                    tope = p
                print("Compra realizada \n")
            else:
                print("Codigo no existente en catalogo")      
    
        if opcion == 2:
            pago = int(input("Ingrese su pago: "))
            venta.append(pago)
            cont1 = pago + cont1
    
            if cont1 == pt:
                print("Compra cancelada")
            if cont1 > pt:
                saldo = pt - cont1
                print("Pago completado, tiene a su favor", saldo*+1)
    
        if opcion == 3:
            print("Su recibo de compra es: ", compra)
            a = pt
            print("Su total es: ", pt)
    
        if opcion == 4:
            print("Su total de pagos",  venta)
    
        if opcion == 5:
            saldo2 = pt - cont1
            print("Su saldo restante: ", saldo2)
    
        if  opcion == 6: 
            PpromedioI = pt/cont
            print("El promedio del precio por item es de: ", PpromedioI)
            
        if  opcion == 7:
            print("El producto mas caro es: ", tope)
            
        if opcion == 8:
            print("Sus productos son", compra, "\n")
            print("Su deuda total es: ", pt)
                
            print("Debe: ", saldo2)
    
            print("Pago: ", (saldo2-pt)*-1)
cProfile.run('b()')    
    
    
    
    
    
