from module.Armas import Arma, Espada, Varita, Daga, Lanza, Arco
from module.Base import Personaje

def getArma(int):
    if int == 1: return Espada()
    if int == 2: return Varita()
    if int == 3: return Arco()
    if int == 4: return Lanza()

class Goblin (Personaje):
    def __init__(self):
        super().__init__(20, "Goblin", Daga())


class Jugador (Personaje):
    def __init__(self, nombre: str, clase):
        super().__init__(100, nombre, getArma(clase)) # type: ignore

    def Curar(self) -> None:
        self.vida += 8
        if self.vida > self.vida_Maxima:
            print("¡haz alcanzado la vida maxima!")
            self.vida = self.vida_Maxima