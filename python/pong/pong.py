import pygame
from pygame.locals import *



def draw_game_screen():
    screen.blit(bg,(0,0))
    screen.blit(paddle1, (10, l_paddle_pos))
    screen.blit(paddle2, (620, 100))
    screen.blit(ball, (ball_pos_x, ball_pos_y))

    # Scores
    l_score_str = font.render(str(l_score), True, (0,0,0))
    r_score_str = font.render(str(r_score), True, (0,0,0))
    screen.blit(l_score_str, (50,10))
    screen.blit(r_score_str, (560,10))

def move_ball():
    """ Update the position of the ball and check if it has hit the paddle or
        the edge of the screen """
    global ball_pos_x, ball_pos_y
    global ball_speed_x, ball_speed_y
    global l_paddle_pos, l_paddle_speed
    global l_score, r_score
    
    ball_pos_x += ball_speed_x
    ball_pos_y += ball_speed_y
    if l_paddle_pos + l_paddle_speed > 0 and l_paddle_pos + l_paddle_speed < 430:
        l_paddle_pos += l_paddle_speed

    relative_pos_l = ball_pos_y - l_paddle_pos

    if ball_pos_x <= 20 and relative_pos_l > -8 and relative_pos_l < 50:
        ball_speed_x = -ball_speed_x
    if ball_pos_x > 604:
        ball_speed_x = -ball_speed_x
    if ball_pos_y <= 0 or ball_pos_y > 464:
        ball_speed_y = -ball_speed_y
    if ball_pos_x <= 0 or ball_pos_x > 624:
        if ball_pos_x <= 0:
            r_score += 1
        else:
            l_score += 1
        ball_speed_x = -ball_speed_x
        ball_pos_x += 10 * ball_speed_x
        ball_pos_y = 200

def handle_user_input():
    """ Handle any keys pressed or released by the user """
    global game_over
    global l_paddle_speed
    for event in pygame.event.get():
        if event.type == QUIT:
            game_over = True
        elif event.type == KEYDOWN:
            if event.key == ord('s'):
                l_paddle_speed = max_paddle_speed
            elif event.key == ord('w'):
                l_paddle_speed = -max_paddle_speed
        elif event.type == KEYUP:
            if event.key == ord('s') or event.key == ord('w'):
                l_paddle_speed = 0
                
    
    

pygame.init()

screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("Pong!")

bg = pygame.Surface((640,480))
bg.fill((255,255,255))

paddle1 = pygame.Surface((10,50))
paddle1.fill((255,0,0))

paddle2 = pygame.Surface((10,50))
paddle2.fill((0,255,0))

ball = pygame.Surface((16,16))
ball = pygame.transform.scale(ball, (16,16))
#ball.fill((255,255,255))
#pygame.draw.circle(ball, (0,0,255), (8,8), 8)

clock = pygame.time.Clock()
font = pygame.font.SysFont("calibri",40)

ball_pos_x = 320
ball_pos_y = 240
ball_speed_x = 5
ball_speed_y = 5
max_paddle_speed = 5
l_paddle_pos = 50
l_paddle_speed = 0

l_score = 0
r_score = 0

game_over = False

while not game_over:
    handle_user_input()
            
    draw_game_screen()
    
    move_ball()
        
        
    pygame.display.flip()
    clock.tick(30)


pygame.quit()
