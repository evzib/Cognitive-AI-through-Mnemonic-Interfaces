# Proof-of-concept CLI for ontology graph visualization
from rdflib import Graph
import networkx as nx
import matplotlib.pyplot as plt
from pathlib import Path

def ontology_to_graph(path="ontology.owl"):
    g = Graph(); g.parse(path)
    G = nx.DiGraph()
    for s,p,o in g:
        G.add_node(str(s)); G.add_node(str(o))
        G.add_edge(str(s), str(o), predicate=str(p))
    return G

if __name__ == "__main__":
    out = Path("outputs"); out.mkdir(exist_ok=True, parents=True)
    G = ontology_to_graph()
    nx.draw(G, with_labels=False, node_size=30, font_size=6)
    plt.tight_layout()
    out_img = out/"ontology_graph.png"
    plt.savefig(out_img, dpi=200)
    print("Saved:", out_img)
