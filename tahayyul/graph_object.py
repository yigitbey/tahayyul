
from py2neo import Node, Relationship

from app import db


class GraphObject(Node):
    def __init(self, **kwargs):
        super(GraphObject, self).__init__(kwargs)
        self.name = None

    def save(self):
        if self.name:
            self.labels.add(self.name)
        db.create(self)