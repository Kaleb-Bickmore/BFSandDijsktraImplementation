from queue import Queue
myDirectedGraph = {'a':{'b':3,'c':5},'b':{'c':1,'d':2},'c':{'e':2,'d':2},'d':{'e':10},'e':{}}
unDirectedGraph = {'a':['b','c'],'b':['a','c','d'],'c':['d','a'],'d':['c','b','e'],'e':['d'],'f':[]}
def BFS(graph,startNode,endNode):
    if(startNode in graph and endNode in graph ):
        visited = {}
        shortestPath = {}
        for keys in graph:
            visited[keys] = False
            shortestPath[keys] = []
        myQueue = Queue()
        visited[startNode] = True
        for items in graph[startNode]:
            myQueue.put(items)
            visited[items] = True
            shortestPath[items].append(startNode)
            shortestPath[items].append(items)
        while( not myQueue.empty()):
            currrentKey =myQueue.get()
            for items in graph[currrentKey]:
                if(visited[items] ==False):
                    visited[items] =True
                    myQueue.put(items)
                    for x in shortestPath[currrentKey]:
                        shortestPath[items].append(x)
                    shortestPath[items].append(items)


        if((shortestPath[endNode] != [])):
            print("shortest path for "+endNode+ " from "+startNode+" is: ")
            print(shortestPath[endNode])
        else:
            print("could not find a path to "+ endNode +" from "+startNode)
    else:
        print("cannot locate start or end node")

def dijsktras(graph,startNode,endNode):
    if(startNode in graph and endNode in graph ):
        shortestPath = {}
        shortestPathWeight ={}
        for keys in graph.keys():
            shortestPathWeight[keys]=9999999
            shortestPath[keys] = []
        myQueue = Queue()

        for items in graph[startNode].keys():
            myQueue.put(items)
            shortestPath[items].append(startNode)
            shortestPath[items].append(items)
            shortestPathWeight[items] = graph[startNode][items]
        while( not myQueue.empty()):
            currrentKey =myQueue.get()
            for items,weights in graph[currrentKey].items():
                if(weights+shortestPathWeight[currrentKey]<shortestPathWeight[items]):
                    myQueue.put(items)
                    shortestPath[items]=[]
                    shortestPathWeight[items] = weights+shortestPathWeight[currrentKey]
                    for x in shortestPath[currrentKey]:
                        shortestPath[items].append(x)
                    shortestPath[items].append(items)


        if((shortestPath[endNode] != [])):
            print("with a weight of "+str(shortestPathWeight[endNode])+" shortest path for "+endNode+ " from "+startNode+" is: ")
            print(shortestPath[endNode])

        else:
            print("could not find a path to "+ endNode +" from "+startNode)
    else:
        print("cannot locate start or end node")

print("undirected graphs shortest path: ")
print("************************************")
print("path from 1:b : ")
BFS(unDirectedGraph,1,'b')
print("path from a:e : ")
BFS(unDirectedGraph,'a','e')
print("path from a:c : ")
BFS(unDirectedGraph,'a','c')
print("path from c:f : ")
BFS(unDirectedGraph,'c','f')

print("************************************")
print("directed, weighted graphs shortest path using Dijsktras: ")
print("************************************")
print("path from 1:b : ")
dijsktras(myDirectedGraph,1,'b')
print("path from a:e : ")
dijsktras(myDirectedGraph,'a','e')
print("path from b:d : ")
dijsktras(myDirectedGraph,'b','d')
