import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math import inf
import heapq


def findShortestPaths(graph, source, n):

	# create a min-heap and push source node having distance 0
	pq = []
	heappush(pq, Node(source))

	# set initial distance from the source to `v` as infinity
	dist = [sys.maxsize] * n

	# distance from the source to itself is zero
	dist[source] = 0

	# list to track vertices for which minimum cost is already found
	done = [False] * n
	done[source] = True

	# stores predecessor of a vertex (to a print path)
	prev = [-1] * n

	# run till min-heap is empty
	while pq:

		node = heappop(pq)  	# Remove and return the best vertex
		u = node.vertex 		# get the vertex number

		# do for each neighbor `v` of `u`
		for (v, weight) in graph.adjList[u]:
			if not done[v] and (dist[u] + weight) < dist[v]:		# Relaxation step
				dist[v] = dist[u] + weight
				prev[v] = u
				heappush(pq, Node(v, dist[v]))

		# mark vertex `u` as done so it will not get picked up again
		done[u] = True

	route = []
	for i in range(n):
		if i != source and dist[i] != sys.maxsize:
			get_route(prev, i, route)
			print(f'Path ({source} —> {i}): Minimum cost = {dist[i]}, Route = {route}')
			route.clear() 


G_eje = nx.Graph() 
G_eje.add_node("GIAN")
G_eje.add_nodes_from([2,3])
print(G_eje.nodes())

df = pd.read_excel('aeropuertos.xlsx')

df.set_index(["IATA"], inplace=True)

#print(df)

dfc = pd.read_csv('costos.csv', sep=';',header=None,names=['origen','destino','precio'])

print(dfc)

G = nx.DiGraph()

G = nx.from_pandas_edgelist(dfc,"origen","destino","precio",create_using=nx.DiGraph)

plt.show()
#print(G.edges(data=True))

pos = nx.spring_layout(G)

nx.draw_networkx_labels(G,pos,font_size=7,font_family="sans-serif")
#plt.show()


mat = nx.adjacency_matrix(G).todense()

nx.draw(G,with_labels=True,node_color="lightgreen")



#plt.show()
print(list(G.neighbors("MDE")))


print(mat)

print(findShortestPaths(mat,"MDE",4))