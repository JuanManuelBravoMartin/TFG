from python.utilities import *
from python.logica import *
from python.splitters import *


INSTRUCCIONES = ["add","addi", "sub", "mul", "div"]


def set_basics(ACCESO_ALU,ACCESO_ESCRITURA,ACCESO_DATOS,BASIC_WORK,BASIC_AR,BASIC_WRITE):

    """ Combina a informacion dada con los tipos de arrays, en favor de hacer la programacion mas facil"""
    if (ACCESO_DATOS !=1):
        for _ in range(ACCESO_DATOS -1):
            BASIC_WORK.insert(0,"IF")

    for x in BASIC_WORK:

        BASIC_AR.append(x)
        BASIC_WRITE.append(x)

    if (ACCESO_ESCRITURA != 1):
        i = BASIC_WRITE.index("M")
        for _ in range(ACCESO_ESCRITURA -1):
            BASIC_WRITE.insert(i,"M")

    if (ACCESO_ALU != 1):

        i = BASIC_AR.index("EX")
        for _ in range(ACCESO_ALU -1):
            BASIC_AR.insert(i,"EX")
    return


def parser (ACCESO_DATOS,BASIC_WORK,BASIC_AR,BASIC_WRITE,FW,programa):
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
                for _ in range(contador -1):
                    variable = ["-"] + variable
                diccionario = {"Accion": accion,"Continente": var2, "Ejecutor": [var1], "Pipeline": variable}
                matriz.append(diccionario.copy())

            elif (accion == "lw"):
                variable = BASIC_WRITE.copy()
                for _ in range(contador -1):
                    variable = ["-"] + variable
                diccionario = {"Accion": accion,"Continente": var1, "Ejecutor": [var2], "Pipeline": variable}
                matriz.append(diccionario.copy())

        elif (linea.split(" ")[0] in INSTRUCCIONES):
            variable = BASIC_AR.copy()
            for _ in range(contador - 1):
                variable = ["-"] + variable
            accion, var1, var2, var3 = arith_function(linea)
            diccionario = {"Accion": accion,"Continente": var1, "Ejecutor": [var2,var3], "Pipeline": variable}
            matriz.append(diccionario.copy())
        else:
            raise Exception("Por favor, introduce un codigo ensamblador valido")
        contador += ACCESO_DATOS

    rar,raw,war=checktodosproblemas(matriz,FW)
    
    html = html_matriz(matriz)
    return html,rar,raw,war


def main(programa,FW,AD = 1,AS = 1,ALU=1):

    try:
        ACCESO_DATOS = int(AD) ###### CICLOS DE ACCESO A LA MEMORIA DE DATOS ######
    except:
        ACCESO_DATOS = 1

    try:
        ACCESO_ESCRITURA = int(AS) ###### CICLOS DE ACCESO A LA MEMORIA DE DATOS ######
    except:
        ACCESO_ESCRITURA = 1

    try:
        ACCESO_ALU = int(ALU) ###### CICLOS DE OPERACIONES ALU ######
    except:
        ACCESO_ALU = 1
    BASIC_WORK = ["IF","ID","EX","M","WB"]
    BASIC_AR = []
    BASIC_WRITE = []
    
    set_basics(ACCESO_ALU,ACCESO_ESCRITURA,ACCESO_DATOS,BASIC_WORK,BASIC_AR,BASIC_WRITE)
    
    return parser(ACCESO_DATOS,BASIC_WORK,BASIC_AR,BASIC_WRITE,FW,programa)

if __name__ == "__main__":
    
    a = """sw a , a(222)
sw a , a
add a, a, b """
    main(a)
