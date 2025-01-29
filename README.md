Web Scraping com BeautifulSoup

Este projeto demonstra como realizar web scraping em páginas da Wikipédia utilizando a biblioteca BeautifulSoup e o módulo urllib em Python. O código busca links dentro de uma página da Wikipédia e imprime aqueles que seguem um padrão específico.

Requisitos

Certifique-se de ter o Python instalado em seu sistema. Para instalar a biblioteca BeautifulSoup, execute:

pip install beautifulsoup4

Como o Código Funciona

Importação dos módulos necessários:

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

A página de exemplo é carregada:

html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')

Busca de links gerais:

for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

Este trecho captura todos os links na página.

Busca de links dentro de um conteúdo específico:

for link in bs.find('div', {'id': 'bodyContent'}).find_all(
    'a', href=re.compile('^(/wiki/)((?!:).)*?')):
    if 'href' in link.attrs:
        print(link.attrs['href'])

Aqui, capturamos apenas links da página que começam com /wiki/, excluindo links externos e de categorias especiais.

Saída Esperada

O código imprime URLs que apontam para outras páginas da Wikipédia. Alguns exemplos possíveis:

/wiki/Kevin_Bacon_filmography
/wiki/Hollywood_Walk_of_Fame
/wiki/American_actor

Possíveis Melhorias

Tratamento de Erros: Adicionar blocos try-except para lidar com problemas de conexão ou páginas inacessíveis.

Filtragem Avançada: Refinar a busca para excluir links irrelevantes.

Exportação: Salvar os links em um arquivo CSV.

Aviso Legal

Este projeto foi criado para fins educacionais. Certifique-se de seguir os Termos de Uso da Wikipédia e de qualquer site ao realizar web scraping.

