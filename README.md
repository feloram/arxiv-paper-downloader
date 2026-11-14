# ArXiv Paper Downloader

A simple Python script that fetches research papers from the arXiv API and saves their PDF files locally.

## Features
- Search for papers based on custom queries.
- Automatically creates a `data/` directory to store PDFs.
- Skips downloading if the paper already exists to save time and bandwidth.

## Customizing Search Queries
The script currently searches for AI-related topics (e.g., "Retrieval-Augmented Generation", "Large Language Models agents"). 
**You can easily change these topics to anything you want!** 

To do this, open `download_papers.py` and modify the `search_queries` list. For example:
```python
search_queries = [
    "Quantum Computing",
    "Cancer Research",
    "Renewable Energy"
]
