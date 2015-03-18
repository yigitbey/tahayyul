from py2neo import Node, Relationship
from app import db

def init_languages():
    languages = ["English", 
                 "French", 
                 "Latin", 
                 "Spanish", 
                 "Italian", 
                 "Turkish", 
                 "German", 
                 "Arabic",
                 "Hebrew",
                 ]

    for language in languages:
        l = Node('Languages', name=language)
        l.labels.add(language)
        db.create(l)
        
