import abc

class Arma(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def PuntosDeDanno(self) -> int:
        pass
    
    @abc.abstractmethod
    def nombreArma(self) -> str:
        pass
    
class Varita(Arma):
    def PuntosDeDanno(self) -> int:
        return 8
    def nombreArma(self) -> str:
        return "Varita"

class Espada(Arma):
    def PuntosDeDanno(self) -> int:
        return 5
    
    def nombreArma(self) -> str:
        return "Espada"

class Daga(Arma):
    def PuntosDeDanno(self) -> int:
        return 4
    
    def nombreArma(self) -> str:
        return "Daga"
    
class Lanza(Arma):
    def PuntosDeDanno(self) -> int:
        return 6
    
    def nombreArma(self) -> str:
        return "Lanza"
    
class Arco(Arma):
    def PuntosDeDanno(self) -> int:
        return 7
    
    def nombreArma(self) -> str:
        return "Arco"
    