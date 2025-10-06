from rdflib import Graph

def test_parse():
    g = Graph(); g.parse("ontology.owl")
    assert len(g) > 0
