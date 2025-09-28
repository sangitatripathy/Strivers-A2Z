m=int(input("enter the no of edges :"))
n=int(input("enter the number of vertices :"))

adj=[[0 for _ in range (n+1)]for _ in range (n+1)]
for i in range (1,n+1):
  u=int(input("enter the first vertex of edge : "))
  v=int(input("enter the second vertex of edge : "))
  adj[u][v]=1
  adj[v][u]=1

for row in adj:
  print(row)  