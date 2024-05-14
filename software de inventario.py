print ('bienvenido al inventario'.center(60,'-'))
cantidad=[ ]
producto=[ ]
precio=[ ]

while True:
    print("""
    (1) añadir productos
    (2) buscar productos
    (3) modificar productos
    (4) ver productos
    (5) salir
    """)

    respuesta=int(input('ingrese su opcion:'))
    if respuesta == 1:
        ac=int(input('ingrese la cantidad de su producto:'))
        ap=input('ingrese el nombre de su producto:')
        apre=str(input('ingrese el precio de su producto:'))

        cantidad.append(ac)
        producto.append(ap)
        precio.append(apre)
    elif respuesta==2:
        buscador=input('ingrese el nombre del producto:')
        posicion=producto.index(buscador)
        print('la cantidad del producto es:',cantidad[posicion ])
        print('el nombre del producto es:',producto[posicion ])
        print('el precio del producto es:',precio[posicion ])

    elif respuesta==3:
        buscador=input('ingrese el nombre del producto que quiere modificar:')
        posicion=producto.index(buscador)
        ac=int(input('ingrese la cantidad de su producto:'))
        ap=input('ingrese el nombre de su producto:')
        apre=str(input('ingrese el precio de su producto:'))
        cantidad[posicion]=ac
        producto[posicion]=ap
        precio[posicion]=apre
    elif respuesta==4:
        print('la cantidad es:',cantidad)
        print('el nombre es:',producto)
        print('el precio es:',precio)
    else:
        break   