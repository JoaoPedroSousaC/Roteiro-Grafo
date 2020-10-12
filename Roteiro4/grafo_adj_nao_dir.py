# -*- coding: utf-8 -*-
import copy
'''--------------------JOAO VICTOR SILVA -----------JOAO PEDRO SOUSA---------------------------'''
class VerticeInvalidoException(Exception):
    pass

class ArestaInvalidaException(Exception):
    pass

class MatrizInvalidaException(Exception):
    pass

class Grafo:

    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'
    __maior_vertice = 0

    def __init__(self, V=None, M=None):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param V: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um inteiro que indica a quantidade de arestas que ligam aqueles vértices
        '''

        if V == None:
            V = list()
        if M == None:
            M = list()

        for v in V:
            if not(Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

        self.N = list(V)

        if M == []:
            for k in range(len(V)):
                M.append(list())
                for l in range(len(V)):
                    if k>l:
                        M[k].append('-')
                    else:
                        M[k].append(0)


        if len(M) != len(V):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(V):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(V)):
            for j in range(len(V)):
                '''
                Verifica se os índices passados como parâmetro representam um elemento da matriz abaixo da diagonal principal.
                Além disso, verifica se o referido elemento é um traço "-". Isso indica que a matriz é não direcionada e foi construída corretamente.
                '''
                if i>j and not(M[i][j] == '-'):
                    raise MatrizInvalidaException('A matriz não representa uma matriz não direcionada')


                aresta = V[i] + Grafo.SEPARADOR_ARESTA + V[j]
                if not(self.arestaValida(aresta)):
                    raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida')

        self.M = list(M)

    def arestaValida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        if not(self.existeVertice(aresta[:i_traco])) or not(self.existeVertice(aresta[i_traco+1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def __primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice X
        :param a: a aresta a ser analisada
        :return: O primeiro vértice da aresta
        '''
        return a[0:a.index(Grafo.SEPARADOR_ARESTA)]

    def __segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice Y
        :param a: A aresta a ser analisada
        :return: O segundo vértice da aresta
        '''
        return a[a.index(Grafo.SEPARADOR_ARESTA)+1:]

    def __indice_primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice X na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do primeiro vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__primeiro_vertice_aresta(a))

    def __indice_segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice Y na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do segundo vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__segundo_vertice_aresta(a))

    def existeAresta(self, a: str):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, a):
            for i in range(len(self.M)):
                for j in range(len(self.M)):
                    if self.M[self.__indice_primeiro_vertice_aresta(a)][self.__indice_segundo_vertice_aresta(a)]:
                        existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Inclui um vértice no grafo se ele estiver no formato correto.
        :param v: O vértice a ser incluído no grafo.
        :raises VerticeInvalidoException se o vértice já existe ou se ele não estiver no formato válido.
        '''
        if v in self.N:
            raise VerticeInvalidoException('O vértice {} já existe'.format(v))

        if self.verticeValido(v):
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

            self.N.append(v) # Adiciona vértice na lista de vértices
            self.M.append([]) # Adiciona a linha

            for k in range(len(self.N)):
                if k != len(self.N) -1:
                    self.M[k].append(0) # adiciona os elementos da coluna do vértice
                    self.M[self.N.index(v)].append('-') # adiciona os elementos da linha do vértice
                else:
                    self.M[self.N.index(v)].append(0)  # adiciona um zero no último elemento da linha
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, a):
        '''
        Adiciona uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.arestaValida(a):
            i_a1 = self.__indice_primeiro_vertice_aresta(a)
            i_a2 = self.__indice_segundo_vertice_aresta(a)
            if i_a1 < i_a2:
                self.M[i_a1][i_a2] += 1
            else:
                self.M[i_a2][i_a1] += 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def remove_aresta(self, a):
        '''
        Remove uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.arestaValida(a):
            if self.existeAresta(a):
                i_a1 = self.__indice_primeiro_vertice_aresta(a)
                i_a2 = self.__indice_segundo_vertice_aresta(a)
                if i_a1 < i_a2:
                    self.M[i_a1][i_a2] -= 1
                else:
                    self.M[i_a2][i_a1] -= 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''

        # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice
        espaco = ' '*(self.__maior_vertice)

        grafo_str = espaco + ' '

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for l in range(len(self.M)):
            grafo_str += self.N[l] + ' '
            for c in range(len(self.M)):
                grafo_str += str(self.M[l][c]) + ' '
            grafo_str += '\n'

        return grafo_str



    #------------------------

    def caminho(self, x, y, Vpercorridos=None):

        verticex = 0
        verticey = 0
        lista = []
        if Vpercorridos is None:
            Vpercorridos = []
        '''Atraves de um for conseguimos um indice equivalente ao vertice analizado, transformamos o x como coluna e o y sendo linha '''
        for vert in range(len(self.N)):
            if self.N[vert] == x:
                verticex = vert
            if self.N[vert] == y:
                verticey = vert

        '''Adicionamos o vertice X na lista Vpercorridos'''
        Vpercorridos.append(verticex)
        '''Para analizar a matriz a coluna necessita ser maior que a linha devido a ser um grafo nao direcionado, logo, fizemos um 'if' 
        para verificar se ha uma aresta ligando os vertices analizados, caso haja retornamos True'''
        if verticex > verticey:
            if self.M[verticey][verticex] > 0   :
                return True
        if verticex < verticey:
            if self.M[verticex][verticey] > 0:
                return True
        '''Em seguida procuramos outras arestas ligadas ao vertice X, caso haja, chamamos a função novamente substituindo o X pelo
        o vertice a ele ligado '''

        for j in range(len(self.M)):
            for i in range(len(self.M)):

                if (i not in Vpercorridos) and (j == verticex) and (self.M[j][i] != '-'):
                    if (self.M[j][i] > 0):
                        resultado = self.caminho(self.N[i], y, Vpercorridos)
                        '''E em seguida adicionamos o resultado em uma lista'''
                        lista.append(resultado)
                if (j not in Vpercorridos) and (i == verticex) and (self.M[j][i] != '-'):
                    if (self.M[j][i] > 0):
                        resultado = self.caminho(self.N[j], y, Vpercorridos)
                        lista.append(resultado)

        '''Analisamos aqui se existe ao menos um True dentro da lista, se sim, é porque há um caminho entre os vértices analisados.'''

        for x in lista:
            if (x):
                return True

        return False

    def conexo(self):
        '''Percorremos a lista dos vertices analizando se ha um caminho entre eles
        caso nao haja entre algum para de vertice retornamos False'''

        for x in range(len(self.N)):
            for y in range(len(self.N)):
                if x != y:
                    resultado = self.caminho(self.N[x], self.N[y])
                    if resultado == False:
                        return False

        return True

    def grau(self,vertice):
        cont = 0
        ''' Primeiro transformamos o vertice informado em letra maiuscula para manter um padrao.'''
        vertice = vertice.upper()
        '''Em seguida encontramos o indice do vertice analizado na matriz'''
        for x in range(len(self.N)):
            if self.N[x] == vertice:
                vertice = x

        for j in range(len(self.M)):
            for i in range(len(self.M)):
                '''Se quando percorrida a matriz for encontrado uma aresta ligada ao vertice analizado adicionamos ao contador'''
                if (i == vertice or j == vertice) and j <= i and self.M[j][i] != 0:
                    cont += self.M[j][i]

        return cont

    def HaCaminhoEuleriano(self):
        impar = 0
        if self.conexo() == False:
            return False
        for x in self.N:
            if self.grau(x) % 2 != 0:
                impar += 1
        if impar == 0 or impar == 2:
            return True
        else:
            return False

    def Impar_Par(self):
        Impares = []
        for x in self.N:
            if self.grau(x) % 2 != 0:
                Impares.append(x)
        if len(Impares) == 0:
            return False
        return Impares

    def CountArestas(self):
        cont = 0
        for j in range(len(self.N)):
            for i in range(len(self.N)):
                if (j <= i) and (self.M[j][i] > 0):
                    cont += self.M[j][i]

        return cont

    def RemoveDaMatriz(self,v,x):
        listaremove = []
        for vert in range(len(x)):
            if x[vert] == v:
                verticev = vert

        for j in range(len(x)):
            for i in range(len(x)):
                if j == verticev:
                    listaremove.append(self.M[j])
        self.M.remove(listaremove[0])
        for j in range(len(self.N)):
            self.M[j].pop(verticev)

    def Is_Ponte(self,j,i,arestas = []):
        ''' J e I É INDICE'''
        GrafoCopia = copy.deepcopy(self)
        arestas.append(GrafoCopia.N[j] + "-" + GrafoCopia.N[i])
        GrafoCopia.remove_aresta(GrafoCopia.N[j] + "-" + GrafoCopia.N[i])
        Nanterior = copy.deepcopy(GrafoCopia.N)
        if GrafoCopia.grau(GrafoCopia.N[j]) == 0:
            vertice = GrafoCopia.N[j]
            Nanterior = copy.deepcopy(GrafoCopia.N)
            GrafoCopia.N.pop(j)
            GrafoCopia.RemoveDaMatriz(vertice,Nanterior)



        if GrafoCopia.grau(Nanterior[i]) == 0 and len(arestas) == self.CountArestas():

            return False
        if GrafoCopia.grau(Nanterior[i]) == 0 and len(arestas) != self.CountArestas():


            return True
        if GrafoCopia.grau(Nanterior[i]) != 0 and GrafoCopia.conexo():

            return False


        return True

    def PrintCaminhoEuleriano(self):
        if self.HaCaminhoEuleriano():
            Caminho = []
            CopiaGrafo = copy.deepcopy(self)

            VerticeRaiz = self.N[0]

            if self.Impar_Par() != False:
                VerticeRaiz = self.Impar_Par()[0]

            for vert in range(len(CopiaGrafo.N)):
                if self.N[vert] == VerticeRaiz:
                    VerticeRaiz2 = vert
            countAresta = self.CountArestas()

            while countAresta != len(Caminho):
                NanteriorFor = copy.deepcopy(CopiaGrafo.N)
                contBreak = 0


                for vert in range(len(CopiaGrafo.N)):
                    if CopiaGrafo.N[vert] == VerticeRaiz:
                        VerticeRaiz2 = vert


                for j in range(len(CopiaGrafo.N)):
                    for i in range(len(CopiaGrafo.N)):
                        if j == VerticeRaiz2:
                            if (CopiaGrafo.M[j][i]!='-') and (CopiaGrafo.M[j][i]>0):
                                if CopiaGrafo.Is_Ponte(j,i,Caminho) == False:
                                    # Caminho.append(CopiaGrafo.N[j] + '-' + CopiaGrafo.N[i])
                                    CopiaGrafo.remove_aresta(CopiaGrafo.N[j] + '-' + CopiaGrafo.N[i])
                                    if CopiaGrafo.grau(CopiaGrafo.N[j]) == 0:

                                        CopiaGrafo.N.pop(j)
                                        CopiaGrafo.RemoveDaMatriz(NanteriorFor[j],NanteriorFor)
                                    contBreak += 1
                                    VerticeRaiz = NanteriorFor[i]
                                    break

                                else:
                                    if (CopiaGrafo.grau(NanteriorFor[i])==1):
                                        break
                                    Caminho.pop(-1)
                                    break

                        if i == VerticeRaiz2:
                            if (CopiaGrafo.M[j][i]!='-') and (CopiaGrafo.M[j][i]>0):
                                resultado = CopiaGrafo.Is_Ponte(i,j,Caminho)
                                if  resultado == False:


                                    # Caminho.append(CopiaGrafo.N[i] + '-' + CopiaGrafo.N[j])
                                    CopiaGrafo.remove_aresta(CopiaGrafo.N[j] + '-' + CopiaGrafo.N[i])
                                    if CopiaGrafo.grau(CopiaGrafo.N[i]) == 0:
                                        CopiaGrafo.N.pop(i)
                                        CopiaGrafo.RemoveDaMatriz(NanteriorFor[i],NanteriorFor)
                                    contBreak += 1
                                    VerticeRaiz = NanteriorFor[j]
                                    break

                                else:


                                    if (CopiaGrafo.grau(NanteriorFor[j])==1):
                                        break
                                    Caminho.pop(-1)
                                    break



                    if contBreak >= 1:
                        break






            return Caminho




















