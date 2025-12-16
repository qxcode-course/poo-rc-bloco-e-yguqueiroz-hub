from abc import ABC, abstractmethod

class Veiculo(ABC):
    def __init__(self, id: str, tipo:str, entrada: int):
        self.id = id
        self.entrada = entrada
        self.tipo = tipo
    @abstractmethod
    def calcular_valor(self, saida: int) -> float:
        pass

    def __str__(self):
        fmt_tipo = self.tipo.rjust(10, "_")
        fmt_id = self.id.rjust(10, "_")
        return f"{fmt_tipo} : {fmt_id} : {self.entrada}"


class Bike(Veiculo):
    def __init__(self, id: str, entrada: int):
        super().__init__(id, "Bike", entrada)

    def calcular_valor(self, saida_saida: int) -> float:
        return 3.00
class Moto(Veiculo):
    def __init__(self, id: str, entrada: int):
        super().__init__(id, "Moto", entrada)

    def calcular_valor(self, hora_saida: int) -> float:
        tempo = hora_saida - self.entrada
        return tempo / 20.0
    
class Carro(Veiculo):
    def __init__(self, id: str, entrada: int):
        super().__init__(id, "Carro", entrada)

    def calcular_valor(self, hora_saida: int) -> float:
        tempo = hora_saida - self.entrada
        valor = tempo / 10.0
        return max(5.00, valor)
    
class Estacionamento:
    def __init__(self):
        self.veiculos = []
        self.hora_atual = 0

    def estacionar(self, tipo: str, id: str):
        novo_veiculo = None
        if tipo == "bike":
            novo_veiculo = Bike(id, self.hora_atual)
        elif tipo == "moto":
            novo_veiculo = Moto(id, self.hora_atual)
        elif tipo == "carro":
            novo_veiculo = Carro(id, self.hora_atual)

        if novo_veiculo:
            self.veiculos.append(novo_veiculo)

    def passar_tempo(self, tempo: int):
        self.hora_atual += tempo

    def pagar(self, id: str):
        veiculo = next((v for v in self.veiculos if v.id == id), None)

        if veiculo:
            valor = veiculo.calcular_valor(self.hora_atual)
            print(f"{veiculo.tipo} chegou {veiculo.entrada} saiu {self.hora_atual}. Pagar R$ {valor:.2f}")
            self.veiculos.remove(veiculo)
        else:
            print("Veiculo nao encontrado")

    def show(self):
        for v in self.veiculos:
            print(v)
        print(f"Hora atual: {self.hora_atual}")

def main():
    estacionamento = Estacionamento()

    while True:
        try:
            line = input()
            if not line:
                continue

            print(f"${line}")
            parts = line.split()
            cmd = parts[0]

            if cmd == "end":
                break
            elif cmd == "show":
                estacionamento.show()
            elif cmd == "tempo":
                estacionamento.passar_tempo(int(parts[1]))
            elif cmd == "estacionar":
                estacionamento.estacionar(parts[1], parts[2])
            elif cmd == "pagar":
                estacionamento.pagar(parts[1])

        except EOFError:
            break

if __name__ == "__main__":
    main()
