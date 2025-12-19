from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str):
        self.nome = nome


    def apresentar_nome(self):
        print(f"Eu sou um(a) {self.nome}!")

    @abstractmethod
    def fazer_som(self):
        pass

    @abstractmethod
    def mover(self):
        pass

class Leao(Animal):
    def fazer_som(self):
        print("Som: o leão ruge alto! Roar!")

    def mover(self):
        print("Movimento: o leão corre")

class Elefante(Animal):
    def fazer_som(self):
        print("Som: o elefante brame! Fum!")

    def mover(self):
        print("Movimento: o elefante caminha")

class Cobra(Animal):
    def fazer_som(self):
        print("Som: a cobra sibila! hsss!")

    def mover(self):
        print("Movimento: a cobra rasteja")

def apresentar(animal: Animal):
        animal.apresentar_nome()
        animal.fazer_som()
        animal.mover()
        print(f"Tipo do objeto: {type(animal).__name__}")
        print("-" * 30)

if __name__ == "__main__":
        zoologico = [
            Leao("Simba"),
            Elefante("Dumbo"),
            Cobra("Kai"),
        ]
        print("bem vindo ao zoologico\n")
        for bicho in zoologico:
            apresentar(bicho)