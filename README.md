# VitrineNeuroMAT
Este projeto contem as informações das consultas SPARQL da página vitrine neuromat feitas sobre o Wikidata. 
Também, as consultas em SPATRQL criadas para a publicação do artigo que explica a todo o processo de wikidificação das publicações do NeuroMAT.


This project contains information from SPARQL queries from the neuromat showcase page made over Wikidata. Also, the SPATRQL queries created for the publication of the article that explains the entire process of wikidification of NeuroMAT publications.

# Setup project

1. dev environment setup

Requirements:
- [Python 3.10+](https://www.python.org)
- [pip 24.0+](https://pip.pypa.io/en/stable/installation/)

We recommend using venv, or similar virtual environment, before proceeding. [Creating Virtual Environments](https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-and-using-virtual-environments)

1. install project dependencies

```sh
pip install -r requirements.txt
```

1. [run Jupyter Notebook](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/)

```sh
jupyter notebook
```

# Running local (with built-in python HTTP server)

1. in Jupyter Notebook, open the most recent `.ipynb` and `Run > Run All Cells`. This updates the `index.html`.

1. start the HTTP server on port `8000`
```sh
python3 -m http.server 8000
```

1. visit `http://localhost:8000` to verify your changes