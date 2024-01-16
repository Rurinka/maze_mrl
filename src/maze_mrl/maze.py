# import pygame
#
# pygame.init()
# screen = pygame.display.set_mode((640, 480))
# pygame.display.set_caption("Hello World")
# while True:
#    for event in pygame.event.get():
#       if event.type == pygame.QUIT:
#          pygame.quit()
#
size = 10
maze = [["██" for j in range(size)] for i in range(size)]
print('\n'.join([''.join(i) for i in maze]))
