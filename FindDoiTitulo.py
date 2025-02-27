#encontrar DOI por título, via crossref
import requests

def get_doi(title):
    url = "https://api.crossref.org/works"
    params = {"query.bibliographic": title, "rows": 1}
    response = requests.get(url, params=params)
    data = response.json()
    try:
        return data["message"]["items"][0]["DOI"]
    except (KeyError, IndexError):
        return "DOI não encontrado"

# Exemplo de uso
titulo = "Acetylcholine modulation in a biophysical model of cortical neuron"
print(get_doi(titulo))
