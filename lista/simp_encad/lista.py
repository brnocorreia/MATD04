from node import Node

class ListaSimples:
    def __init__(self):
        self.prim = None
    
    def consulta(self, x: int):
        p = self.prim
        while (p != None):
            if (p.chave == x):
                return True, p
            p = p.prox
        return False, None

    def insere(self, x: int):
        res = self.__verifica__(x)
        if not res:
            return res
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
    
    def remove_maior(self):
        if self.prim == None:
            return 
        
        p = self.prim
        pant = None
        maior = self.prim.chave
        while p.prox:
            if p.prox.chave > maior:
                maior = p.prox.chave
                pant = p
            p = p.prox
        
        if pant == None:
            if self.prim.chave == maior:
                self.prim = self.prim.prox
        else:
            pant.prox = pant.prox.prox
    
    def display(self):
        p = self.prim
        while p:
            print(p.chave, end=' -> ')
            p = p.prox
        print("None")

    
    def __verifica__(self, x):
        if x < 0 or x % 2 != 0:
            return False
        return True
    

cadeia = ListaSimples()

cadeia.insere(4)
cadeia.insere(8)
cadeia.insere(2)
cadeia.insere(4)
cadeia.insere(6)

print('lista original:')
cadeia.display()

print()

cadeia.remove_maior()

print('lista agora:')
cadeia.display()
        
