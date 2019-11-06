import pydotplus

# Classe de base pour toutes les sortes de noeuds
class Node:
    # Variables globales
    count = 0
    type = 'Node (unspecified)'
    shape = 'ellipse'

    # Constructeur
    def __init__(self,children=None):
        if children != None:
            children = [children]
        else:
            self.children = []

        self.ID = str(Node.count)
        Node.count+=1
        self.next = []

    # Ajoute le prochain noeud
    def addNext(self,next):
        self.next.append(next)

    # Construit un arbre qui représente toute la structure en dessous de ce noeud (version console)
    def asciitree(self, prefix=''):
        result = "%s%s\n" % (prefix, repr(self))
        prefix += '|  '
        for c in self.children:
            if not isinstance(c,Node):
                result += "%s*** Error: Child of type %r: %r\n" % (prefix,type(c),c)
                continue
            result += c.asciitree(prefix)
        return result
    
    # Retourne l'arbre en format console
    def __str__(self):
        return self.asciitree()
    
    # Retourne la représentation du noeud
    def __repr__(self):
        return self.type
    
    # Construit un arbre représentant toute la structure en dessous de ce noeud (version graphique)
    def makegraphicaltree(self, dot=None, edgeLabels=True):
            if not dot:
                dot = pydotplus.Dot()

            selfNode = pydotplus.Node(self.ID, label=repr(self), shape=self.shape)
            dot.add_node(selfNode)

            for i, c in enumerate(self.children):
                c.makegraphicaltree(dot, edgeLabels)
                edge = pydotplus.Edge(self.ID, c.ID)

                if edgeLabels and len(self.children) - 1:
                    edge.set('label', str(i))

                dot.add_edge(edge)

                #Workaround for a bug in pydot 1.0.2 on Windows:
                #dot.set_graphviz_executables({'dot': r'C:\Program Files\Graphviz2.38\bin\dot.exe'})
            return dot
        
    def threadTree(self, graph, seen = None, col=0):
            colors = ('red', 'green', 'blue', 'yellow', 'magenta', 'cyan')
            if not seen:
                seen = []

            if self in seen:
                return 
            seen.append(self)

            if not graph.get_node(self.ID):
                graphnode = pydotplus.Node(self.ID,label=repr(self), shape=self.shape)
                graphnode.set('style', 'dotted')
                graph.add_node(graphnode)

            for i,c in enumerate(self.next):
                if not c:
                    return

                col = (col + 1) % len(colors)
                color = colors[col]                
                c.threadTree(graph, seen, col)
                edge = pydotplus.Edge(self.ID,c.ID)
                edge.set('color', color)
                edge.set('arrowsize', '.5')
                edge.set('constraint', 'false') 

                if len(self.next) - 1:
                    edge.set('taillabel', str(i))
                    edge.set('labelfontcolor', color)

                graph.add_edge(edge)
            return graph   
        