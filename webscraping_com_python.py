from  urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

        # //wikimediafoundation.org/wiki/Privacy_policy
        # //en.wikipedia.org/wiki/wikipedia.Contact_us

        # /wiki/Category:Articles_with_unsourced_statements_from_april_2014
        # /wiki/talk:kevin_Bacon

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://en.wikipedia.org/wiki/kevin_Bacon')
from  urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://en.wikipedia.org/wiki/kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])

        # //wikimediafoundation.org/wiki/Privacy_policy
        # //en.wikipedia.org/wiki/wikipedia.Contact_us

        # /wiki/Category:Articles_with_unsourced_statements_from_april_2014
        # /wiki/talk:kevin_Bacon

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://en.wikipedia.org/wiki/kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find('div', {'id':'bodyContent'}).find_all(
    'a', href=re.compile('^(/wiki/)((?!:).)*?')):
    if 'href' in link.attrs:
        print(link.attrs['href'])