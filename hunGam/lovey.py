import pygame
import random

pygame.init()
WIDTH = 800
HEIGHT = 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("I love you")
pygame.display.set_icon(pygame.image.load("hunGam/images/luvIcon.png"))

#color defs
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class paddle():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.wid = 30
        self.hei = 150
    
    def drop_it_like_its_HOT(self):
        win.fill(WHITE, pygame.rect.Rect(self.x, self.y, self.wid, self.hei))
    
    def move(self, up:bool):
        move = 40
        if up:
            self.y -= move
            if self.y < 0:
                self.y = 0
        else:
            self.y += move
            if self.y > 450:
                self.y = 450

class ballz(paddle):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.wid = 30
        self.hei = 30
        self.vel = [2, -2]

    def move(self):
        self.x += self.vel[0]
        self.y += self.vel[1]
        if self.y > 570:
            self.y = 569
            self.vel[1] = -2
        elif self.y < 0:
            self.y = 1
            self.vel[1] = 2
        
        if (self.x > 2):
            pass

def start():
    pass

def main():

    p1 = paddle(20, 30)
    p2 = paddle(750, 30)
    ball = ballz(380, 280)

    run = True
    while run:

        win.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    p2.move(False)
                elif event.key == pygame.K_UP:
                    p2.move(True)
                elif event.key == pygame.K_w:
                    p1.move(True)
                elif event.key == pygame.K_s:
                    p1.move(False)
        
        ball.move()
        print(ball.x, ball.y)
        p1.drop_it_like_its_HOT()
        p2.drop_it_like_its_HOT()
        ball.drop_it_like_its_HOT()

        pygame.display.flip()

if __name__ == "__main__":
    main()