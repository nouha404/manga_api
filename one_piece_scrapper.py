from bs4 import BeautifulSoup
import requests
from tinydb import TinyDB

db = TinyDB('one_piece_db.json', indent=4, ensure_ascii=False)
INFORMATION = db.table('informations')
MANGA = db.table('pages')

headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36 Edg/105.0.1343.33'
}


def get_informations(url: str):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    infos = soup.find('dl', class_='dl-horizontal')

    author = infos.findAll('dd')
    release_date = infos.findAll('dd')
    category = infos.findAll('dd')
    resume = soup.find('div', class_='well').p

    INFORMATION.insert({'author': author[2].text.replace('\n', ''),
                        'resume': resume.text,
                        'release-date': release_date[3].text,
                        'category': [
                            category[4].text]})


get_informations('https://www.scan-vf.net/one_piece')

CHAPTERS = []


def get_all_chapters(url: str):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    chapters = soup.find('ul', class_='chapters')
    all_chapters = chapters.findAll('a')

    for src in all_chapters:
        links = src['href']
        CHAPTERS.append(links)
    return CHAPTERS


get_all_chapters('https://www.scan-vf.net/one_piece')


def get_scan_names():
    for url in CHAPTERS:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        # get names
        names_class = soup.findAll('div', class_='page-header')
        NAMES = []
        for name in names_class:
            name_extracted = name.find('b').text
            NAMES.append(name_extracted)

        # get images
        images_class = soup.findAll('img', class_='img-responsive')
        IMAGES = []
        for img_src in images_class:
            image_extracted = img_src.get('data-src')
            IMAGES.append(image_extracted)
            print(f'Extraction de tous les images de {image_extracted} ...')
        MANGA.insert({'name': NAMES, 'chapters': IMAGES})


get_scan_names()
