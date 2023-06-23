import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Emoji Slot Machine")

# Define emojis
emojis = [":)", ":D", ":(", ":O", ":P", ":3", ";)", "!"]

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define fonts
font = pygame.font.SysFont(None, 50)

# Define slot machine parameters
slot_width = 150
slot_height = 150
slot_margin = 20

# Create slots
slots = []
for i in range(3):
    x = (screen_width - (slot_width * 3 + slot_margin * 2)) / 2 + (slot_width + slot_margin) * i
    y = (screen_height - slot_height) / 2
    slots.append(pygame.Rect(x, y, slot_width, slot_height))

# Spin the slots
def spin_slots():
    return [random.choice(emojis) for _ in range(3)]

# Game loop
running = True
spinning = False
spin_count = 0
result = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not spinning:
                spin_count = 0
                spinning = True

    if spinning:
        if spin_count < 8:
            result = spin_slots()
            spin_count += 1
        else:
            spinning = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw the slots
    for slot in slots:
        pygame.draw.rect(screen, BLACK, slot)

    # Draw the emojis
    if spinning:
        for i in range(len(slots)):
            emoji_text = font.render(random.choice(emojis), True, WHITE)
            emoji_rect = emoji_text.get_rect(center=slots[i].center)
            screen.blit(emoji_text, emoji_rect)
    elif result:
        for i in range(len(result)):
            emoji_text = font.render(result[i], True, WHITE)
            emoji_rect = emoji_text.get_rect(center=slots[i].center)
            screen.blit(emoji_text, emoji_rect)

    # Update the display
    pygame.display.update()

    # Delay to control spinning speed
    pygame.time.delay(100)

# Quit the game
pygame.quit()