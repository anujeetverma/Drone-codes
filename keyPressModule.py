import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))
    return win

def getKey(KeyName):
    ans = False
    for event in pygame.event.get(): pass



if __name__ == '__main__':
    init()