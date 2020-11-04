
# -*- coding: utf-8 -*-
import copy
import math
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
        '''Inicialmente verifiacamos se o grafo é conexo'''
        if self.conexo() == False:
            return False
        '''Verificamos quantos vertices impares há no grafo'''
        for x in self.N:
            if self.grau(x) % 2 != 0:
                impar += 1
        '''Caso a quantidade de impares seja 0 ou 2, retornamos true pois existe um caminho'''
        if impar == 0 or impar == 2:
            return True
        else:
            return False

    def Impar_Par(self):
        Impares = []
        '''Verificamos quais são os 2 vertices impares, e retornamos a lista contendo eles'''
        for x in self.N:
            if self.grau(x) % 2 != 0:
                Impares.append(x)
        if len(Impares) == 0:
            return False
        return Impares


    def CountArestas(self):
        cont = 0
        '''Contamos o numero de arestas existentes no grafo'''
        for j in range(len(self.N)):
            for i in range(len(self.N)):
                if (j <= i) and (self.M[j][i] > 0):
                    cont += self.M[j][i]

        return cont

    def RemoveDaMatriz(self,v,listavertices):
        '''Removemos de forma o vertice da matriz'''
        listaremove = []
        for vert in range(len(listavertices)):
            if listavertices[vert] == v:
                verticev = vert

        for j in range(len(listavertices)):
            for i in range(len(listavertices)):
                if j == verticev:
                    listaremove.append(self.M[j])
        self.M.remove(listaremove[0])
        for j in range(len(self.N)):
            self.M[j].pop(verticev)

    def Is_Ponte(self,vertice1,vertice2,arestas = []):
        '''Inicialmente criamos uma copia do grafo, para nela alterarmos'''
        GrafoCopia = copy.deepcopy(self)
        '''Adicionamos os pares de vertices na lista de arestas'''
        arestas.append(GrafoCopia.N[vertice1] + "-" + GrafoCopia.N[vertice2])
        '''Após isso removemos a aresta da copia do grafo'''
        GrafoCopia.remove_aresta(GrafoCopia.N[vertice1] + "-" + GrafoCopia.N[vertice2])
        '''Fazemos uma copia dos vertices do grafo'''
        Nanterior = copy.deepcopy(GrafoCopia.N)

        '''Caso o grau do vertice seja 0, removemos da matriz'''
        if GrafoCopia.grau(GrafoCopia.N[vertice1]) == 0:
            vertice = GrafoCopia.N[vertice1]
            GrafoCopia.N.pop(vertice1)
            GrafoCopia.RemoveDaMatriz(vertice,Nanterior)

        '''Verificamos se é a ultima aresta a ser pecorrida'''
        if GrafoCopia.grau(Nanterior[vertice2]) == 0 and len(arestas) == self.CountArestas():
            return False
        '''Verificamos se o vertice analisado possui grau 0 e não é a ultima aresta, caso seja, é uma ponte'''
        if GrafoCopia.grau(Nanterior[vertice2]) == 0 and len(arestas) != self.CountArestas():
            return True
        '''Verificamos se após a remoção da aresta o grafo continua conexo, se sim, a aresta analisada nao é ponte'''
        if GrafoCopia.grau(Nanterior[vertice2]) != 0 and GrafoCopia.conexo():
            return False

        return True


    def PrintCaminhoEuleriano(self):
        if len(self.N) <= 1:
            return "Não possui caminho euleriano"
        '''Vimos se no grafo há um caminho euleriano e continuamos a partir daí'''
        if self.HaCaminhoEuleriano():
            Caminho = []
            '''Criamos uma copia do grafo para fazer alterações'''
            CopiaGrafo = copy.deepcopy(self)
            '''Atribuimos ao "VerticeRaiz" um vertice, para começarmos a busca a partir dele'''
            VerticeRaiz = self.N[0]

            '''Verificamos se há 2 vertices com grau impar, ou todos os vertices são pares'''
            if self.Impar_Par() != False:
                VerticeRaiz = self.Impar_Par()[0]

            '''Fizemos um for pecorrendo o tamanho da lista de vertices do grafo, transformando o VerticeRaiz em índice'''
            for vert in range(len(CopiaGrafo.N)):
                if self.N[vert] == VerticeRaiz:
                    VerticeRaiz2 = vert

            countAresta = self.CountArestas()

            '''Criamos um while com uma condição de parada: Se a quantidade de arestas do grafo for igual
               a lista de Caminho, terminamos o programa retornando o Caminho pecorrido'''
            while countAresta != len(Caminho):
                NanteriorFor = copy.deepcopy(CopiaGrafo.N)
                contBreak = 0

                '''Transformamos o verticeraiz em índice'''
                for vert in range(len(CopiaGrafo.N)):
                    if CopiaGrafo.N[vert] == VerticeRaiz:
                        VerticeRaiz2 = vert

                '''Pecorremos a matriz com diversas condições'''
                for j in range(len(CopiaGrafo.N)):
                    for i in range(len(CopiaGrafo.N)):
                        if j == VerticeRaiz2:
                            '''Verificamos se há uma aresta entre os vertices analisados'''
                            if (CopiaGrafo.M[j][i]!='-') and (CopiaGrafo.M[j][i]>0):
                                '''verificamos se a aresta analisada não é uma ponte, então removemos da matriz'''
                                if CopiaGrafo.Is_Ponte(j,i,Caminho) == False:
                                    CopiaGrafo.remove_aresta(CopiaGrafo.N[j] + '-' + CopiaGrafo.N[i])
                                    '''Se o grau do vertice da aresta removida for 0, removemos o vertice da matriz'''
                                    if CopiaGrafo.grau(CopiaGrafo.N[j]) == 0:
                                        CopiaGrafo.N.pop(j)
                                        CopiaGrafo.RemoveDaMatriz(NanteriorFor[j],NanteriorFor)
                                    contBreak += 1
                                    '''Atualizamos o Vertice Raiz'''
                                    VerticeRaiz = NanteriorFor[i]
                                    break

                                else:
                                    '''Se for ponte e for o ultimo caminho damos um Break, se não for o ultimo
                                    removemos a aresta do caminho'''
                                    if (CopiaGrafo.grau(NanteriorFor[i])==1):
                                        break
                                    Caminho.pop(-1)
                                    break

                        if i == VerticeRaiz2:
                            if (CopiaGrafo.M[j][i]!='-') and (CopiaGrafo.M[j][i]>0):
                                resultado = CopiaGrafo.Is_Ponte(i,j,Caminho)
                                if  resultado == False:
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
        else:
            return "Não possui caminho euleriano"

    def VerticeLigados(self,vertice):
        '''Fizemos uma função verificando quais vertices são adjacentes ao vertice passado como parâmetro, e retornamos
        uma lista com eles'''
        verticesLigados = []
        for j in range(len(self.N)):
            for i in range(len(self.N)):
               if j <= i and (self.N[j] == vertice or self.N[i] == vertice) and self.M[j][i] > 0:
                   if self.N[j] == vertice:
                        verticesLigados.append(self.N[i])
                   else:
                        verticesLigados.append(self.N[j])

        return verticesLigados



    def Caminho_Hamiltoniano(self,size, vertice, lista=None):
        if lista is None:
            lista = []
        '''Se o vertice passado como parâmetro não estiver na lista, nós adicionamos'''
        if vertice not in set(lista):
            lista.append(vertice)
            '''Se o tamanho da lista for igual a quantidade de vertices, retornamos a lista'''
            if len(lista) == size:
                return lista
            TodosCaminhos = []
            '''Pecorremos os vertices adjacentes ao vertice passado como parâmetro'''
            for prox_vertice in self.VerticeLigados(vertice):
                res_lista = list(lista)
                caminhos = self.Caminho_Hamiltoniano(size,prox_vertice,res_lista)

                '''Se o caminho não for vazio, adicionamos o caminho em uma lista'''
                if caminhos is not None:
                    TodosCaminhos.extend(caminhos)
                else:
                    pass
            return TodosCaminhos
        else:
            return None

    def Ciclo_Hamiltoniano(self):
        Vertice = self.N[0]
        '''Adicionamos o resultado do "Caminho_Hamiltoniano" em um lista'''
        Lista =  self.Caminho_Hamiltoniano(len(self.N),Vertice)
        CaminhosOrganizado = []
        '''Em seguida organizamos o resultado da lista '''
        for j in range(len(self.N)):
            while j * len(self.N) < len(Lista):
                start = int(j * len(self.N))
                end = int((j + 1) * len(self.N))
                CaminhosOrganizado.append(Lista[start:end])
                break
        '''Verificamos se o primeiro vertice é adjacente ao ultimo, dos caminhos da lista'''
        for Caminhos in CaminhosOrganizado:
            if Vertice in self.VerticeLigados(Caminhos[-1]):
                return Caminhos

            else:
                return  False
        return False

    '''---------------------------------------------Roteiro-7--------------------------------------------------------------'''
    def Algoritmo_de_Dijkstra(self,verticePartida, verticeChegada, cargaIncial, cargaTotal, verticesRecarga = []):
        '''Fizemos o algoritmo padrao de Dijkstra e adicionamos um novo dicionario 'gama', nele contem a quantidade
         de carga em cada vertice. '''
        beta = {}
        fi = {}
        pi = {}
        gama = {}
        w = verticePartida
        PonteiroR = ''
        '''Fizemos um 'for' para poder preencher cada dicionario com seus respectivos valores'''
        for x in self.N:
            gama.update({x: 0})
            pi.update({x:0})
            if x == verticePartida:
                fi.update({x:1})
                beta.update({x:0})
            else:
                fi.update({x: 0})
                beta.update({x: math.inf})
        gama.update({verticePartida: cargaIncial})



        while(PonteiroR != verticeChegada):


            for verticeLigado in self.VerticeLigados(w):
                '''Esse primeiro 'if' é do algoritimo padrao...'''
                if (fi[verticeLigado] == 0 and (beta[verticeLigado]>beta[w] + 1)):
                    beta[verticeLigado] = beta[w] + 1
                    pi[verticeLigado] = w
                '''Nesses dois 'if' eu uso a logica que encontrei para o problema, verificamos se o proximos vertice 
                ligado ao vertice 'W' ele tem uma carga maior que o vertice 'W' e seu 'fi' é igual a zero, caso ele tenha,
                 alteramos  o seu 'pi' para 'W' e alteramos o seu valor de 'gama' para o 'gama' de 'w' - 1 '''
                if fi[verticeLigado] == 0 and gama[verticeLigado] < gama[w] - 1:
                    pi[verticeLigado] = w
                    gama[verticeLigado] = gama[w] - 1
                '''Logo em seguida verificamos se o vertice ligado ao 'w' é um vertice de recarga.'''
                if verticeLigado in verticesRecarga:
                    gama[verticeLigado] = cargaTotal


            '''Na minha logica, alterei como achar o 'R*', o 'R*' é a maior entre os 'gama' e que tem o 'fi' igual a zero'''
            maximo = 0
            PonteiroR = ''

            for x in self.N:
                if fi[x] == 0 and gama[x] > maximo :
                    maximo = gama[x]
                    PonteiroR = x

            if (verticeChegada in self.VerticeLigados(w)) and  PonteiroR == '':
                PonteiroR = verticeChegada

            if PonteiroR == '':
                return False

            fi[PonteiroR] = 1
            w = PonteiroR


        return self.printDijkstra(pi,verticeChegada)

    def printDijkstra(self,pi,verticeChegada):
        '''Fizemos um for onde vai pegando os antecessores e colocando em ordem'''
        lista = []
        lista.append(verticeChegada)

        for x in range(len(pi)):
            lista.append('->')
            lista.append(pi[verticeChegada])

            verticeChegada = pi[verticeChegada]
            if pi[verticeChegada] == 0:

                break
        a = ' '.join(lista[::-1])
        return a






