class Animal():
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f" {self.nome} tava com muita fome e foi comer...")


class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
    def emitirSom(self):
        print(f" {self.nome} que é toda {self.cor} está miaaando, MIAAAAAAAAAAU...")

class Cachorro(Animal):
    def __init__(self, nome,cor):
        super().__init__(nome,cor)
    def emitirSom(self):
        print(f"{self.nome}que é todo {self.cor} está latindo, AUAU AUAU...")

class Coelho(Animal):
    def __init__(self, nome,cor):
        super().__init__(nome,cor)
    def emitirSom(self):
        print(f" {self.nome} que é todo(a) {self.cor} está ronronando, RAWR RAWR RAWR...")

class Vaca(Animal):
    def __init__(self, nome,cor):
        super().__init__(nome,cor)
    def emitirSom(self):
        print(f"A vaquinha {self.nome} que é toda {self.cor} está mugindo, MUUUUUUUUUUUU...")


class Forma:
    def __init__(self,area,perimetro):
        self.area = area
        self.perimetro = perimetro
