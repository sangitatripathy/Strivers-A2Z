from collections import defaultdict,deque

graph=defaultdict(list)
n=int(input("enter the number of edges :"))
for _ in range (n):
  u=int(input("enter the first vertex of edge"))
  v=int(input("enter the second vertex of edge"))
  graph[u].append[v]
  graph[v].append[u]

def bfs(graph,start):
  visited=set()
  queue=deque([start])

  while queue:
    node=queue.popleft() 
    visited.add(node)
    for neighbour in graph[node]:
      if neighbour not in visited:
        queue.append(neighbour)

start_node=int(input("Enter the starting node of bfs"))  
bfs(graph,start_node)

  