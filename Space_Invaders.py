import pygame

#Initalize the module
pygame.init()

#Window display
gameWindow = pygame.display.set_mode((600, 800))

#Title of the game and game logo
title = pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceinvadersicon.png")
pygame.display.set_icon(icon)

#Background
background_image = pygame.image.load("background68.png")

#Player
player_image = pygame.image.load("space-invaders-ship.png")
player_x = 284
player_y = 750
player_change_x = 0

#Invader
invader_image = pygame.image.load("invader.png")
invader_y = 32
invader_x = 16
invader_change = 3

#Bullet
#Ready - No bullet on the screen
#Fire - Bullet is moving on the screen
bullet = pygame.image.load("bullet.png")
#bullet_x = 0
bullet_y = 700
#bullet_change_x = 0
bullet_change_y = 40
bullet_state = "ready"

#Player function
def player(x, y):
    gameWindow.blit(player_image, (player_x, player_y))

#Invader function
def invader(x, y, num):

    #Risanje
    for i in range(0, num):
        x = x + 64
        y = y + 32
        gameWindow.blit(invader_image, (x, invader_y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    gameWindow.blit(bullet, (x+16, y+10))

#Game loop
runGame = True

while runGame:
    # Background color - Navy blue
    gameWindow.fill((0, 0, 128))

    # Background image
    gameWindow.blit(background_image, (0, 0))

    for event in pygame.event.get():
        #Quit commands
        if event.type == pygame.QUIT:
            runGame = False

        #Key commands
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change_x = -5
            if event.key == pygame.K_RIGHT:
                player_change_x = 5
            if event.key == pygame.K_SPACE:
                fire_bullet(player_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change_x = 0

    #
    #Adding/subtracting player/invader the coordinates
    player_x += player_change_x
    invader_y += invader_change

    #
    #Bullet movement
    if bullet_state == "fire":
        fire_bullet(player_x, bullet_y)
        bullet_y -= bullet_change_y

    #
    #Borders
    if player_x <= 0:
        player_x = 0
    elif player_x >= 568:
        player_x = 568
    if invader_y >= 600:
        invader_y = 600

    #
    #Player call under screen and above update
    player(player_x, player_y)
    invader(invader_x, invader_y, 7)
    #Window update - Display must be updating
    pygame.display.update()


