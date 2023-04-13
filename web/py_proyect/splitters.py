"""Funciones para separar las instrucciones dependiendo de que tipo sean"""

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