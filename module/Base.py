import abc
from module.Armas import Arma

class GameArt ():
    def __init__(self):
        
        self.titu = """
                                                   (                               (                             
                    *   )   )        ))                            )) (                        
                    ` )  /(( /(   (   (()/(  (      ) (  (            (()/( )) (      (  (       
                    ( )(_))()) ))   /(_)) )(  ( /( )))( (   (      /(_)|(_| /( ))  )))(  (   )
                  ( (_(_()|(_) /((_) (_))_ (() )(_)|(_)) )  ) )  (_)__ ())(__()) _ )(_)|()/( / 
                  |_   _| |(_|_))    |_   _| ((_|(_)_ (()(_|(_)_(_/(  |  | ^ |  ||(|| ((_)_ )(_)|) 
                    | | | ' \/ -_)     | |   /__  / -_)| / / _` | |   |   / \   |/ _` ||  _)/__ 
                    |_| |_||_\___|   |_____|/___/ \___||_\_\__,_| |   |__/   \__|\__,_|| | /____/
                                                                
                                                    
                    A game by pankercito (Eiker Rodriguez)  
                    
                    """
        self.line = "\n==============================================================================="

    def titulo(self):
        
        print(self.titu)
    
    def linea(self):
        print(self.line)

class Personaje (metaclass = abc.ABCMeta):
    def __init__(self, Maxima: int, nombre: str, arma: 'Arma'):
        self.vida_Maxima = Maxima
        self.nombre = nombre
        self.arma = arma
        self.vida = self.vida_Maxima
        
    def Stats(self):
        print(f"Vida: {self.vida} / {self.vida_Maxima}")
        print(f"Nombre: {self.nombre}")
        print(f"Arma: {self.arma.nombreArma()}")
        print(f"Daño: {self.arma.PuntosDeDanno()}")  
              
    def PreAtack (self):
        return self.arma.PuntosDeDanno()
    
    def RecibeAttk(self, monstro: 'Personaje') -> None:
        self.vida -= monstro.PreAtack()
        
        if self.vida < 0:
            self.vida = 0
    
    def Atacar (self, RecibeDano: 'Personaje') -> None:
        RecibeDano.RecibeAttk(self)
        
    def ComprobarVid (self):
        if self.vida == 0: 
            return False 
        else: 
            return True
