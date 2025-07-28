import pygame
#ekypress checker
def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))


def getKey(KeyName):
    ans = False
    for event in pygame.event.get(): pass
    KeyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(KeyName))
    if KeyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

def main():
    if getKey('a'):
        print("left key pressed")

    if getKey('d'):
        print("right key pressed")

    if getKey('w'):
        print("up key pressed")

    if getKey('s'):
        print("down key")


if __name__ == '__main__':
    init()
    while True:
        main()