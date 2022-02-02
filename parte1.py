import cProfile
def h():
    debitos  = []
    creditos = []
    i = 0
    
    debitos =[]
    creditos=[]
    i=0
    
    contc=0
    contd=0
    cont=0
    
    
    print("1. Ingresar debito")
    print("2. Ingresar credito")   
    print("3. Calcular total de debitos")
    print("4. Calcular total de creditos")
    print("5. Calcular Saldo")
    print("6. Calcular promedio de debitos")
    print("7. Calcular promedio de creditos")
    print("8. Mostrar monto de debitos mas grande")
    print("9. Conteo de operaciones de credito y debito")
    print("10. Mostrar todos los creditos y debitos")
    print("11. Eliminar creditos")
    print("12. Salir")
    
    
    
    while i != 12:
        i = int(input("Ingrese que desea realizar "))
        if i==1:
            debitos.append(int(input("Ingrese el debito ")))
            contd=contd+1
    
        if i==2:
            creditos.append(int(input("Ingrese el credito ")))
            contc=contc+1
    
        if i==3:
            c2=0
            for j in debitos:
                c2=c2+j
            print(c2)
    
        if i==4:
            c2=0
            for j in creditos:
                c2=c2+j
            print(c2)
    
        if i==5:
            c2=0
            for j in creditos:
                c2=c2+j
            for j in debitos:
                c2=c2-j
            print(c2)
    
        if i==6:
            cont=0
            c2=0
            for j in debitos:
                c2=c2+j
                cont=cont+1
            promedio=c2/cont
            print(promedio)
    
        if i ==7:
            cont=0
            c2=0
            for j in creditos:
                c2=c2+j
                cont=cont+1
            promedio=c2/cont
            print(promedio)
    
        if i ==8:
            c2=0
            for j in debitos:
                if j > c2:
                    c2=j
            print(c2)
            
        if i==9:
            print("Conteo de debitos",contd)
            print("Conteo de creditos",contc)
    
        if i==10:
            print("Debitos: ")
            for j in debitos:
                print(j)
            print("Creditos: ")
            for j in creditos:
                print(j)
    
        if i==11:
            creditos.clear()
cProfile.run('h()')