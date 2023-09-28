from node import Node


class ListaDupla:
    def __init__(self):
        self.prim = None
    
    def consulta(self, x: int):
        p = self.prim
        while (p != None) and (p.chave != x):
            p = p.prox
        if (p == None):
            return False
        return True
    
    def insere(self, x: int):
        if self.consulta(x):
            return False
        p = Node(x)
        if self.prim == None:
            self.prim = p
        else:
            p.prox = self.prim
            self.prim.ant = p
            self.prim = p
        return True
    
    def remove(self, x: int):
        p = self.prim
        while (p != None) and (p.chave != x):
            p = p.prox
        if (p == None):
            return False
        if p.ant:
            p.ant.prox = p.prox
        else:
            self.prim = p.prox
        if p.prox:
            p.prox.ant = p.ant
        return True
        