from module.Base import GameArt
from module.Personaje import Goblin, Jugador


GameArt().titulo() #flamas
GameArt().linea()
print()
print("si. start game")
print("no. exit")
GameArt().linea()
init = input("comenzar: ")

while init == 'si':
        # iniciador de juegos
    if init == 'si':
        nombreJugador = input("ingrese nombre del jugador: ")
        GameArt().linea()
        print(" ")
        print(f'=============== {nombreJugador} ===============')
        print("1. Guerrero")
        print("2. Mago")
        print("3. Arquero")
        print("4. Lancero")
        GameArt().linea()
            
        clase = int(input("seleccione la clase del jugador: "))

        if clase > 0 & clase < 5:
            
            jugador  = Jugador(nombreJugador, clase)
            
            # mostrar estadisticas de jugador
            print(f'=============== {jugador.nombre} ===============')
            jugador.Stats();
            GameArt().linea()    
            
            # acciones 
            print(f'=============== {jugador.nombre} ===============')
            print("1. Explorar")
            print("2. Habilidades")
            print("3. Inventario")
            print("4. Salir")
            GameArt().linea()    
                    
            action = input("moviento: ")
            
            while action != "4":
                if action == '1': 
                    GameArt().linea() 
                    macana = Goblin()
                            
                    GameArt().linea()
                    print("has encontrado un enemigo")
                    macana.Stats()
                    GameArt().linea() 
                    
                    print("¡Goblin a atacado!")
                    GameArt().linea() 
                    macana.Atacar(jugador)
                    
                    
                    if int(action) == 1:                
                        while macana.ComprobarVid() == True: 
                            # mostrar estadisticas de jugador
                            print(f'=============== {jugador.nombre} ===============')
                            jugador.Stats()
                            GameArt().linea()  
                            macana.Stats()
                                
                            print(f'=============== {jugador.nombre} ===============')
                            print("1. Atacar")
                            print("2. Habilidades")
                            print("3. Inventario")
                            print("4. Correr")
                            GameArt().linea() 
                            
                            
                                    
                            queHacer = input("que hacer: ")
                            GameArt().linea()
                            
                            if queHacer == '1': 
                                jugador.Atacar(macana)
                                print(f"¡{jugador.nombre} a atacado!")
                                GameArt().linea() 
                                
                            if queHacer == '2':
                                # acciones 
                                print(f'=============== {jugador.nombre} ===============')
                                print(f'=============== HABILIDADES ===============')
                                print("1. Curar")
                                print("4. Salir")
                                GameArt().linea()    

                                habilidad = input("utilizar: ")
                                if habilidad == '1':
                                    print(f'¡{jugador.nombre} se a curado!')
                                    jugador.Curar()
                                    GameArt().linea()
                                    
                            # comprobar estado de enemigo
                            if macana.ComprobarVid() == False:
                                continue  
                            
                            print("¡Goblin a atacado!")
                            GameArt().linea()
                            macana.Atacar(jugador)
                        else:
                            print(f"¡{macana.nombre} a muerto!")               
        
                if action == '2':
                    # acciones 
                    print(f'=============== {jugador.nombre} ===============')
                    print(f'=============== HABILIDADES ===============')
                    print("1. Curar")
                    print("4. Salir")
                    GameArt().linea()    

                    habilidad = input("utilizar: ")
                    if habilidad == '1':
                        print(f'¡{jugador.nombre} se a curado!')
                        jugador.Curar()
                        GameArt().linea() 
                         
                # mostrar estadisticas de jugador
                print(f'=============== {jugador.nombre} ===============')
                jugador.Stats();
                GameArt().linea()    
                
                # acciones 
                print(f'=============== {jugador.nombre} ===============')
                print("1. Explorar")
                print("2. Habilidades")
                print("3. Inventario")
                print("4. Salir")
                GameArt().linea()    
                action = input("moviento: ")
        else:
            print("elije bien")       
    elif init == 'no':
        print("cobarde")
    else: 
        print("elija una opcion")
    
    input("comenzar: ")
    