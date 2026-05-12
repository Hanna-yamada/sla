class Animal:
    def __init__(self, nome, especie, patas):
        self.nome = nome
        self.especie = especie
        self.patas = patas
    
    def respirar(self):
        print("respirando...")
    def rugir(self):
        print("O animal vai rugir...")

class Cachorro(Animal):
 
    def abanar_rabo (self):
        print("Abanando rabo...") 
    def rugir(self):
        print("Auu Auu")    

class Gato(Animal):       
    def __init__(self, nome,especie,patas):
        super().__init__( nome,especie,patas)
        # self.dono = dono        

    def ronronar (self):
        print("animal ronronar...")
    def rugir(self):
        print("Miau")  