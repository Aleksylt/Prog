from bs4 import BeautifulSoup
from config import PARSE_URL
import ssl
import os.path
import urllib.request

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


def a_plus_b(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError
    return a + b


def a_minus_b(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError
    return a - b


def get_site_responce() -> str:
    ssl._create_default_https_context = ssl._create_unverified_context
    url = PARSE_URL
    try:
        return urllib.request.urlopen(url).read()
    except:
        print("error url")


def main():
    if os.path.exists("html.txt"):
        with open("html.txt", "r", encoding='utf8') as file:
            doc = file.read()
    else:
        doc = get_site_responce()
        with open("html.txt", "wb") as file:
            file.write(doc)

    soup = BeautifulSoup(doc, 'html.parser')
    print(soup.title.string)
    a = soup.find_all('a', class_='songs__item-cover')
    for tag in a:
        href = tag.get('href')
        if href.startswith('/'):
            href = PARSE_URL + href[1:]
        elif not href.startswith('http'):
            continue
        img = tag.next_element.get('src').replace(' ', '%20')
        alt = tag.next_element.get('alt')
        if img.startswith('/'):
            img = PARSE_URL + img[1:]
        print(alt)
        print("img: " + img)
        print(href)


if __name__ == '__main__':
    main()
