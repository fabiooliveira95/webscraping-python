# 🕸️ Web Scraping em Python

Repositório dedicado ao estudo e prática de **Web Scraping com Python**, focado em coleta, limpeza e análise de dados obtidos de websites públicos.

---

## 🎯 Objetivos

- Coletar dados estruturados de sites públicos.
- Automatizar a extração de informações (ex: preços, notícias, métricas).
- Servir como base de estudo em Python, Web Scraping e Análise de Dados.

---

## 📁 Estrutura do Projeto

webscraping-python/ ├── src/ # Códigos-fonte (scripts de scraping) ├── data/ # Dados coletados (CSV, JSON, etc.) ├── notebooks/ # Jupyter Notebooks para análise └── requirements.txt # Dependências do projeto


---

## ⚙️ Como Usar

1.Clone o repositório
```bash
   git clone https://github.com/fabiooliveira95/webscraping-python.git
```

2.Acesse a pasta do projeto:
```bash
   cd webscraping-python.git
```

3.Instale as dependências 
```bash
   pip install -r requirements.txt
```

🧰 Ferramentas Utilizadas

Python 3+
BeautifulSoup – Análise de HTML/XML
requests – Requisições HTTP
pandas – Manipulação e exportação de dados 

💡 Exemplos de Uso
1. Extraindo Títulos de Notícias (BeautifulSoup)

   python

       from bs4 import BeautifulSoup
       import requests

       url = "http://en.wikipedia.org/wiki/Kevin_Bacon"
       response = requests.get(url)
       soup = BeautifulSoup(response.text, 'html.parser')

       for tag in soup.find_all('h2'):
       print(tag.text.strip())
   
3. Salvando Dados em CSV (pandas)

   python

       import pandas as pd

       dados = {'Produto': ['Item A', 'Item B'], 'Preço': [99.90, 149.90]}
       df = pd.DataFrame(dados)
       df.to_csv('data/precos.csv', index=False)

📌 Resultados

O código acima imprime cabeçalhos da página da Wikipédia. É possível adaptar os seletores ``( find, find_all)``
para capturar qualquer tipo de conteúdo (tabelas, links, imagens, etc.). 

📜 Licença

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)


## 📬 Contato

* Fábio Oliveira
* 🔗 [LinkedIn](https://www.linkedin.com/in/fabio-oliveira-araujo-cientista/)
* 📧 fabiooliveira0067@gmail.com
