def submenu_sorts(pc):
    
    print("1. Ordenar por nombre")
    print("2. Ordenar por tipo")
    print("3. Ordenar por poder de combate")
    
    opcion = int(input("Opción: "))
    
    if opcion == 1:
        lista = pc.bubble_sort_nombre()

    elif opcion == 2:
        lista = pc.selection_sort_tipo()

    elif opcion == 3:
        lista = pc.ordenar_poder()
    
    else:
        print("opcion invalida")
        return

    for pokemon in lista:
        print(pokemon)