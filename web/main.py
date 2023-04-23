from utilities import *
from logica import *
from splitters import *




ACCESO_DATOS = 2 
ACCESO_ESCRITURA = 5 ###### CICLOS DE ACCESO A LA ESCRITURA DE DATOS ######
ACCESO_LECTURA = 1 ###### CICLOS DE ACCESO A LA LECTURA DE DATOS ######
RWEXCEPTIONS = " "

def set_basics(ACCESO_DATOS,BASIC_WORK,BASIC_READ,BASIC_WRITE):
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
    return


def parser (BASIC_WORK,BASIC_READ,BASIC_WRITE,programa):
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
                diccionario = {"Accion": accion,"Continente": var1, "Ejecutor": [var2], "Pipeline": variable}
                matriz.append(diccionario.copy())
            elif (accion == "lw"):
                variable = BASIC_WORK.copy()
                for _ in range(contador -1):
                    variable = ["-"] + variable
                diccionario = {"Accion": accion,"Continente": var1, "Ejecutor": [var2], "Pipeline": variable}
                matriz.append(diccionario.copy())
        elif (linea.split(" ")[0] == "add"):
            variable = BASIC_WORK.copy()
            for _ in range(contador -1):
                variable = ["-"] + variable
            accion, var1, var2, var3 = arith_function(linea)
            diccionario = {"Accion": accion,"Continente": var1, "Ejecutor": [var2,var3], "Pipeline": variable}
            matriz.append(diccionario.copy())
        contador += ACCESO_DATOS

    rar,raw,war=checktodosproblemas(matriz)
    
    html = html_matriz(matriz)
    return html,rar,raw,war


def main(WBH,AD,prgrama):
    WB = bool(WBH)
    try:
        ACCESO_DATOS = int(AD) ###### CICLOS DE ACCESO A LA MEMORIA DE DATOS ######
    except:
        ACCESO_DATOS = 1
    BASIC_WORK = ["IF","ID","EX","M","WB"]
    BASIC_READ = []
    BASIC_WRITE = []
    set_basics(ACCESO_DATOS,BASIC_WORK,BASIC_READ,BASIC_WRITE)
    
    return parser(BASIC_WORK,BASIC_READ,BASIC_WRITE,prgrama)

if __name__ == "__main__":
    
    a = """sw a , a(222)
sw a , a
add a, a, b """
    main(a)
