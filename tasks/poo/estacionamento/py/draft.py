from abc import ABC, abstractmethod
class Veiculo(ABC):
    def __init__(self, id: str, entrada: int, tipo: str):
        self.id = id
        self.entrada = entrada
        self.tipo = tipo
    @abstractmethod
    def calcular_valor(self, saida: int) -> float:
        pass
 


