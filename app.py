# Minimal Flask API for ontology statistics
from flask import Flask, jsonify
from rdflib import Graph

app = Flask(__name__)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/stats")
def stats():
    g = Graph(); g.parse("ontology.owl")
    return jsonify({"triples": len(g)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
