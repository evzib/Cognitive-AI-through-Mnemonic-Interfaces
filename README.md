# Cognitive Interaction Layers — Simulation Prototype

**Overview**  
This repository contains a proof-of-concept prototype for cognitive interaction layers.  
It demonstrates how structured knowledge (ontology) can be mapped into cognitively enriched interaction formats using semantic cues, clusters, and visual metaphors.  

**Quick Start**

```bash
python -m venv .venv && source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py                                      # -> generates outputs/ontology_graph.png
python app.py                                       # -> http://localhost:8000/health , /stats
```

**Notes**  
- Simulation-based evaluation only (no human participants).  
- Example ontology domain: pharmacology.  
- Related preprint available on Zenodo (DOI: 10.5281/zenodo.15651442).  

**License**  
MIT License (see LICENSE).
