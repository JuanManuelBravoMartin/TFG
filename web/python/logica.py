from python.utilities import *

def checktodosproblemas(matriz):
    base = ["IF","ID","EX","M","WB"]
    RAWSTRING = "<table>\n<tr><th>RAW</th></tr>\n"
    WARSTRING = "<table>\n<tr><th>WAR</th></tr>\n"
    WAWSTRING = "<table>\n<tr><th>WAW</th></tr>\n"
    for x in range(1,len(matriz)):

        anterior = matriz[x-1]["Pipeline"].copy()
        siguiente = matriz[x]["Pipeline"].copy()


        for palabra in base:

            if (palabra == "EX"):

                for y in range(x):

                    iteracion = matriz[y]["Pipeline"].copy()

                    if ((matriz[y]["Continente"] in matriz[x]["Ejecutor"]) and (lastindex(iteracion,"WB") >= firstindex(siguiente,"EX"))):

                        while(lastindex(iteracion,"WB") >= firstindex(siguiente,"EX")):

                            siguiente.insert(firstindex(siguiente,"EX"),"-")

                        RAWSTRING += "<tr><th>I" + str(y) + "--->" + "I" + str(x) +"</th></tr>\n"

                    if (matriz[x]["Continente"] in matriz[y]["Ejecutor"]):

                        WARSTRING +="<tr><th>I" + str(y) + "--->" + "I" + str(x) +"</th></tr>\n"

                    if (matriz[x]["Continente"] == matriz[y]["Continente"]):

                        WAWSTRING += "<tr><th>I" + str(y) + "--->" + "I" + str(x) +"</th></tr>\n"

            indice_anterior = lastindex(anterior,palabra)
            indice_siguiente = firstindex(siguiente,palabra)
            dif = indice_anterior - indice_siguiente

            if dif >= 0:

                for _ in range(dif+1):

                    siguiente.insert(indice_siguiente,"-")

            matriz[x-1]["Pipeline"] = anterior.copy()
            matriz[x]["Pipeline"] = siguiente.copy()
    WAWSTRING += "</table>"
    RAWSTRING += "</table>"
    WARSTRING += "</table>"
    return WAWSTRING,RAWSTRING,WARSTRING