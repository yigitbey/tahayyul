from flask import Flask
from flask.ext.neo4j import Neo4j
from py2neo import Node, Relationship

GRAPH_DATABASE="http://localhost:7474/db/data"

tahayyul = Flask(__name__)
tahayyul.config.from_object(__name__)

graph_indexes  = {'Words': Node, "Languages": Node}
db = Neo4j(tahayyul, graph_indexes).gdb



