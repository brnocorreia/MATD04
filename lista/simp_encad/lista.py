from node import Node

class ListaSimples:
    def __init__(self):
        self.prim = None
    
    def consulta(self, x: int):
        p = self.prim
        while (p != None):
            if (p.chave == x):
                return True
            p = p.prox
        return False

    def insere(self, x: int):
        if (self.consulta(x)):
            return False
        p = Node(x)
        p.prox = self.prim
        self.prim = p
        return True
    
    def remove(self, x: int):
        pant = None
        p = self.prim
        while (p != None) and (p.chave != x):
            pant = p
            p = p.prox
        if (p == None):
            return False
        if (pant == None):
            self.prim = p.prox
        else:
            pant.prox = p.prox
        return True
