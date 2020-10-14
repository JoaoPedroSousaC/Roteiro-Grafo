def DFSCount( v, visited):
    count = 1

    VerticesEmV = []
    for vert in range(len(g_p.N)):
        if g_p.N[vert] == v:
            verticeV = vert
    visited[verticeV] = True
    for j in range(len(g_p.N)):
        for i in range(len(g_p.N)):
            if (i > j) and (j == verticeV) and (g_p.M[j][i] > 0):
                VerticesEmV.append(g_p.N[i])
            if (i > j) and (i == verticeV) and (g_p.M[j][i] > 0):
                VerticesEmV.append(g_p.N[j])

    for i in VerticesEmV:
        for vert in range(len(g_p.N)):
            if g_p.N[vert] == i:
                indice = vert
        if visited[indice] == False:
            count = count + DFSCount(i,visited)
    return count





def isValidNextEdge(u, v):
    VerticesEmU = []
    for vert in range(len(g_p.N)):
        if g_p.N[vert] == u:
            verticeu = vert
    for j in range(len(g_p.N)):
        for i in range(len(g_p.N)):
            if (i > j) and (j == verticeu) and (g_p.M[j][i] > 0):
                VerticesEmU.append(g_p.N[i])
            if (i > j) and (i == verticeu) and (g_p.M[j][i] > 0):
                VerticesEmU.append(g_p.N[j])
    if len(VerticesEmU) == 1:
        return True
    else:
        visitados = [False] * (g_p.N)
        cont1 = DFSCount(u,visitados)
        g_p.remove_aresta(u+"-"+v)
        visitados = [False] * (g_p.N)
        cont2 = DFSCount(u, visitados)
        g_p.adicionaAresta(u+"-"+v)
        return False if cont1 > cont2 else True
