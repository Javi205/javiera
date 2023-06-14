class Numero():
    def __init__(self, numero):
        self.numero = numero
        
    def es_par(self):
        if self.numero % 2 == 0:
            return True
        else:
            return False
    
    def es_impar(self):
        if self.numero % 2 == 0:
            return False
        else:
            return True
