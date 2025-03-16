import pygame
import os

pygame.init()
pygame.mixer.init()


playlist = ["gnx-kendrick-lamar-type-beat-tv-off-pt2-303828.mp3", "travis-scott-x-don-toliver-x-playboi-carti-trap-type-beat-206891.mp3", "stop-breathing-hard-energy-beat-playboi-carti-type-217806.mp3"]
current_song = 0

def play_music():
    pygame.mixer.music.load(playlist[current_song])
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_song():
    global current_song
    current_song = (current_song + 1) % len(playlist)
    play_music()

def prev_song():
    global current_song
    current_song = (current_song - 1) % len(playlist)
    play_music()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                play_music()
            elif event.key == pygame.K_s:  
                stop_music()
            elif event.key == pygame.K_n:  
                next_song()
            elif event.key == pygame.K_p:  
                prev_song()

    screen.fill((30, 30, 30))
    pygame.display.flip()

pygame.quit()