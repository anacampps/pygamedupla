import pygame 
from funcoes_auxiliares import *

def inicializa():
    assets = {}

    font = pygame.font.get_default_font()
    font = pygame.font.Font(font, 45)

    
    assets['font'] = font                        
    assets['num gerado']= gera_num(x=2)
    

    window = pygame.display.set_mode((700, 500))
    pygame.display.set_caption('Jogo da Memória')

    window.fill((0, 0, 0))
   
    return window, assets  ##


def recebe_eventos():

    game = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
    
    return game


def desenha(window, assets):

    window.fill((0, 0 , 0))

    memorize = assets['font'].render(str('MEMORIZE....'), True, (255, 255, 255)) 
    window.blit(memorize, (200, 150))
    

    caixa_branca = pygame.draw.rect(window, (255, 255, 255), (100, 250, 500, 125))

    caixa_vermelha = pygame.draw.rect(window,(255, 0, 0), (120, 230, 460, 75))
    
    # pygame.rect


    num_gerado= assets['font'].render(str(assets['num gerado']),True, (0, 0 , 0))
    window.blit(num_gerado, (320, 240))
    ##-------Aqui implementamos a primeira fase: 2 digitos--------

    
    digite= assets['font'].render(str(['Digite']), True, (255, 255 ,255))
    window.blit(digite, (200, 150))
    
    if num_gerado== True:
        memorize= digite 
        

    pygame.display.update()


def game_loop(window, assets):   ##  ## equivalente ao while GAME

# : receber assets como argumento e repassar para desenha
    while recebe_eventos():  
        desenha(window, assets)  ##         #adcionar assets depois

if __name__ == '__main__':
    pygame.init()
        ##-- : receber assets aqui e repassar para game_loop
    window, assets = inicializa() ##
   
    # window.fill((0, 0, 0))
 
    game_loop(window,assets)  ##