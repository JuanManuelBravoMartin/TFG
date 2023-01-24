a = """sw a , a(222)
sw a , b(222)
add a, a, b """
BASIC_WORK = ["IF","ID","EX","M","WB"]


def parser (programa):

    contador = 0
    matriz = []
    partido = programa.split("\n")
    for linea in partido:
        variable = BASIC_WORK.copy()
        for _ in range(contador):
            variable = ["-"] + variable
        if (linea.split(" ")[0] == "sw" or linea.split(" ")[0] == "lw"):
            accion, var1, var2 = memory_function(linea)
            matriz.append([[accion,var1,var2],variable])
        elif (linea.split(" ")[0] == "add"):
            accion, var1, var2, var3 = arith_function(linea)
            matriz.append([[accion,var1,var2,var3],variable])
        contador += 1
    printear(matriz)
    print (matriz)

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
    total = len(matriz[-1][1])
    for x in range(total):
        ciclo = "C" + str(x +1)
        constant = constant + ciclo + "\t"
        longitud = len(constant)
    constant += "\n"
    for y in matriz:
        instruccion = y[0][0] + " " + y[0][1] +" , "+y[0][2]
        constant += instruccion
        constant += "\t"
        for z in y[1]:
            constant += z + "\t"
        constant += "\n"

    print(constant)
    



parser(a)