import pygame 

pygame.init()

window = pygame.display.set_mode((700, 500))

def incializa():
    # window = pygame.display.set_mode((700, 500))
    pygame.display.set_caption('Jogo da Memória')

    window.fill((0, 0, 0))
    pygame.display.flip()

    return window


def recebe_eventos():

    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
                pygame.quit()


def desenha():
    pass

def game_loop(window):     ## equivalente ao while GAME
# : receber assets como argumento e repassar para desenha
    while recebe_eventos():  
       
        desenha(window)  #adcionar assets depois

if __name__ == '__main__':
        ##-- : receber assets aqui e repassar para game_loop
    # w , assets = inicializa()
   
    # window.fill((0, 0, 0))
 
    game_loop(window)  #window=, assets