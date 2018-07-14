import pygame
import random
import time

pygame.init()

# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.SysFont("monospace", 15)

clock = pygame.time.Clock()

GREEN = (20, 255, 140)
GREY = (210, 210, 210)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
BLUE = (100, 100, 255)
BLACK = (0, 0, 0)
colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE, GREY)
SCREENWIDTH = 1400  # normal is 1400
SCREENHEIGHT = 800  # normal is 800
size = (SCREENWIDTH, SCREENHEIGHT)

# screen = pygame.display.set_mode(size)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)


class Dynabox:
    """ Represent a dynabox in all its magic"""

    def __init__(self, sentin):
        self.x = random.randint(50, 700)
        self.y = random.randint(50, 590)
        self.w = random.randint(50, 200)
        self.h = random.randint(50, 200)
        self.xv = random.randint(-20, 20) / 10
        self.yv = random.randint(-20, 20) / 10
        self.bx = 1
        self.by = int(self.h / 4)
        self.byv = random.choice([-1, 1])
        self.bxv = random.choice([-1, 1])
        self.type = random.choice([1, 2])
        self.sentin = sentin

    def show(self):
        pygame.draw.rect(screen, RED, (self.x, self.y, self.w, self.h), 3)
        pygame.draw.circle(screen,
                           BLUE,
                           (int(self.x) + self.bx,
                            int(self.y) + self.by), 10, 1)
        # render text
        message = str(self.sentin)
        label = myfont.render(message, 1, (255, 255, 0))
        screen.blit(label, (self.x + self.bx - 4, self.y + self.by - 4))

    def updateinterior(self):

        if internalmode == 1:
            if self.type == 2:
                self.byv += 1
        elif internalmode == 3:
            self.byv += 1
        else:
            pass

        self.bx += self.bxv
        self.by += self.byv

        if self.bx > self.w or self.bx < 0:
            self.bx -= self.bxv
            self.bxv = -self.bxv
        if self.by > self.h or self.by < 0:
            self.by -= self.byv
            self.byv = -self.byv

    def updateexterior(self):
        self.x += self.xv
        self.y += self.yv
        if self.x + self.w > SCREENWIDTH or self.x < 0:
            self.x -= self.xv
            self.xv = -self.xv
        if self.y + self.h > SCREENHEIGHT or self.y < 0:
            self.y -= self.yv
            self.yv = -self.yv

familysize = 20
internalmode = 1  # 1=normal, 3=force bouncy, 2= force pong
carryon = True
db = [Dynabox(x) for x in range(familysize)]

while carryon:

    clock.tick(100)
    # print("ticks " + str(pygame.time.get_ticks() ))
    print("fps " + str(clock.get_fps()))  # requires clock.tick on and shows its limiting

    # INPUT phase   i   i   i   i   i   i   i   i   i   i   i   i   i   i
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryon = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        carryon = False
    if keys[pygame.K_1]:
        screen.fill(BLACK)
        time.sleep(0.5)
    if keys[pygame.K_0]:
        time.sleep(5)
    if keys[pygame.K_3]:
        internalmode += 1
        time.sleep(0.5)
        if internalmode > 3:
            internalmode = 1

    # UPDATE phase u   u   u   u   u   u   u   u   u   u   u   u   u   u   u

    for z in range(familysize):
        db[z].updateexterior()
        db[z].updateinterior()

    # DRAW phase d   d   d   d   d   d   d    d    d   d   d    d   d   d   d

    screen.fill(BLACK)

    for z in range(familysize):
        db[z].show()

    # render text
    uimodemessage = str(internalmode)
    uilabel = myfont.render(uimodemessage, 1, (20, 20, 255))
    screen.blit(uilabel, (20, 20))

    pygame.display.flip()

pygame.quit()
