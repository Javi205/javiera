class Numero():
    def __init__(self, numero):
        self.numero = int(numero)
        
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

    def es_primo(self):
        if self.numero < 2:
            return False
        for i in range(2, int(self.numero ** 0.5) + 1):
            if self.numero % i == 0:
                return False
        return True
    
    def es_compuesto(self):
        if self.numero < 2:
            return False
        for i in range(2, int(self.numero ** 0.5) + 1):
            if self.numero % i == 0:
                return True
        return False
     
    def es_perfecto(self): 
        suma = 0
        for i in range(1, self.numero):
            if self.numero % i == 0:
                suma += i
                print(suma)
        if suma == self.numero:
            return True
        else: 
            return False


    
a = Numero(6)
# print(a.es_impar())
#print(a.es_par())
#print(a.es_primo())
# print(a.es_compuesto())
print(a.es_perfecto())
