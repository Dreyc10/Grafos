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
    




    
