# Cognitive Interaction Layers — Simulation Prototype

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15651442.svg)](https://doi.org/10.5281/zenodo.15651442)

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

## API Endpoints

After starting the Flask server (python server.py), the following endpoints are available:

GET /health — server status check

Example output:
`{ "status": "running" }`

## Notes

Simulation-based evaluation only (no human participants)

Example ontology domain: pharmacology

## License

MIT License (see LICENSE file)
