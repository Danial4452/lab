
import pygame


pygame.init()


SCREEN_WIDTH = 700
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

BLACK = (0,0,0)
RED = (255, 0, 0)


BALL_RADIUS = 25
BALL_SIZE = 50  
ball_x = (SCREEN_WIDTH - BALL_SIZE) // 2 
ball_y = (SCREEN_HEIGHT - BALL_SIZE) // 2  
BALL_SPEED = 7


clock = pygame.time.Clock()


running = True
while running:
    clock.tick(60)

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_y - BALL_SPEED >= 0: 
        ball_y -= BALL_SPEED
    if keys[pygame.K_DOWN] and ball_y + BALL_SPEED <= SCREEN_HEIGHT - BALL_SIZE:  
        ball_y += BALL_SPEED
    if keys[pygame.K_LEFT] and ball_x - BALL_SPEED >= 0:  
        ball_x -= BALL_SPEED
    if keys[pygame.K_RIGHT] and ball_x + BALL_SPEED <= SCREEN_WIDTH - BALL_SIZE:  
        ball_x += BALL_SPEED
        
    screen.fill(BLACK)

    

    pygame.draw.circle(screen, RED, (ball_x + BALL_RADIUS, ball_y + BALL_RADIUS), BALL_RADIUS)

   
    pygame.display.flip()

pygame.quit()