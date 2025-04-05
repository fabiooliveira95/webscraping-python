# 🕷️ Web Scraping em Python

Repositório dedicado ao estudo e prática de **Web Scraping** usando Python, com foco em coleta, limpeza e análise de dados de diversas fontes na web.

## 🚀 Objetivo
Este projeto tem como objetivo:
- Coletar dados estruturados de websites públicos.
- Automatizar a extração de informações (ex.: preços, notícias, métricas).
- Servir como base para estudos em **Python**, **Web Scraping** e **Análise de Dados**.

## 📦 Estrutura do Projeto

webscraping-python/
├── src/ # Códigos-fonte (scripts de scraping)
├── data/ # Dados coletados (CSV, JSON, etc.)
├── notebooks/ # Jupyter Notebooks para análise
└── requirements.txt # Dependências do projeto


## ⚙️ Configuração
1. **Clone o repositório**:

       bash
       git clone https://github.com/fabiooliveira95/webscraping-python.git
       cd webscraping-python

2.Instale as dependências:
     
       bash
       pip install -r requirements.txt

🛠️ Ferramentas Utilizadas

Python 3+
Bibliotecas:
BeautifulSoup - Parsing de HTML/XML.
requests - Requisições HTTP.
pandas - Manipulação de dados.

📌 Exemplos de Uso
Extraindo Títulos de Notícias (BeautifulSoup)

    python
    from bs4 import BeautifulSoup
    import requests

    url = "http://en.wikipedia.org/wiki/kevin_Bacon"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for titulo in soup.find_all('h2', class_='kevin_Bacon'):
    print(link.attrs['href'])

Salvando Dados em CSV (Pandas)
     
    python
    import pandas as pd
    
    dados = {'Produto': ['Item A', 'Item B'], 'Preço': [99.90, 149.90]}
    df = pd.DataFrame(dados)
    df.to_csv('data/precos.csv', index=False)

📊 Resultados
  Aqui, capturamos apenas links da página que começam com /wiki/, excluindo links externos e de categorias especiais.
  Saída Esperada
  O código imprime URLs que apontam para outras páginas da Wikipédia. Alguns exemplos possíveis:
  /wiki/Kevin_Bacon_filmography  
  /wiki/Hollywood_Walk_of_Fame
 /wiki/American_actor

📜 Licença

 ![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
