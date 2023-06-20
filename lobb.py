# Import the required libraries
import gc
import signal
from tkinter import Button
import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set up the display
display_info = pygame.display.Info()
display_width = display_info.current_w
display_height = display_info.current_h
game_display = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
pygame.display.set_caption("GoGambleGo")

# Set up the background
background_image = pygame.image.load("Images/Floor.png")
background_image = pygame.transform.scale(background_image, (display_width, display_height))
background_surface = pygame.Surface((display_width, display_height))
background_surface.blit(background_image, (0, 0))

# Set up the player
player_width = 50
player_height = 50
player_x = 0
player_y = 400
player_speed = 5
player_sprite = pygame.Rect(player_x, player_y, player_width, player_height)

# Set up the player animations
player_animations_forward = [
    pygame.image.load("Images/Player/animation_state1.png"),
    pygame.image.load("Images/Player/animation_state2.png")
]
player_animations_backward = [
    pygame.image.load("Images/Player/animation_state3.png"),
    pygame.image.load("Images/Player/animation_state4.png")
]
player_animations_left = [
    pygame.image.load("Images/Player/animation_state5.png"),
    pygame.image.load("Images/Player/animation_state6.png")
]
player_animations_right = [
    pygame.image.load("Images/Player/animation_state7.png"),
    pygame.image.load("Images/Player/animation_state8.png")
]
current_animation_index = 0
current_animation = player_animations_forward[current_animation_index]

# Set up the obstacle
obstacle_width = 300
obstacle_height = 400
obstacle_x = -200
obstacle_y = -200
obstacle_image = pygame.image.load("Images/Slots/slot2.png")
obstacle_sprite = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)

# Set up the camera
camera_x = 0
camera_y = 0

# Set up animation change speed
animation_change_speed = 8
frame_counter = 0

# Set up scenes
SCENE_MAIN = "main"
SCENE_NEW = "new"
SCENE_PAUSE = "pause"  # New scene constant for the pause menu
current_scene = SCENE_PAUSE

# Define function to open new scene
def open_new_scene():
    global current_scene
    current_scene = SCENE_NEW

def runttt():
    execfile("./filename") 

# Define function to handle "E" key press on the obstacle
def handle_obstacle_interaction():
    if current_scene == SCENE_MAIN and player_sprite.colliderect(obstacle_sprite):
        open_new_scene()

# Define function to handle the pause functionality
def handle_pause():
    global current_scene
    if current_scene == SCENE_MAIN:
        current_scene = SCENE_PAUSE
    elif current_scene == SCENE_PAUSE:
        current_scene = SCENE_MAIN

# Game loop
game_running = True
clock = pygame.time.Clock()

# Set up button colors
BUTTON_COLOR = (41, 128, 185)
BUTTON_TEXT_COLOR = (255, 255, 255)

while game_running:
    clock.tick(60)

    frame_counter += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            handle_obstacle_interaction()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                handle_pause()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_sprite.y -= player_speed
    if keys[pygame.K_a]:
        player_sprite.x -= player_speed
    if keys[pygame.K_s]:
        player_sprite.y += player_speed
    if keys[pygame.K_d]:
        player_sprite.x += player_speed
    if keys[pygame.K_t]:
        execfile('tictactoce.py')
        

    if player_sprite.colliderect(obstacle_sprite):
        if keys[pygame.K_w]:
            player_sprite.y += player_speed
        if keys[pygame.K_a]:
            player_sprite.x += player_speed
        if keys[pygame.K_s]:
            player_sprite.y -= player_speed
        if keys[pygame.K_d]:
            player_sprite.x -= player_speed

    if frame_counter % animation_change_speed == 0:
        if keys[pygame.K_w]:
            current_animation_index = (current_animation_index + 1) % len(player_animations_forward)
            current_animation = player_animations_forward[current_animation_index]
        if keys[pygame.K_a]:
            current_animation_index = (current_animation_index + 1) % len(player_animations_left)
            current_animation = player_animations_left[current_animation_index]
        if keys[pygame.K_s]:
            current_animation_index = (current_animation_index + 1) % len(player_animations_backward)
            current_animation = player_animations_backward[current_animation_index]
        if keys[pygame.K_d]:
            current_animation_index = (current_animation_index + 1) % len(player_animations_right)
            current_animation = player_animations_right[current_animation_index]

    if frame_counter >= 1000:
        frame_counter = 0

    camera_x = -player_sprite.x + display_width / 2
    camera_y = -player_sprite.y + display_height / 2

    game_display.blit(background_surface, (0, 0))
    game_display.blit(obstacle_image, obstacle_sprite.move(camera_x, camera_y))
    game_display.blit(current_animation, player_sprite.move(camera_x, camera_y))

    if current_scene == SCENE_PAUSE:  # Display pause menu
        pause_surface = pygame.Surface((display_width, display_height))
        pause_surface.set_alpha(128)
        pause_surface.fill((0, 0, 0))
        game_display.blit(pause_surface, (0, 0))

        pause_text = pygame.font.SysFont(None, 50).render("GoGambleGo", True, (255, 255, 255))
        play_text = pygame.font.SysFont(None, 30).render("Play", True, BUTTON_TEXT_COLOR)
        settings_text = pygame.font.SysFont(None, 30).render("Settings", True, BUTTON_TEXT_COLOR)
        quit_text = pygame.font.SysFont(None, 30).render("Quit", True, BUTTON_TEXT_COLOR)

        play_button = pygame.Rect(display_width / 2 - 50, display_height / 2 - 30, 100, 40)
        settings_button = pygame.Rect(display_width / 2 - 75, display_height / 2 + 10, 150, 40)
        quit_button = pygame.Rect(display_width / 2 - 50, display_height / 2 + 50, 100, 40)

        pygame.draw.rect(game_display, BUTTON_COLOR, play_button)
        pygame.draw.rect(game_display, BUTTON_COLOR, settings_button)
        pygame.draw.rect(game_display, BUTTON_COLOR, quit_button)

        game_display.blit(pause_text, (display_width / 2 - pause_text.get_width() / 2, display_height / 2 - 120))
        game_display.blit(play_text, (display_width / 2 - play_text.get_width() / 2, display_height / 2 - 20))
        game_display.blit(settings_text, (display_width / 2 - settings_text.get_width() / 2, display_height / 2 + 20))
        game_display.blit(quit_text, (display_width / 2 - quit_text.get_width() / 2, display_height / 2 + 60))

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if play_button.collidepoint(mouse_pos):
                handle_pause()
            elif quit_button.collidepoint(mouse_pos):
                game_running = False

    pygame.display.update()

pygame.quit()