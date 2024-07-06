#  Choose a classic problem-solving task (e.g., the Eight Queens Puzzle, the Traveling Salesman
# Problem) and formulate it as a search problem. Implement and compare different search
# algorithms (e.g., DFS, BFS, A*, etc.) to find solutions to the problem. Analyze the efficiency and
# effectiveness of each algorithm in solving the problem.

#maze problem
from collections import deque


def dfs(node, graph, visited, component):
    node = int(node)
    component.append(node)
    visited[node - 1] = True

    for child in graph[node]:
        if not visited[child - 1]:
            dfs(str(child), graph, visited, component)

def bfs(node, graph, visited, component):
    node = int(node)
    queue = deque([node])
    visited[node - 1] = True

    while queue:
        current = queue.popleft()
        component.append(current)

        for child in graph[current]:
            if not visited[child - 1]:
                visited[child - 1] = True
                queue.append(child)
def manhattanastar (node, graph, visited, component):
    diff= abs(int(node[0]) - 0) + abs(int(node[1]) - 0)
    return diff
def matrixtosearchgraph(matrix):
    nodes={}
    edges=[]
    for i in range(len(matrix)):
        row=""
        for j in range(len(matrix[i])):
            row+= str((i+1)*4+(j+1))
        nodes["R"+str(i+1)]=row
    for i in range(5):
        for j in range(5):
            if matrix[i][j]!=0 and i<4 and matrix[i+1][j]==0:edges.append((("R"+str(i+1)),"R"+str(i+1)+","+str(j+1)))
            if matrix[i][j]!=0 and i<4 and j<4:
                edges.append((("R"+str(i+1),"C"+str(j+1)),matrix[i][j], "R"+str(i+1)+","+str(j+1)))
    return nodes,edges
# startx, starty = input().split(" ")
# start=[startx, starty]
# numNodes, numEdges = map(int,input().split())
#obstacles is 1
#maze
a= [[2 , 0 , 0 , 0 , 0 ],
    [0 , 0 , 1 , 1 , 0 ],
    [0 , 0 , 1 , 0 , 0 ],
    [0 , 1 , 1 , 0 , 0 ],
    [0 , 0 , 0 , 0 , 3 ]]

nodes,edges =matrixtosearchgraph(a)
visited = []
component = []
manhattanastar(nodes,edges,visited,component)
print ("Component : ",component)





