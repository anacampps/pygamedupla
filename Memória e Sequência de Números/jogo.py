import pygame 

pygame.init()

def incializa():
    pass

def recebe_eventos():
    pass


def desenha():
    pass

def game_loop(window):     ## equivalente ao while GAME
# : receber assets como argumento e repassar para desenha
    while recebe_eventos():  
       
        desenha(window)  #adcionar assets depois

if __name__ == '__main__':
        ##-- : receber assets aqui e repassar para game_loop
    # w , assets = inicializa()
   
    
 
    game_loop()  #window=, assets