import pygame
import os

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Music Player")

background_path = "/Users/macbook/Documents/PP2/LAB_7/image/telepatiaalbom.jpeg"

if os.path.exists(background_path):
    background = pygame.image.load(background_path)
    background = pygame.transform.scale(background, (500, 500))
else:
    print(f"Фон не найден!")
    background = None

music_folder = "/Users/macbook/Documents/PP2/LAB_7/music"

if not os.path.exists(music_folder):
    print(f"Папка не найдена!")
    pygame.quit()
    exit()

tracks = [f for f in os.listdir(music_folder) if f.endswith('.mp3')]
if not tracks:
    print("Нет музыкальных файлов!")
    pygame.quit()
    exit()

current_track = 0
playing = True
pygame.mixer.init()
pygame.mixer.music.load(os.path.join(music_folder, tracks[current_track]))

print(f"Загружаем: {tracks[current_track]}")
if not pygame.mixer.get_init():
    print("ERROR")

pygame.mixer.music.play()
pygame.display.set_caption(f"Playing: {tracks[current_track]}")

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:  # Play 
                pygame.mixer.music.unpause()
                playing = True

            if event.key == pygame.K_s:  # Pause
                pygame.mixer.music.pause()
                playing = False

            if event.key == pygame.K_d:  # Next track
                pygame.mixer.music.stop()
                current_track = (current_track + 1) % len(tracks)
                pygame.mixer.music.load(os.path.join(music_folder, tracks[current_track]))
                pygame.mixer.music.play()
                pygame.display.set_caption(f"Playing: {tracks[current_track]}")
                playing = True

            if event.key == pygame.K_a:  # Previous track
                pygame.mixer.music.stop()
                current_track = (current_track - 1) % len(tracks)
                pygame.mixer.music.load(os.path.join(music_folder, tracks[current_track]))
                pygame.mixer.music.play()
                pygame.display.set_caption(f"Playing: {tracks[current_track]}")
                playing = True

    if background:
        screen.blit(background, (0, 0))

    pygame.display.flip()

pygame.quit()
