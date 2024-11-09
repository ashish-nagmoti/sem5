#o(m^v * v) (m->colr and v->vertice )  o(n)(no of vertice)
count = 0
def is_safe(graph,color,v,c):
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] ==c:
            return False
    return True

def graph_coloring_util(graph,m,color,v):
    global count
    if v == len(graph):
        count+=1
        print(count)
        print("--------------------------------------------------------\n")
        for v in range(len(graph)):
            print(f"Vertx :{v }--> color:{color[v]}")
        print("--------------------------------------------------------\n")
        return True
    for c in range(1,m+1):
        if is_safe(graph,color,v,c):
            color[v] = c
            graph_coloring_util(graph,m,color,v+1)
            
            color[v] = 0
    return False

def graph_coloring(graph,m):
    color = [0]*len(graph)

    if not graph_coloring_util(graph,m,color,0):
        print("no next soln")
        return False


    return True

if __name__ == "__main__":
    graph = [
        [0,1,1,1],
        [1,0,1,0],
        [1,1,0,1],
        [1,0,1,0]
    ]
    m=3
    graph_coloring(graph,m)