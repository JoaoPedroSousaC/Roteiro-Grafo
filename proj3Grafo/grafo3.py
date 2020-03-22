from grafo import *

g_p  =  Grafo(['J', 'C', 'E', 'P'], {'a1':'J-C', 'a3':'E-J', 'a4':'J-P', 'a6':'E-C', 'a7':'C-P', 'a8':'P-E'})
def Ciclo():
    listaremove = []
    ciclo = []
    arestaVisitada = []
    aparicao = 0
    while True:
        cont = 0
        for nomeAresta , aresta in g_p.A.items():

            if(aresta[0] == aresta[2]):
                return (aresta[0], nomeAresta, aresta[0])

            if ((g_p.grau(aresta[0])<= 1 or g_p.grau(aresta[2])<= 1 ) and aresta[0] != aresta[2] ):
                listaremove.append(nomeAresta)

                cont += 1



        for x in listaremove:
            del g_p.A[x]
        listaremove = []
        if (cont == 0):
            break
    while True:
        cont = 0
        for nomeAresta, aresta in g_p.A.items():

            if ((g_p.grau(aresta[0]) != 2 or g_p.grau(aresta[2]) != 2) and aresta[0] != aresta[2]):
                listaremove.append(nomeAresta)

                cont += 1
                break

        for x in listaremove:
            del g_p.A[x]
        listaremove = []
        if (cont == 0):
            break
    if (g_p.A == {}):
        return False
    else:
        main = ""
        olhar = ""
        while aparicao < 2:

            for nomeAresta, aresta in g_p.A.items():

                if aparicao == 0:
                    main = aresta[0]
                    aparicao += 1
                    ciclo.append(main)
                    ciclo.append(nomeAresta)
                    ciclo.append(aresta[2])
                    arestaVisitada.append(nomeAresta)
                    olhar = aresta[2]
                elif (olhar == aresta[2] and nomeAresta not in arestaVisitada ):
                    if aresta[0] == main:
                        aparicao += 1
                        ciclo.append(nomeAresta)
                        ciclo.append(main)

                        break
                    else:
                        olhar = aresta[0]
                        ciclo.append(nomeAresta)
                        ciclo.append(aresta[0])
                        arestaVisitada.append(nomeAresta)
                elif (olhar == aresta[0] and nomeAresta not in arestaVisitada):
                    if aresta[2] == main:
                        aparicao += 1
                        ciclo.append(nomeAresta)
                        ciclo.append(main)

                        break
                    else:
                        olhar = aresta[2]
                        ciclo.append(nomeAresta)
                        ciclo.append(aresta[2])
                        arestaVisitada.append(nomeAresta)



    return ciclo

print(Ciclo())