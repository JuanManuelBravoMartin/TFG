from python.utilities import *
INSTRUCCIONES = ["add", "sub", "mul", "div"]
def checktodosproblemas(matriz,FW):

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

                    if (FW == False):

                        if ((matriz[y]["Continente"] in matriz[x]["Ejecutor"]) and (lastindex(iteracion,"WB") >= firstindex(siguiente,"EX"))):

                            while(lastindex(iteracion,"WB") >= firstindex(siguiente,"EX")):

                                siguiente.insert(firstindex(siguiente,"EX"),"-")

                            RAWSTRING += "<tr><th>I" + str(y) + "--->" + "I" + str(x) +"</th></tr>\n"
                    elif (FW == True):

                        if(matriz[y]["Accion"] in INSTRUCCIONES):
                            
                            if ((matriz[y]["Continente"] in matriz[x]["Ejecutor"]) and (lastindex(iteracion,"EX") >= firstindex(siguiente,"EX"))):

                                while(lastindex(iteracion,"EX") >= firstindex(siguiente,"EX")):

                                    siguiente.insert(firstindex(siguiente,"EX"),"-")

                                RAWSTRING += "<tr><th>I" + str(y) + "--->" + "I" + str(x) +"</th></tr>\n"
                        else:
                            if ((matriz[y]["Continente"] in matriz[x]["Ejecutor"]) and (lastindex(iteracion,"M") >= firstindex(siguiente,"EX"))):

                                while(lastindex(iteracion,"M") >= firstindex(siguiente,"EX")):

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
                siguiente.insert(indice_siguiente,"-")
                for _ in range(dif):

                    siguiente.insert(indice_siguiente,"-")

            matriz[x-1]["Pipeline"] = anterior.copy()
            matriz[x]["Pipeline"] = siguiente.copy()
    WAWSTRING += "</table>"
    RAWSTRING += "</table>"
    WARSTRING += "</table>"
    return WAWSTRING,RAWSTRING,WARSTRING