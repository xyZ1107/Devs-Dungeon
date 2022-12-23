import os.path

cwd = os.path.dirname(__file__)

WIDTH, HEIGHT = (1280, 720)
FPS = 60

states = {'off': False, 'on': True}

block_images = [f'{cwd}/Assets/b_down.png', 
                f'{cwd}/Assets/b_up.png', 
                f'{cwd}/Assets/b_left.png', 
                f'{cwd}/Assets/b_right.png']

enemy_images = [f'{cwd}/Assets/enemyblue', 
                f'{cwd}/Assets/enemygreen', 
                f'{cwd}/Assets/enemyorange', 
                f'{cwd}/Assets/enemyyellow']

black = (0, 0, 0)