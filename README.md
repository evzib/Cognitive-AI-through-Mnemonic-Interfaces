# Cognitive Interaction Layers — Simulation Prototype

## Overview
This repository provides a proof-of-concept prototype for **cognitive interaction layers** (CILs).  
CILs act as human-centered interfaces that align structured knowledge (ontologies) with cognitively motivated encodings such as semantic cues, clusters, and visual metaphors.  
The prototype demonstrates how structured knowledge can be mapped into cognitively enriched interaction formats.

## Quick Start

Clone the repository and install dependencies:

`bash
git clone https://github.com/<your-username>/Cognitive-AI-through-Mnemonic-Interfaces.git
cd Cognitive-AI-through-Mnemonic-Interfaces
pip install -r requirements.txt`

Run the demo scripts:

`python main.py
python server.py`

API Endpoints

After starting the Flask server (python server.py), the following endpoints are available:

    'GET /health — server status check
    Example output:

{"status": "ok", "message": "Cognitive AI server is running"}

GET /stats — ontology summary (triples, unique subjects)

POST /query — custom SPARQL query
Example:

curl -X POST http://127.0.0.1:5000/query \
     -H "Content-Type: application/json" \
     -d '{"query": "SELECT ?drug ?effect WHERE { ?drug <http://example.org/pharm#hasSideEffect> ?effect }"}'

GET /example_query — built-in query returning all drugs and their side effects
Example output:

    {
      "results": [
        {"drug": "http://example.org/pharm#Aspirin", "effect": "http://example.org/pharm#Bleeding"},
        {"drug": "http://example.org/pharm#Paracetamol", "effect": "http://example.org/pharm#Hepatotoxicity"}
      ]
    }
`
Notes

    This prototype uses simulation-based evaluation only (no human participants).

    Example ontology domain: pharmacology.

    Related preprint available on Zenodo: 10.5281/zenodo.15651442

.

License: MIT (see LICENSE).

