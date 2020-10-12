from grafo_adj_nao_dir import *
import copy
# g_p     = Grafo([ 'A','B','C','D','E','F'])
#
#
#
# g_p.adicionaAresta('A-B')
#
# g_p.adicionaAresta('B-C')
# g_p.adicionaAresta('A-C')
# g_p.adicionaAresta('D-E')
# g_p.adicionaAresta('E-F')
# g_p.adicionaAresta('F-D')
# g_p.adicionaAresta('A-D')
# g_p     = Grafo([ 'A','B','C','D'])
#
#
#
# g_p.adicionaAresta('A-B')
#
# g_p.adicionaAresta('B-C')
# g_p.adicionaAresta('D-C')
# g_p.adicionaAresta('D-B')
# g_p     = Grafo([ 'A','B','C','D'])
#
#
#
# g_p.adicionaAresta('A-B')
#
# g_p.adicionaAresta('B-C')
# g_p.adicionaAresta('D-C')
# g_p.adicionaAresta('D-A')
g_p = Grafo(['D','C', 'A', 'F', 'E', 'H', 'G','B'])

g_p.adicionaAresta('D-G')
g_p.adicionaAresta('B-G')
g_p.adicionaAresta('E-B')
g_p.adicionaAresta('C-E')
g_p.adicionaAresta('D-A')
g_p.adicionaAresta('D-C')
g_p.adicionaAresta('D-F')
g_p.adicionaAresta('A-C')
g_p.adicionaAresta('C-F')
g_p.adicionaAresta('E-G')
g_p.adicionaAresta('E-H')
g_p.adicionaAresta('H-G')














#
# copia = copy.deepcopy(g_p)
#
# copia.remove_aresta('C-B')
# Nanterior= copy.deepcopy(copia.N)
#
# copia.N.pop(2)
# print(Nanterior)
# copia.RemoveDaMatriz('C',Nanterior)
#
# copia.remove_aresta('C-B')
# copia.N.pop(1)
# Nanterior= ['B','C']
# copia.RemoveDaMatriz('C',Nanterior)
print(g_p.PrintCaminhoEuleriano())

# def RemoveDaMatriz(v,x):
#     listaremove = []
#     for vert in range(len(copia.N)):
#         if x[vert] == v:
#             verticev = vert
#
#     for j in range(len(copia.N)):
#         for i in range(len(copia.N)):
#             if j== verticev :
#                 listaremove.append(copia.M[j])
#     copia.M.remove(listaremove[0])
#     for j in range(len(copia.N)):
#         copia.M[j].pop(verticev)
# RemoveDaMatriz("A",g_p.N)
# print(copia)
# print(copia.conexo())


# print(copia.M)
#
# # print(copia.N,copia.M)
#
# print(copia)
# # print(copia2.N)
# print(copia.conexo())







#
#
#
# def caminho(x,y,Vpercorridos=None):
#
#     verticex = 0
#     verticey = 0
#     lista = []
#     if Vpercorridos is None:
#         Vpercorridos = []
#     '''Atraves de um for conseguimos um indice equivalente ao vertice analizado, transformamos o x como coluna e o y sendo linha '''
#     for vert in range(len(g_p.N)):
#         if g_p.N[vert] == x:
#             verticex = vert
#         if g_p.N[vert] == y:
#             verticey = vert
#
#     '''Adicionamos o vertice X na lista Vpercorridos'''
#     Vpercorridos.append(verticex)
#     '''Para analizar a matriz a coluna necessita ser maior que a linha devido a ser um grafo nao direcionado, logo, fizemos um 'if'
#     para verificar se ha uma aresta ligando os vertices analizados, caso haja retornamos True'''
#     if verticex > verticey:
#         if g_p.M[verticey][verticex] > 0 :
#             return True
#     if verticex < verticey:
#         if g_p.M[verticex][verticey] > 0 :
#             return True
#     '''Em seguida procuramos outras arestas ligadas ao vertice X, caso haja, chamamos a função novamente substituindo o X pelo
#     o vertice a ele ligado '''
#
#     for j in range(len(g_p.M)):
#         for i in range(len(g_p.M)):
#             if (i not in Vpercorridos) and (j == verticex):
#
#                 resultado = caminho(g_p.N[i],y,Vpercorridos)
#                 '''E em seguida adicionamos o resultado em uma lista'''
#                 lista.append(resultado)
#             if (j not in Vpercorridos) and (i == verticex):
#                 resultado = caminho(g_p.N[j], y, Vpercorridos)
#                 lista.append(resultado)
#
#     '''Analisamos aqui se existe ao menos um True dentro da lista, se sim, é porque há um caminho entre os vértices analisados.'''
#
#     for x in lista:
#         if(x):
#
#             return True
#
#
#     return False
#
# def conexo():
#     '''Percorremos a lista dos vertices analizando se ha um caminho entre eles
#     caso nao haja entre algum para de vertice retornamos False'''
#
#     for x in range(len(g_p.N)):
#         for y in range(len(g_p.N)):
#             if x != y :
#                 resultado = caminho(g_p.N[x],g_p.N[y])
#                 if resultado == False:
#                     return False
#
#     return True
#
#
# def grau(vertice):
#     cont = 0
#     ''' Primeiro transformamos o vertice informado em letra maiuscula para manter um padrao.'''
#     vertice = vertice.upper()
#     '''Em seguida encontramos o indice do vertice analizado na matriz'''
#     for x in range(len(g_p.N)):
#         if g_p.N[x] == vertice:
#             vertice = x
#
#     for j in range(len(g_p.M)):
#         for i in range(len(g_p.M)):
#             '''Se quando percorrida a matriz for encontrado uma aresta ligada ao vertice analizado adicionamos ao contador'''
#             if (i == vertice or j == vertice) and j <= i and g_p.M[j][i] != 0:
#                 cont += g_p.M[j][i]
#
#     return cont
#
# def HaCaminhoEuleriano():
#     impar = 0
#     if conexo() == False:
#         return False
#     for x in g_p.N:
#         if grau(x) % 2 != 0 :
#             impar += 1
#     if impar == 0 or impar == 2:
#         return True
#     else:
#         return False
#
# def Impar_Par():
#     Impares = []
#     for x in g_p.N:
#         if grau(x) % 2 != 0:
#             Impares.append(x)
#     if len(Impares) == 0:
#         return False
#     return Impares
#
# def CountArestas():
#     cont = 0
#     for j in range(g_p.N):
#         for i in range(g_p.N):
#             if (j <= i) and (g_p.M[j][i] > 0):
#                 cont += g_p.M[j][i]
#
#     return cont


