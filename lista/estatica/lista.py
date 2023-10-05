class ListaEstatica:
    def __init__(self, maxnelems):
        self.dados = [0] * maxnelems
        self.nelems = 0

    def consulta(self, x):
        for i in range(self.nelems):
            if x == self.dados[i]:
                return True, i
        
        return False, None
    
    def insere(self, x):
        res = self.__verifica__(x)
        if not res:
            return False
        self.dados[self.nelems] = x
        self.nelems += 1
        return True
    
    def remove(self, x):
        res, pos = self.consulta(x)
        if not res:
            return False
        self.dados[pos] = self.dados[self.nelems - 1]
        self.dados[self.nelems - 1] = 0
        self.nelems -= 1
        return True
    
    def remove_ult(self):
        if self.nelems == 0:
            return
        self.dados[self.nelems - 1] = 0
        self.nelems -= 1
        return True

    
    def __verifica__(self, x):
        if x < 0 or x % 2 != 0 or self.nelems >= len(self.dados):
            return False

        return True
    

cadeia = ListaEstatica(10)

cadeia.insere(2)
cadeia.insere(4)
cadeia.insere(16)
cadeia.insere(18)

print(cadeia.dados)
print()

cadeia.remove_ult()
print(cadeia.dados)

cadeia.insere(18)
cadeia.insere(20)

print()
print(cadeia.dados)

cadeia.remove(16)

print()
print(cadeia.dados)