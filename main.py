import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math import inf
import csv
class Graph():
	def __init__(self) -> None:
		dfc = pd.read_csv('costos.csv', sep=';',header=None,names=['origen','destino','precio'])

		print(dfc)

		G = nx.DiGraph() 

		G = nx.from_pandas_edgelist(dfc,"origen","destino","precio",create_using=nx.DiGraph)

		self.Graph = G

		self.Graph.edges(data=True)
		for u, v, attrs in G.edges(data=True):
			weight_str = attrs['precio'].replace(",","")
			weight_int = int(weight_str)
			attrs['precio'] = weight_int
		self.edges= edge_labels = nx.get_edge_attributes(self.Graph, 'precio')


	def showGraph(self):
		dfc = pd.read_csv('costos.csv', sep=';',header=None,names=['origen','destino','precio'])

		print(dfc)

		G = nx.DiGraph() 

		G = nx.from_pandas_edgelist(dfc,"origen","destino","precio",create_using=nx.DiGraph)

		self.Graph = G

		self.Graph.edges(data=True)
		for u, v, attrs in G.edges(data=True):
			weight_str = attrs['precio'].replace(",","")
			weight_int = int(weight_str)
			attrs['precio'] = weight_int
		edge_labels = nx.get_edge_attributes(self.Graph, 'precio')
		pos = nx.spring_layout(self.Graph)

		nx.draw_networkx_edge_labels(self.Graph,pos,rotate=False,edge_labels=edge_labels)

		nx.draw(self.Graph,pos,with_labels=True,node_color="lightgreen")
		
		plt.show()

	def addNewRoute(self,origin,destination,price):
		line = [origin,destination,price]
		new_data_str = ';'.join(map(str, line))
		fname = 'costos.csv'
		with open(fname,mode="a",newline='') as file:
			writer = csv.writer(file)
			writer.writerow([new_data_str])
		self.__init__

	def shortestRoute(self,origin,destination):
		# Apply Dijkstra's algorithm to find the shortest path
		G = self.Graph
		shortest_path = nx.shortest_path(G, source=origin, target=destination, weight='precio')

		# Draw the graph
		pos = nx.spring_layout(G)
		nx.draw(G, pos, with_labels=True, node_color='lightgreen')

		# Highlight the shortest path in red
		path_edges = [(shortest_path[i], shortest_path[i + 1]) for i in range(len(shortest_path) - 1)]
		nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red')
		nx.draw_networkx_edge_labels(self.Graph,pos,rotate=False,edge_labels=self.edges)

		# Show the plot
		plt.show()



if __name__ == '__main__':
	g = Graph()
	g.showGraph()
	g.shortestRoute("LQM","PVA")