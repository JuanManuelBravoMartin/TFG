a = """sw a , a(222)
sw a , a
add a, a, b """

BASIC_WORK = ["IF","ID","EX","M","WB"]
BASIC_READ = []
BASIC_WRITE = []
copia = ["IF","ID","EX","M","WB"]
WB = True
ACCESO_DATOS = 2 ###### CICLOS DE ACCESO A LA MEMORIA DE DATOS ######
ACCESO_ESCRITURA = 5 ###### CICLOS DE ACCESO A LA ESCRITURA DE DATOS ######
ACCESO_LECTURA = 1 ###### CICLOS DE ACCESO A LA LECTURA DE DATOS ######
RWEXCEPTIONS = " "

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
def set_basics():
    """ Combina a informacion dada con los tipos de arrays, en favor de hacer la programacion mas facil"""
    if (ACCESO_DATOS !=1):
        for _ in range(ACCESO_DATOS -1):
            BASIC_WORK.insert(0,"IF")
    for x in BASIC_WORK:
        BASIC_READ.append(x)
        BASIC_WRITE.append(x)
    if (ACCESO_ESCRITURA != 1):
        i = BASIC_WRITE.index("M")
        for _ in range(ACCESO_ESCRITURA -1):
            BASIC_WRITE.insert(i,"M")
    if (ACCESO_LECTURA != 1):
        i = BASIC_READ.index("M")
        for _ in range(ACCESO_LECTURA -1):
            BASIC_READ.insert(i,"M")

def parser (programa):
    """Funcion que divide el programa(un string) en diccionarios, asociandolos a una de las filas de la matriz, con su tipo
    de instruccion. Una vez hecho esto, y de forma temporal, ejecuta las fucniones que detectan que las instrucciones se pisan
    entre si"""
    contador = 0
    matriz = []
    partido = programa.split("\n")
    for linea in partido:
        if (linea.split(" ")[0] == "sw" or linea.split(" ")[0] == "lw"):
            accion, var1, var2 = memory_function(linea)
            if (accion == "sw"):
                variable = BASIC_WRITE.copy()
                for _ in range(contador):
                    variable = ["-"] + variable
                matriz.append({"Accion": accion,"Continente": var2, "Ejecutor": [var1], "Pipeline": variable})
            elif (accion == "lw"):
                variable = BASIC_WORK.copy()
                for _ in range(contador):
                    variable = ["-"] + variable
                matriz.append({"Accion": accion,"Continente": var1, "Ejecutor": [var2], "Pipeline": BASIC_READ.copy()})
        elif (linea.split(" ")[0] == "add"):
            variable = BASIC_WORK.copy()
            for _ in range(contador):
                variable = ["-"] + variable
            accion, var1, var2, var3 = arith_function(linea)
            matriz.append({"Accion": accion,"Continente": var1, "Ejecutor": [var2,var3], "Pipeline": variable})
        contador += 1
    check_problems(matriz)
    check_consistency(matriz)
    printear(matriz)


def check_consistency(matriz):
    """Dada una matriz de filas del pipeline, busca si en la fila anterior se encuentra ocupado el hueco en el que tiene que entrar la nueva fila."""
    for x in range(1,len(matriz)):
        anterior = matriz[x-1]["Pipeline"].copy()
        siguiente = matriz[x]["Pipeline"].copy()
        for i in copia:
            # print(i)
            indice_anterior = lastindex(anterior,i)
            indice_siguiente = firstindex(siguiente,i)
            dif = indice_anterior - indice_siguiente
            if dif >= 0:
                for i in range(dif+1):
                    siguiente.insert(indice_siguiente,"-")
        matriz[x-1]["Pipeline"] = anterior.copy()
        matriz[x]["Pipeline"] = siguiente.copy()
    return matriz
def check_problems(matriz):
    """Funcion que comprueba los problemas en la matriz del tipo RaW o WaR"""
    RAWSTRING = "******RAW******\n"
    WARSTRING = "******WAR******\n"
    RARSTRING = "******RAR******\n"
    for x in range(1,len(matriz)):

        if (matriz[x-1]["Continente"] in matriz[x]["Ejecutor"]):
            RAWSTRING +="I" + str(x-1) + "--->" +"I" + str(x) +"\n"
        if (matriz[x]["Continente"] in matriz[x-1]["Ejecutor"]):
            WARSTRING +="I"+ str(x-1) + "--->" + "I" + str(x) +"\n"
        if (matriz[x]["Continente"] == matriz[x-1]["Continente"]):
            RARSTRING += "I"+str(x-1) + "--->" + "I" +str(x) +"\n"
        
    print(RARSTRING)
    print(RAWSTRING)
    print(WARSTRING)

def memory_function(linea):
    """Funcion que, dada una instruccion de acceso a memoria, devuelve los parametros en el orden estimado."""
    spliteado = linea.split(",")
    header = spliteado[0].split(" ")
    accion = header[0]
    var1 = header[1]
    var2 = spliteado[1][1:]
    return accion,var1,var2

def arith_function(linea):
    """Funcion que, dada una instruccion arithmetica, devuelve los parametros en el orden estimado."""
    spliteado = linea.split(",")
    header = spliteado[0].split(" ")
    accion = header[0]
    var1 = header[1]
    var2 = spliteado[1][1:]
    var3 = spliteado[2][1:]
    return accion,var1,var2,var3

def printear(matriz):
    """Funcion para mostrar la matriz."""
    constant = "                "
    total = len(matriz[-1]["Pipeline"])
    for x in range(total):
        ciclo = "C" + str(x+1)
        constant = constant + ciclo + "\t"
        longitud = len(constant)
    constant += "\n"
    for y in matriz:
        instruccion = y["Accion"] + " " + y["Continente"] 
        for x in y["Ejecutor"]:
            instruccion += " , "+ x
        constant += instruccion
        constant += "\t"
        for z in y["Pipeline"]:
            constant += z + "\t"
        constant += "\n"

    print(constant)
    
if __name__ == "__main__":
    RWEXCEPTIONS = ""
    set_basics()
    parser(a)
    print(RWEXCEPTIONS)