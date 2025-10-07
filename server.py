from flask import Flask, request, jsonify
from rdflib import Graph

app = Flask(__name__)

# Loading the ontology
g = Graph()
g.parse("ontology/ontology.owl", format="xml")

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "message": "Cognitive AI server is running"})

@app.route("/stats", methods=["GET"])
def stats():
    classes = len(set(g.subjects(predicate=None, object=None)))
    triples = len(g)
    return jsonify({
        "triples": triples,
        "unique_subjects": classes
    })

@app.route("/query", methods=["POST"])
def query():
    """
    Example call:
    curl -X POST http://127.0.0.1:5000/query -H "Content-Type: application/json" \
        -d '{"query": "SELECT ?drug ?effect WHERE { ?drug <http://example.org/pharm#hasSideEffect> ?effect }"}'
    """
    sparql_query = request.json.get("query")
    try:
        results = g.query(sparql_query)
        output = []
        for row in results:
            output.append([str(x) for x in row])
        return jsonify({"results": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/example_query", methods=["GET"])
def example_query():
    """
    An example of a ready-made SPARQL query: retrieve all drugs and their side effects.
    """
    sparql_query = """
    PREFIX ex: <http://example.org/pharm#>
    SELECT ?drug ?effect
    WHERE {
      ?drug a ex:Drug .
      ?drug ex:hasSideEffect ?effect .
    }
    """
    try:
        results = g.query(sparql_query)
        output = [{"drug": str(row.drug), "effect": str(row.effect)} for row in results]
        return jsonify({"query": sparql_query, "results": output})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
