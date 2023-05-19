import networkx as nx
import pandas as pd
from IPython.display import HTML
import matplotlib.pyplot as plt



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

G = nx.from_pandas_edgelist(dfc,source="origen",target="destino",create_using=nx.DiGraph)

pos = nx.spring_layout(G)

nx.draw_networkx_labels(G,pos,font_size=10,font_family="sans-serif")