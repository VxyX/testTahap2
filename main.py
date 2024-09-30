import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
pos = {
    'A' : (0,0),
    'B' : (0.5,0.5),
    'C' : (0.5,-0.5),
    'D' : (1,0.5),
    'E' : (0.95,-0.4),
    'F' : (1.5,0.2),
    }

for letter, value in pos.items():
    G.add_node(letter, color='#A4C2F4')
G.nodes['B']['color'] = 'white'

edges = [('A', 'B', {'weight' : 4}), ('A', 'C', {'weight' : 2}), 
        ('B', 'D', {'weight' : 10}), ('B', 'C', {'weight' : 5}),
        ('C', 'E', {'weight' : 3}),
        ('D', 'F', {'weight' : 11}),
        ('E', 'D', {'weight' : 4})]

G.add_edges_from(edges, color='black')

################### Finding Path ############################
start = 'A'
end = 'E'
length, path = nx.single_source_dijkstra(G, start)

print(f"Nearest path from {start} to {end} = {path[end]} = {length[end]}")

for i in range(len(path[end]) - 1):
    G[path[end][i]][path[end][i+1]]['color'] = 'blue'
###############################################################

nx.draw(
    G, pos,  
    edge_color=[G[u][v]['color'] for u, v in G.edges()], width=1, linewidths=1,
    node_size=1000, 
    node_color=[G.nodes[node]['color'] for node in G.nodes()], edgecolors='black', alpha=0.9,
    labels={node: node for node in G.nodes()}, 
    arrows=True, arrowstyle='simple', arrowsize=8
)

nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels=nx.get_edge_attributes(G, 'weight'),
    font_color='black'
)



plt.xlim(-0.5, 2)
plt.ylim(-1.5,1.5)
plt.show()