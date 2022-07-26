import pygame
from network import Network
from enemy import Enemy_Manager
from player import Player
pygame.init()
pygame.font.init()
width = 800
height = 800
win = pygame.display.set_mode((width, height))

running = True

img = pygame.image.load("bg.gif")
img.convert()
rect = img.get_rect()
rect.center = width // 2, height // 2

player1_image = pygame.image.load("mario.png")
player1_image = pygame.transform.scale(player1_image, (40,59))
player1_rect = player1_image.get_rect()

player2_image = pygame.image.load("luigi.png")
player2_image = pygame.transform.scale(player2_image, (40,59))
#player2_rect = player2_image.get_rect()

enemy_image = pygame.image.load("enemy.png")
enemy_image = pygame.transform.scale(enemy_image, (40, 59))

moving = False
level = 1

pygame.display.set_caption("Client")


# catImg = pygame.image.load("cat (1).png").convert()
# dogImg = pygame.image.load("dog.png").convert()


def redrawWindow(win, player, player2, enemy):
    win.blit(img, rect)
    player.draw(win, player1_image, player1_image.get_rect())
    player2.draw(win, player2_image, player2_image.get_rect())
    enemy.draw(win, enemy_image, enemy_image.get_rect())

    font_colour = (0, 0, 0)
    if player.score == 3:
        fontx = pygame.font.Font(None, 100)
        textx = fontx.render("Player 1 Wins", True, (255, 0, 0))
        win.blit(textx, (200, 200))
    elif player2.score == 3:
        fontx = pygame.font.Font(None, 100)
        textx = fontx.render("Player 2 Wins", True, (255, 0, 0))
        win.blit(textx, (200, 200))

    font1 = pygame.font.Font(None, 50)
    text1 = font1.render(str(player.score), True, font_colour)
    font2 = pygame.font.Font(None, 50)
    text2 = font2.render(str(player2.score), True, font_colour)
    win.blit(text1, (150, 50))
    win.blit(text2, (650, 50))
        if player.y < 40:
        player.y = 700
        player2.y = 700
        player.score += 1
    elif player2.y < 40:
        player.y = 700
        player2.y = 700
        player2.score += 1
    pygame.display.flip()

#p = Player(340, 700, 50, 50)#, (255, 0, 0))
#p2 = Player(480, 700, 50, 50)

def main():
    run = True
    n = Network()
    n.getIP()
    p = n.connect()
    #p = n.getP()
    enemy = Enemy_Manager(50, 50, width, height)
    enemy.create_car_lanes()
    pygame.init()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
        enemy.update_cars()
        p.move()
        if enemy.detect_collision(p):
            p.go_to_start()
            p2.score += 1

        redrawWindow(win, p, p2, enemy)


main()