def PrintCaminhoEuleriano(self):
    if self.HaCaminhoEuleriano():
        Caminho = []
        CopiaGrafo = Grafo(self.N, self.M)
        print(CopiaGrafo)
        VerticeRaiz = ''


        if self.Impar_Par() != False:
            VerticeRaiz = self.Impar_Par()[0]
        for vert in range(len(CopiaGrafo.N)):
            if self.N[vert] == VerticeRaiz:
                VerticeRaiz2 = vert
        while len(Caminho) != self.CountArestas():
            if self.Impar_Par() != False:
                cont = 0

                print(VerticeRaiz2, "vetice 2")

                for j in range(len(CopiaGrafo.N)):

                    for vert in range(len(CopiaGrafo.N)):
                        if CopiaGrafo.N[vert] == VerticeRaiz:
                            VerticeRaiz2 = vert
                    print(VerticeRaiz2, "vetice 2 no for")

                    for i in range(len(CopiaGrafo.N)):
                        if (j <= i) and (j == VerticeRaiz2 or i == VerticeRaiz2) and (CopiaGrafo.M[j][i] > 0):
                            if (j == VerticeRaiz2):
                                print("if j ==")
                                Caminho.append(CopiaGrafo.N[i] + "-" + CopiaGrafo.N[j])
                                CopiaGrafo.remove_aresta(CopiaGrafo.N[i] + "-" + CopiaGrafo.N[j])
                                if self.grau(CopiaGrafo.N[j]) == 0:

                                    VerticeRaiz = CopiaGrafo.N[i]
                                    print('remove --', CopiaGrafo.N[j])
                                    CopiaGrafo.N.pop(j)

                                    cont += 1
                                    break

                                elif CopiaGrafo.conexo():
                                    VerticeRaiz = CopiaGrafo.N[i]
                                    cont += 1
                                    break
                                else:
                                    Caminho.pop(-1)
                                    CopiaGrafo.adicionaAresta(CopiaGrafo.N[i] + "-" + CopiaGrafo.N[j])

                    if cont > 1:
                        print('entrou no break')
                        break

                    for j in range(len(CopiaGrafo.N)):

                        for vert in range(len(CopiaGrafo.N)):
                            if CopiaGrafo.N[vert] == VerticeRaiz:
                                VerticeRaiz2 = vert
                        print(VerticeRaiz2, "vetice 2 no for")
                        if (i == VerticeRaiz2):
                            print("if i ==")
                            Caminho.append(CopiaGrafo.N[i] + "-" + CopiaGrafo.N[j])
                            CopiaGrafo.remove_aresta(CopiaGrafo.N[j] + "-" + CopiaGrafo.N[i])
                            if self.grau(CopiaGrafo.N[j]) == 0:
                                print(CopiaGrafo.N[j], CopiaGrafo.N[i])
                                print(CopiaGrafo.M)
                                VerticeRaiz = CopiaGrafo.N[j]
                                print(i, "remove esse")
                                CopiaGrafo.N.pop(i)
                                cont += 1
                                print("aq")
                                break
                            elif CopiaGrafo.conexo():
                                VerticeRaiz = CopiaGrafo.N[j]
                                cont += 1

                                break
                            else:
                                Caminho.pop(-1)
                                CopiaGrafo.adicionaAresta(CopiaGrafo.N[i] + "-" + CopiaGrafo.N[j])
                        if cont > 1:
                            print('entrou no break')
                            break


#
# for j in range(len(g_p.N)):
#     for i in range(len(g_p.N)):
#         if (j <= i) and (j == 0 or i == 0) and (g_p.M[j][i] > 0):
#             print(g_p.N[j],g_p.N[i])


