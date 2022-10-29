import json
from pathlib import Path

with open('one_piece_db.json', 'r') as f:
    data = json.load(f)


def get_about():
    for name in data['informations']:
        return data['informations'][name]


def get_all_images():
    IMAGES = []
    for name in data['pages']:
        for images in data['pages'][name]['name']:
            IMAGES.append(images)
    return IMAGES


def get_specifique(id: str):
    for _ in data['pages']:
        tester = [data['pages'][id] if id in data['pages'] else {f'id {id}: not in the database'}]
        return tester


def get_last_chapter():
    for _ in data['pages']:
        return data['pages']['1']


def get_last_five_chapter():
    FIVE_CHAPTER = []
    for name in data['pages']:
        FIVE_CHAPTER.append(data['pages'][name])
    return FIVE_CHAPTER[:5]


def get_name_only(id: str):
    for _ in data['pages']:
        tester = [data['pages'][id]['name'] if id in data['pages'] else {f"id {id}: not in the database"}]
        return tester


def get_number_chapter_only(id: str, number_page: str):
    new_array = []
    [new_array.append(name) for name in data['pages'][id]['chapters']]

    for names in new_array:
        chemin = Path(names)
        if number_page in chemin.parts[-1]:
            return names