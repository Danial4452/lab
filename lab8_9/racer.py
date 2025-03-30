import pygame
import random
import time
import sys
from pygame.locals import *


pygame.init()
pygame.mixer.init()


FPS = 60
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
COINS_COLLECTED = 0


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racing Game")


font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)  


try:
    pygame.mixer.music.load('background.wav')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)
    
    crash_sound = pygame.mixer.Sound('crash.wav')
    crash_sound.set_volume(0.3)  
    coin_sound = pygame.mixer.Sound('coin.wav')
    coin_sound.set_volume(0.3)
except Exception as e:
    print(f"Ошибка загрузки звуков: {e}")
    class DummySound:
        def play(self): pass
    crash_sound = DummySound()
    coin_sound = DummySound()


try:
    background = pygame.image.load("AnimatedStreet.png").convert()
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    enemy_img = pygame.image.load("Enemy.png").convert_alpha()
    player_img = pygame.image.load("Player.png").convert_alpha()
except:
    print("Фон не загружен, используется запасной вариант")
    background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background.fill(WHITE)


class ScrollingBackground:
    def __init__(self):
        self.y = 0
        self.speed = SPEED
        
    def update(self):
        self.y += self.speed
        if self.y >= SCREEN_HEIGHT:
            self.y = 0
            
    def draw(self, surface):
        surface.blit(background, (0, self.y))
        surface.blit(background, (0, self.y - SCREEN_HEIGHT))


class GameObject:
    def __init__(self, image, position):
        self.image = image
        self.rect = self.image.get_rect(center=position)
    
    def update(self, speed):
        self.rect.move_ip(0, speed)
    
    def draw(self, surface):
        surface.blit(self.image, self.rect)


def reset_game():
    global SCORE, SPEED, enemies, coins, COINS_COLLECTED
    SCORE = 0
    SPEED = 5
    COINS_COLLECTED = 0
    enemies = []
    coins = []

player = GameObject(pygame.transform.scale(player_img, (95, 100)), (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100))
player.rect.inflate_ip(-player.rect.width * 0.2, -player.rect.height * 0.2)  
enemies = []
coins = []
scrolling_bg = ScrollingBackground()


clock = pygame.time.Clock()
running = True
game_over = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == INC_SPEED:
            SPEED += 0.5
            scrolling_bg.speed = SPEED

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT] and player.rect.left > 0:
            player.rect.move_ip(-5, 0)
        if keys[pygame.K_RIGHT] and player.rect.right < SCREEN_WIDTH:
            player.rect.move_ip(5, 0)

        if random.randint(1, 100) == 1:
            enemies.append(GameObject(enemy_img, (random.randint(40, SCREEN_WIDTH - 40), 0)))

        if random.randint(1, 100) == 1:
            coins.append(GameObject(pygame.Surface((20, 20)), (random.randint(20, SCREEN_WIDTH - 20), 0)))
            coins[-1].image.fill(YELLOW)

        for enemy in enemies[:]:
            enemy.update(SPEED)
            if enemy.rect.top > SCREEN_HEIGHT:
                enemies.remove(enemy)
            if player.rect.colliderect(enemy.rect):
                game_over = True
                crash_sound.play()

        for coin in coins[:]:
            coin.update(SPEED // 2)
            if coin.rect.top > SCREEN_HEIGHT:
                coins.remove(coin)
                continue
            if player.rect.colliderect(coin.rect):
                COINS_COLLECTED += 1
                coin_sound.play()
                coins.remove(coin)

    DISPLAYSURF.fill(BLACK)
    scrolling_bg.update()
    scrolling_bg.draw(DISPLAYSURF)

    for enemy in enemies:
        enemy.draw(DISPLAYSURF)

    for coin in coins:
        coin.draw(DISPLAYSURF)

    player.draw(DISPLAYSURF)

    coins_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, WHITE)
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 100, 10))

    if game_over:
        game_over_text = font.render("Game Over", True, BLACK)
        DISPLAYSURF.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 30))
        

    pygame.display.update()
    clock.tick(FPS)


pygame.mixer.music.stop()
pygame.quit()
sys.exit()