import pygame, sys, os.path
from config import *
import block
import enemy

class run:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Run! Pygame Project')
        self.game_state = states.get('off')
        
        self.sprite = block.Block((WIDTH/2, HEIGHT/2))
        self.block_group = pygame.sprite.Group(self.sprite)


    def loop(self):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')

            self.block_group.update()
            self.block_group.draw(self.screen)
            

            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = run()
    game.loop()

