# -*- coding: utf-8 -*-
from py2neo import Node, Relationship

from app import db
from graph_object import GraphObject


class Word(GraphObject):
    def __init__(self, sign, language):

        super(GraphObject, self).__init__(sign, language)
        self.sign = sign
        self.language = language
        self.name = self.sign

    def save(self):
        pass


def sample_words():
    words_list = [
        # ("space", "English"),
        # ("espace", "French"),
        # ("spatium", "Latin"),
        # ("espacio", "Spanish"),
        # ("spazio", "Italian"),
        ("laban", "Arabic"),
        ("sut", "Turkish"),
        ("laban", "Hebrew"),
        ("labne", "Turkish"),
        ("Luban", "Arabic"),
        ("labenzoe", "Latin"),
        ("benzoe", "Latin"),
        ("benjoin", "French"),
        ("benzine", "Latin"),
        ("Benzin", "German"),
        ("benzine",  "English"),
        ("benzin", "Turkish")

    ]
    words = []
    for word in words_list:
        words.append(Word(word[0], word[1]))

    connections = [
        # {
        #     "word": "space",
        #     "language": "English",
        #     "origin_word": "spatium",
        #     "origin_language": "Latin",
        #     "year": 1300,
        #     "origin_year": 1200,
        # },
        # {
        #     "word": "espace",
        #     "language": "French",
        #     "origin_word": "spatium",
        #     "origin_language": "Latin",
        #     "year": 1300,
        #     "origin_year": 1200,
        # },
        # {
        #     "word": "espacio",
        #     "language": "Spanish",
        #     "origin_word": "spatium",
        #     "origin_language": "Latin",
        #     "year": 1300,
        #     "origin_year": 1200,
        # },
        # {
        #     "word": "spazio",
        #     "language": "Italian",
        #     "origin_word": "spatium",
        #     "origin_language": "Latin",
        #     "year": 1300,
        #     "origin_year": 1200,
        # },
        {
            "word": "labenzoe",
            "language": "Latin",
            "origin_word": "laban",
            "origin_language": "Arabic",
        },
        {
            "word": "benzoe",
            "language": "Latin",
            "origin_word": "labenzoe",
            "origin_language": "Latin",
        },
        {
            "word": "benjoin",
            "language": "French",
            "origin_word": "benzoe",
            "origin_language": "Latin",
        },
        {
            "word": "benzine",
            "language": "Latin",
            "origin_word": "benzoe",
            "origin_language": "Latin",
        },
        {
            "word": "Benzin",
            "language": "German",
            "origin_word": "benzine",
            "origin_language": "Latin",
        },
        {
            "word": "benzine",
            "language": "English",
            "origin_word": "benzine",
            "origin_language": "Latin",
        }
        ,
        {
            "word": "benzin",
            "language": "Turkish",
            "origin_word": "Benzin",
            "origin_language": "German",
        }

     ]


    translations = [
        #{
        #    "word": "sut",
        #    "language": "Turkish",
        #    "dest_word": "laban",
        #    "dest_language": "Arabic"
        #},

    ]


    for word, language in words_list:
        w = Node("Words", sign=word, language=language)
        w.labels.add(word)
        l = db.find_one(language)
        db.create(w)
        db.create(Relationship(w, 'word-of', l))
        
    

    for connection in connections:

        w1 = db.find_one(connection['word'], property_key="language", property_value=connection['language'])

        w2 = db.find_one(connection['origin_word'], property_key="language", property_value=connection['origin_language'])

        year = connection.get('year', None)
        rel = db.create(Relationship(w1, 'comes-from', w2, year=year))


    #for translation in translations:
        #w1 = db.find_one(translation['word'], property_key="language", property_value=translation['language'])
        #w2 = db.find_one(translation['dest_word'], property_key="language", property_value=translation['dest_language'])
        #print w1, w2
        #rel = db.create(Relationship(w1, 'translation-of', w2))


