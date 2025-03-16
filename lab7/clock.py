import pygame
import os
import datetime

_image_library = {}

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image is None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

def rotate_center(surf, image, center, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    surf.blit(rotated_image, new_rect.topleft)

pygame.init()
screen = pygame.display.set_mode((900, 600))
clock = pygame.time.Clock()

background = get_image("clock.png")
minute_hand = get_image("min_hand.png")
second_hand = get_image("sec_hand.png")

center_x, center_y = 420, 320  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))
    screen.blit(background, (20, 20))

    now = datetime.datetime.now()
    minute_angle = -((now.minute % 60) * 6) 
    second_angle = -((now.second % 60) * 6) 

    rotate_center(screen, minute_hand, (center_x, center_y), minute_angle)
    rotate_center(screen, second_hand, (center_x, center_y), second_angle)

    pygame.display.flip()
    clock.tick(60)