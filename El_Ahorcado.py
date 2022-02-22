
def play_ahorcado():
    '''
    Esta función es utilizada para jugar al Juego del Ahocardo. 
    Una vez iniciado el juego, se solicitarán dos inputs: 
        palabra_adivinar -> string
        intentos -> integer
    '''

    palabra_adivinar = list(input("Guardian! Introduzca la palabra que el condenado debe adivinar para salvar su vida: ").upper())

        #Indicamos que solamente hay 6 intentos (para ello, utilizamos un "while", y cuando se acaben los intentos, hacemos un "break")
    intentos = int(input("Guardián, introduzca el número de vidas que le concedes al condenado: "))

    print("Querido condenado, ¡Ya no hay vuelta atrás! Comienza el juego del AHORCADO! Esperemos que sobrevivas a esta temerosa experiencia, ¡jejejejeje!")

    '''Generaremos una palabra que no revele pero que indique el número de letras que contiene la palabra a adivinar:'''
    palabra_camuflada = list("_" * len(palabra_adivinar))
    print("La palabra a adivinar es: ", " ".join(palabra_camuflada)) #Lo mostraremos por pantalla

    while intentos >= 0:
        import time #Por si acaso, para que no se quede pensando infinitamente
        time.sleep(1) 

        import random #Para que haya más variedad en el juego
        adjetivos_bonitos_para_nuestro_condenado = ["rata de dos patas", "pecho frío", "mequetrefe sin patillas", "estropajo invertebrado", \
            "bicho bola sin escrúpulos", "oso malpeinado", "majadero", "bestia inmunda", "bicharaco con plumas", "brontosaurio escapado de la prehistoria", \
                "mercader de alfombras", "trozo de mula con patas", "calabacín diplomado", "troglodita sin cerebro", "lengua de jirafa", "imberbe sin meñiques"]
        
        letra_usuario = input("Introduce una letra").upper() #Lo ponemos en mayúscula, para que coincida con nuestra palabra_adivinar
        
        #Si la letra es correcta....
        if letra_usuario in palabra_adivinar: 
            for indice, letra in enumerate(palabra_adivinar): #Hacemos un FOR__IN para añadir "letra" tantas veces como esté presente en "palabra"
                if letra == letra_usuario: #Y para añadirlo en la posición correcta a nuestra palabra_camuflada, hacemos este condicional
                    palabra_camuflada[indice] = letra
                    if "_" not in palabra_camuflada: #Si se ha adivinado todas las letras de la palabra
                        print(" ".join(palabra_camuflada))
                        print("ENHORABUENA. ¡Has salvado tu pescuezo esta vez. Mereces mis respetos, ¡", random.choice(adjetivos_bonitos_para_nuestro_condenado), "!")
                        return #Funciona como un "break", porque este último no funciona dentro de un "nested if statement"

            print(" ".join(palabra_camuflada))            
            continue
        
        #Si la letra es incorrecta...
        else:
            if intentos == 0:
                print("¡Se te acabaron los intentos, ", random.choice(adjetivos_bonitos_para_nuestro_condenado),"! nos encontraremos de nuevo, pero en el inframundo, JAJAJAJJA. ¡Ahorquenlo!")
                break
            else:
                intentos -= 1
                print("La letra ", letra_usuario, "no es correcta. Te quedan ", intentos, " intentos antes de morir. Piensa bien antes de responder, ¡", random.choice(adjetivos_bonitos_para_nuestro_condenado), "!")
                print(" ".join(palabra_camuflada))
                continue


'''Se muestra el comando que llama al juego:'''

play_ahorcado()