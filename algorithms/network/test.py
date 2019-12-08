
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms import community


path = '/Users/junr/Documents/git/lingua/data/20191206-pdf/chinese.net'
G = nx.readwrite.pajek.read_pajek(path, encoding='utf-8-sig')


# Community detection
# communities_generator = community.girvan_newman(G)
# top_level_communities = next(communities_generator)
# next_level_communities = next(communities_generator)

communities = community.greedy_modularity_communities(G)


# Draw
# pos = nx.spring_layout(G)
# colors = range(20)
# options = {
#     # "node_color": "#A0CBE2",
#     # "edge_color": colors,
#     "width": 4,
#     "edge_cmap": plt.cm.Blues,
#     "with_labels": False,
# }
# nx.draw(G, pos, **options)
# plt.show()


