from utilities import *

def checktodosproblemas(matriz):
    base = ["IF","ID","EX","M","WB"]
    RAWSTRING = "******RAW******\n"
    WARSTRING = "******WAR******\n"
    RARSTRING = "******RAR******\n"
    for x in range(1,len(matriz)):

        anterior = matriz[x-1]["Pipeline"].copy()
        siguiente = matriz[x]["Pipeline"].copy()

        for palabra in base:
            # print(i)



            indice_anterior = lastindex(anterior,palabra)
            indice_siguiente = firstindex(siguiente,palabra)
            dif = indice_anterior - indice_siguiente


            if (palabra == "EX"):

                for y in range(x):

                    iteracion = matriz[x-1]["Pipeline"].copy()
                    # print(y)
                    if (matriz[y]["Continente"] in matriz[x]["Ejecutor"]):

                        if(lastindex(iteracion,"WB") >= firstindex(matriz[x]["Pipeline"],"EX")):

                            while(lastindex(iteracion,"WB") >= firstindex(siguiente,"EX")):

                                siguiente.insert(firstindex(siguiente,"EX"),"-")

                        RAWSTRING +="I" + str(y) + "--->" + "I" + str(x) +"\n"

                    if (matriz[x]["Continente"] in matriz[y]["Ejecutor"]):

                        WARSTRING +="I"+ str(y) + "--->" + "I" + str(x) + "\n"

                    if (matriz[x]["Continente"] == matriz[y]["Continente"]):

                        RARSTRING += "I"+str(y) + "--->" + "I" +str(x) +"\n"

            if dif >= 0:

                for palabra in range(dif+1):

                    siguiente.insert(indice_siguiente,"-")

            matriz[x-1]["Pipeline"] = anterior.copy()
            matriz[x]["Pipeline"] = siguiente.copy()

    print(RARSTRING)
    print(RAWSTRING)
    print(WARSTRING)