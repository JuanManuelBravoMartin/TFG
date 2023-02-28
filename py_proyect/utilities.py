def lastindex(lista,palabra):
    """Devuelve la ultima aparicion de un objeto en una lista."""
    aparicion = 0
    for x in range(len(lista)):
        if lista[x] == palabra:
            aparicion = x
    # print(aparicion)
    return aparicion

def firstindex(lista,palabra):
    """Devuelve la primera aparicion de un objeto en una lista."""
    aparicion = 0
    for x in range(len(lista)):
        if lista[x] == palabra:
            aparicion = x
            # print(aparicion)
            return aparicion
    
    return aparicion

def dibujar_matriz(matriz):
    
    """Funcion para mostrar la matriz."""
    constant = "                "
    total = len(matriz[-1]["Pipeline"])
    for x in range(total):
        ciclo = "C" + str(x+1)
        constant = constant + ciclo + "\t"
    constant += "\n"
    for y in matriz:
        if y["Accion"] == "add":
            instruccion = y["Accion"] + " " + y["Continente"] 
            for x in y["Ejecutor"]:
                instruccion += " , "+ x
            constant += instruccion
            constant += "\t"
            for z in y["Pipeline"]:
                constant += z + "\t"
            constant += "\n"
        else:
            instruccion = y["Accion"] + " " + y["Ejecutor"][0]
            instruccion += " , "+ y["Continente"]
            constant += instruccion
            constant += "\t"
            for z in y["Pipeline"]:
                constant += z + "\t"
            constant += "\n"
    print(constant)