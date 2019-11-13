from Node import Node

# Noeud représentant un program ou un bloc du programe
# (Contenu d'une boucle FOR, WHILE, ...)
class ProgramNode(Node):
    type = 'Program'