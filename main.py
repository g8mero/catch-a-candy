import pygame
import random

pygame.init()
score_font = pygame.font.Font("assets/karmatic-arcade.ttf", 19)


window = pygame.display.set_mode((400, 600))
bg = pygame.image.load("assets/bg.png")
bg = pygame.transform.scale(bg,(400,600))
pygame.display.set_caption("Catch the Candy")

score = 0
score_text = score_font.render(f"Score: {score}", True, (255, 255,255))
lives = 3
lives_text = score_font.render(f"Lives: {lives}", True, (255, 255,255))

player = pygame.surface.Surface((100,100))
player.fill((255,255,255))
player = pygame.image.load("assets/cat-sprite.png").convert_alpha()
player = pygame.transform.scale(player,(100,100))
player_x = 0
player_y=400
player_vel_x=0
player_vel_y=0

candy = pygame.surface.Surface((100,100))
candy.fill((255,255,255))
candy = pygame.image.load("assets/candy-sprite.png").convert_alpha()
candy = pygame.transform.scale(candy,(50,50))
candy_x = random.randint(0,window.width-candy.width)
candy_y=0
candy_vel_x=0
candy_vel_y=8

def collision_detection():
    return (
        candy_x < player_x + player.width and
        candy_x + candy.width > player_x and
        candy_y < player_y + player.height and
        candy_y + candy.height > player_y
    )

game_state = 0
clock = pygame.time.Clock()

while True: 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_state = 1
                score = 0
                lives = 3
                lives_text = score_font.render(f"Lives: {lives}", True, (255, 255, 255))
                score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
            if event.key == pygame.K_LEFT:
                player_vel_x = -6
            if event.key == pygame.K_RIGHT:
                player_vel_x = 6
        else: 
            player_vel_x = 0
            player_vel_y = 0

    if game_state == 1:
        if candy_y >= window.height:
            candy_y=0
            candy_x=random.randint(0,window.width-candy.width)
        if collision_detection():
            score +=1 
            score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
            candy_vel_y+=0.1
            candy_y = 0
            candy_x=random.randint(0,window.width-candy.width)
            
        if candy_y > 550:
            lives -= 1
            candy_y = 0
            candy_x=random.randint(0,window.width-candy.width)
            lives_text = score_font.render(f"Lives: {lives}", True, (255, 255, 255))
            if lives < 1:
                game_state = 2

    #output
    window.fill((255,255,255))
    window.blit(bg, (0,0))
    if game_state == 0:
        welcome_text = score_font.render("Welcome to Catch the Candy", True, (255, 255, 255))
        welcome_text1 = score_font.render("Press SPACE to start", True, (255, 255, 255))
        window.blit(welcome_text, (8, 600 // 2 - 50))
        window.blit(welcome_text1, (50, 600 // 2))

        
    if game_state == 1:
        player_x += player_vel_x
        player_y += player_vel_y

        candy_x += candy_vel_x
        candy_y += candy_vel_y

        window.blit(player, (player_x,player_y))
        window.blit(candy, (candy_x,candy_y))
        window.blit(score_text, (15, 15))
        window.blit(lives_text, (300, 15))
        
    if game_state == 2:
        game_over_text = score_font.render("GAME OVER", True, (255, 255, 255))
        try_again = score_font.render("Press SPACE to try again", True, (255, 255, 255))
        window.blit(game_over_text, (140, 250))
        window.blit(score_text, (150, 300))
        window.blit(try_again, (25, 350))
    
    pygame.display.flip()
    clock.tick(60)

