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

# Testing

At this moment, `NeuroMatVitrine.ipynb` is the main entrypoint, and it is the source for the production page.

1. Make sure all cells run successfully: in Jupyter Notebook, open  ``NeuroMatVitrine.ipynb` and `Run > Run All Cells`

**Or**, using the CLI:
```sh
jupyter nbconvert --to notebook --execute NeuroMatVitrine.ipynb
```

# Validating

To see the changes as they will appear in the production server, you need to:

1. update `index.html`: once you have the new data, add it to the appropriated fields in the `index.html`

1. run a local HTTP server on port `8000` with Python's built-in server:
```sh
python3 -m http.server 8000
```

1. visit `http://localhost:8000` to verify your changes

1. make sure your changes don't break the page style: you can use an online HTML linter to help you