g_z12 = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z','A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1'])
g_z12.adicionaAresta('A-B')
g_z12.adicionaAresta('A-C')
g_z12.adicionaAresta('A-D')
g_z12.adicionaAresta('B-E')
g_z12.adicionaAresta('B-I')
g_z12.adicionaAresta('B-F')
g_z12.adicionaAresta('C-G')
g_z12.adicionaAresta('C-D')
g_z12.adicionaAresta('D-H')
g_z12.adicionaAresta('E-F')
g_z12.adicionaAresta('F-J')
g_z12.adicionaAresta('F-G')
g_z12.adicionaAresta('H-L')
g_z12.adicionaAresta('H-G')
g_z12.adicionaAresta('I-M')
g_z12.adicionaAresta('I-J')
g_z12.adicionaAresta('J-N')
g_z12.adicionaAresta('K-O')
g_z12.adicionaAresta('L-P')
g_z12.adicionaAresta('M-Q')
g_z12.adicionaAresta('M-S')
g_z12.adicionaAresta('N-R')
g_z12.adicionaAresta('N-S')
g_z12.adicionaAresta('N-T')
g_z12.adicionaAresta('O-S')
g_z12.adicionaAresta('P-T')
g_z12.adicionaAresta('Q-U')
g_z12.adicionaAresta('Q-R')
g_z12.adicionaAresta('R-V')
g_z12.adicionaAresta('R-S')
g_z12.adicionaAresta('S-W')
g_z12.adicionaAresta('S-X')
g_z12.adicionaAresta('S-T')
g_z12.adicionaAresta('U-C1')
g_z12.adicionaAresta('U-Y')
g_z12.adicionaAresta('V-Y')
g_z12.adicionaAresta('V-Z')
g_z12.adicionaAresta('V-W')
g_z12.adicionaAresta('W-A1')
g_z12.adicionaAresta('X-A1')
g_z12.adicionaAresta('X-B1')
g_z12.adicionaAresta('A1-E1')
g_z12.adicionaAresta('E1-D1')
g_z12.adicionaAresta('D1-C1')
g_z12.adicionaAresta('E1-F1')
g_z12.adicionaAresta('F1-G1')
g_z12.adicionaAresta('G1-E1')
g_z12.adicionaAresta('A-F1')
g_z12.adicionaAresta('G1-F1')




print(g_z12.Algoritmo_de_Dijkstra('A','G1',2,3,['L','S','U','D1']))






