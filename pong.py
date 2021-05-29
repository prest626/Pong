import pygame, sys, random

def ball_animation():
    global ball_speed_x, ball_speed_y, opponent_score, player_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        ball_restart()
        player_score+=1
    if ball.right >= screen_width:
        ball_restart()
        opponent_score+=1
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1



def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom>ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

def ball_restart():
    global ball_speed_y, ball_speed_x
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))

def p2():
    opponent.y += opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height

pygame.init()
clock = pygame.time.Clock()


screen_width = 900
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong")

#Getting the player rectangles
ball = pygame.Rect(screen_width/2-15, screen_height/2-15, 30, 30)
player = pygame.Rect(screen_width-20, screen_height/2-70, 10, 140)
opponent = pygame.Rect(10, screen_height/2-70, 10, 140)
#making the colors
bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

#game variables
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7
multiplayer = 1


#text variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 30)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed+=7
            if event.key == pygame.K_UP:
                player_speed-=7

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed-=7
            if event.key == pygame.K_UP:
                player_speed+=7
        



    ball_animation()
    player_animation()
    opponent_ai()
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2, 0), (screen_width/2, screen_height))

    player_text = game_font.render(f"{player_score}", False,light_grey)
    screen.blit(player_text, (460, 200))

    opponent_text = game_font.render(f"{opponent_score}", False, light_grey)
    screen.blit(opponent_text, (425, 200))
    #Updating the window
    pygame.display.flip()
    clock.tick(60)
