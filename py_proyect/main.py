a = """sw a , a(222)
sw a , b(222)
add a, a, b """

BASIC_WORK = ["IF","ID","EX","M","WB"]
BASIC_READ = []
BASIC_WRITE = []

WB = True
ACCESO_DATOS = 2
ACCESO_ESCRITURA = 5
ACCESO_LECTURA = 1

def set_basics():
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
    check_consistency(matriz)
    printear(matriz)


def check_consistency(matriz):
    for x in range(1,len(matriz)):
        anterior = matriz[x-1]["Pipeline"]
        siguiente = matriz[x]["Pipeline"]
        for j in range(len(anterior)):
            try:
                if anterior[j] == "-":
                    print("AAA")
                    for i in range(j,0,-1):
                        if anterior[i] != "-":
                            print("BBB")
                            if siguiente[i] == anterior[i]:
                                anterior.insert(i,"-")
                        break
                if anterior[j] == siguiente[j]:
                    siguiente.insert(j, "-")

            except:
                break

def memory_function(linea):
    spliteado = linea.split(",")
    header = spliteado[0].split(" ")
    accion = header[0]
    var1 = header[1]
    var2 = spliteado[1][1:]
    return accion,var1,var2

def arith_function(linea):
    spliteado = linea.split(",")
    header = spliteado[0].split(" ")
    accion = header[0]
    var1 = header[1]
    var2 = spliteado[1][1:]
    var3 = spliteado[2][1:]
    return accion,var1,var2,var3

def printear(matriz):
    constant = "                "
    total = len(matriz[-1]["Pipeline"])
    for x in range(total):
        ciclo = "C" + str(x +1)
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
    


set_basics()
parser(a)