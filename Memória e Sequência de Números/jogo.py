import pygame 
from funcoes_auxiliares import *

def inicializa(): ##-- não tem argumento porque apenas cria coisas sem depender de nada (informações externas) --##
    assets = {}

    font = pygame.font.get_default_font()
    font = pygame.font.Font(font, 45)

    
    assets['font'] = font                        
    assets['num gerado']= gera_num(x=2)

    assets['fase'] = 'Memorizar'
    tempo_passado = pygame.time.get_ticks()
    assets['tempo_passado']= tempo_passado
    assets['tempo']  = 0
    assets['qtd_dígitos_seq_num'] = 2
    

    window = pygame.display.set_mode((700, 500))
    pygame.display.set_caption('Jogo da Memória')

    window.fill((0, 0, 0))
   
    return window, assets  ##


def recebe_eventos():

    game = True

    for event in pygame.event.get(): ##-- tudo que fica dentro do for event está relacionado com o mouse/teclado --##
        # print(event)   ## -- ótimo para achar posições da tela sem rachar a cabeça --##
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
        
                                            # if assets['tempo'] == 0:   ##-- inúteis
                                            #     tempo = pygame.time.get_ticks()
    atual = pygame.time.get_ticks()
    if atual - assets['tempo_passado'] > 4000:
        assets['fase'] = 'Digitar'
        assets['tempo_passado'] = atual

    
    return game


def desenha(window, assets): ##-- função (sem return): não retorna nada porque desenha na tela diretamente --##

    window.fill((0, 0 , 0))

    caixa_branca = pygame.draw.rect(window, (255, 255, 255), (100, 250, 500, 125))
    caixa_vermelha = pygame.draw.rect(window,(255, 0, 0), (120, 230, 460, 75))

    if assets['fase'] == 'Memorizar':
        memorize = assets['font'].render(str('MEMORIZE....'), True, (255, 255, 255)) 
        window.blit(memorize, (200, 150))
 
        num_gerado= assets['font'].render(str(assets['num gerado']),True, (0, 0 , 0))  #
        window.blit(num_gerado, (320, 240))
        ##-------Aqui implementamos a primeira fase: 2 digitos--------

    else: 
        digite = assets['font'].render(str('DIGITE: '), True, (255, 255 ,255)) #
        window.blit(digite, (265, 150))
     #-------------------------------------------------------------------
          
    
    # pygame.rect

        
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