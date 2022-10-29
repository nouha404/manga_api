import uvicorn
from fastapi import FastAPI, Path

from views import get_all_images, get_about, get_specifique, get_last_chapter, get_last_five_chapter, get_name_only, \
    get_number_chapter_only

app = FastAPI()


@app.get('/')
def index():
    return {'message': 'My first Api',
            'about/': 'To get information about manga name',
            'docs/': 'Get the documentation',
            }


# recuperer les informations
@app.get('/about/')
def about():
    return get_about()


# recuperer tous nom des chapitres
@app.get('/chapters/')
def manga_pages():
    return get_all_images()


# Recuperer un chapitre
@app.get('/chapters/{id}/pages/')
def get_specifique_chapter(id: str = Path(..., description='Add the id to get the a chapter specifique')):
    return get_specifique(id)


# Recuperer le dernier chapter
@app.get('/last/')
def last_chapter():
    return get_last_chapter()


@app.get('/chapters/{id}/name/')
def get_name(id: str = Path(..., description='Add the id to get the chapter name')):
    return get_name_only(id)


@app.get('/chapters/{id}/pages/{number_chapter}/')
def get_image_with_number(id: str, number_chapter: str):
    return get_number_chapter_only(id, number_chapter)


@app.get('/last/five/')
def last_five():
    return get_last_five_chapter()


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)