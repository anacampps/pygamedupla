import pygame 





def inicializa():
    window = pygame.display.set_mode((700, 500))
    pygame.display.set_caption('Jogo da Memória')

    window.fill((0, 0, 0))
   

    return window


def recebe_eventos():

    game = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
    
    return game


def desenha(window):
    window.fill((0, 0 , 0))

    pygame.draw.rect(window, (255, 255, 255), (100, 250, 500, 125))
    

    pygame.draw.rect(window,(255, 0, 0), (120, 230, 460, 75))
    
    # pygame.draw.rect(window, (255, 255, 255), (10, 10, 10, 10))

    pygame.display.update()

def game_loop(window):     ## equivalente ao while GAME

# : receber assets como argumento e repassar para desenha
    while recebe_eventos():  
        desenha(window)  #adcionar assets depois

if __name__ == '__main__':
    pygame.init()
        ##-- : receber assets aqui e repassar para game_loop
    window = inicializa()
   
    # window.fill((0, 0, 0))
 
    game_loop(window)  #window=, assets