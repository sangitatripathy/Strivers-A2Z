from collections import defaultdict
graph=defaultdict(list)

def add_edge(graph,u,v):
  graph[u].append(v)
  graph[v].append(u)

def generate_edges(graph):
  edges=[]
  visited=set()
  for node in graph:
    for neighbour in graph[node]:
      edge=tuple(sorted((node,neighbour)))
      if edge not in visited:
        edges.append(edge)
        visited.add(edge)
  return edges  


n=int(input("enter the number of edges :"))
for _ in range(n):
  u=int(input("enter the first vertex of edge : "))
  v=int(input("enter the second vertex of edge : "))
  add_edge(graph,u,v)

print(generate_edges(graph))  
      
        


  