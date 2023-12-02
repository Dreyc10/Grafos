def create_graph(num_vertex):   
    
    grafo=[]
    i=1
    while i <=num_vertex:
        fila_i= []
        k=1
        while k<=num_vertex:
            fila_i.append(0)
            k=k+1
        grafo.append(fila_i)
        i=i+1

    return grafo 

def conectar_vertices (grafo, v_1, v_2 ):

    grafo[v_1][v_2]=0
    grafo[v_2][v_1]=0

def desconectar_vertices (grafo, v_1, v_2):

    grafo[v_1][v_2]=1
    grafo[v_2][v_1]=1

def adyacentes_a_vi(grafo,v_i):
    i=0
    lista_adyacentes=[]
    while i < len(grafo[v_i]):
        if if_conectados(grafo,v_i,i):
            lista_adyacentes.append(i)
        i=i+1
    return lista_adyacentes

def degree_v_i(grafo,v_i):
    return len(adyacentes_a_vi(grafo,v_i))

def num_arcos(grafo):

    i=1
    sum=0
    while i <= len(grafo):
        sum=sum+degree_v_i(i)
        i=i+1

    return sum/2



def if_conectados (grafo, v_1, v_2 ):
    
    if grafo[v_1][v_2] ==1 :
        return True 
    else:
        return False
    


def sequentialColoring(G,colores):

    b = len(G[0])
    g = []
    for x in range(0,b):
        g.append("u")
    G.insert(0,g)

    l = len(G)

    for i in range(1,l):
        vecinos = []
        for j in range(0,l-1):
            if G[i][j] == 1:
                if G[0][j] != "u":
                    vecinos.append(G[0][j])

        for color in colores:
            if color not in vecinos:
                G[0][i-1] = color
                break
    return G


#print(sequentialColoring(G,colores))
def degreeSaturation(G,colores):

    b = len(G[0])
    g = []
    for x in range(0,b):
        g.append(["u",[],G[x].count(1)])
    G.insert(0,g)



    coloreados = 0

    while coloreados < len(G[0]):

        max1 = 0
        max2 = 0
        indice = 0

        for nodo in G[0]:
            if nodo[0] == "u":
                if len(nodo[1]) > max1:
                    max1 = len(nodo[1])
                    indice = G[0].index(nodo)
                elif len(nodo[1]) == max1 :
                    if nodo[2] > max2:
                        max2 = nodo[2]
                        indice = G[0].index(nodo)



        for color in colores:

            if color not in G[0][indice][1]:
                G[0][indice][0] = color
                for i in range(0,len(G[0])):
                    if G[indice + 1][i] == 1:

                        if color not in G[0][i][1]:

                            G[0][i][1].append(color)

                break
        coloreados += 1

    return G
colores = ["rojo", "azul" , "verde" , "amarillo", "negro", "blanco" , "cafe" , "naranja" , "morado" , "rosado"]
G1 = [ 
     [ 0 , 1 , 1 , 0 , 1 ],
     [ 1 , 0 , 1 , 0 , 0 ],
     [ 1 , 1 , 0 , 0 , 0 ],
     [ 0 , 0 , 0 , 0  ,1 ],
     [ 1 , 0 , 0 , 1 , 0 ]]


G2 = [ 
     [ 0 , 1 , 1 , 1 , 1 ],
     [ 1 , 0 , 1 , 1 , 1 ],
     [ 1 , 1 , 0 , 1 , 1 ],
     [ 1 , 1 , 1 , 0  ,1 ],
     [ 1 , 1 , 1 , 1 , 0 ]] 


print(degreeSaturation(G2,colores))
    




    
