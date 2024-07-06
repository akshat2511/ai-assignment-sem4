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

def getDirection(a, b):
    if (b - a) == 1:
        return 'R'
    elif (a - b) == 1:
        return 'L'
    elif (b - a) == 2:
        return 'D'
    else:
        return 'U'

def getResult(component, dirt):
    n = len(component)
    for i in range(n - 1):
        x=component[i]
        if dirt[(x - 1)] == 1:
            print(component[i], 'S')
        else:
            print(component[i], 'N')
        dir = getDirection(component[i], component[i + 1])
        print(component[i], dir)
    if dirt[(component[n - 1] - 1)] == 1:
        print(component[n - 1], 'S')
    else:
        print(component[n - 1], 'N')


if __name__ == "__main__":
    # Graph of nodes
    graph = {
        1: [2, 3],
        2: [4, 1],
        3: [1, 4],
        4: [2, 3]
    }
    file = open("input.txt", "r")
    node = file.readline().rstrip('\n')

    print(node)

    dust = file.readline().split(',')
    dirt = [(dust[0]), (dust[1]), (dust[2]), (dust[3].rstrip('\n'))]
    print(dirt)

    approach = file.readline()
    print(approach)
    # node = 1  # Starting node
    
    max_node = max(graph.keys())
    visited = [False] * max_node
    if(approach == 'dfs'):
        component_dfs = []
        dfs(node, graph, visited, component_dfs)
        print(f"DFS Result: {component_dfs}")
        getResult(component_dfs, dirt)

    elif(approach == 'bfs'):
        component_bfs = []
        bfs(node, graph, visited, component_bfs)
        print(f"BFS Result: {component_bfs}")
        getResult(component_bfs, dirt)

    # dirt = [1, 0, 0, 1]

    # visited = [False] * max_node
