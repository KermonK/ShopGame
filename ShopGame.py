import pygame
from pygame.locals import *

# Algseadistused
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Harjutamine")

# Piltide laadimine
bg_shop = pygame.image.load("bg_shop.jpg")
seller = pygame.image.load("seller.png")
chat = pygame.image.load("chat.png")  # Jutumulli pilt

# Piltide suuruse muutmine
seller_scaled = pygame.transform.scale(seller, (256, 305))  # Poemüüja väiksemaks
chat_scaled = pygame.transform.scale(chat, (255, 210))  # Jutumulli suuruse kohandamine

# Font ja teksti määramine
font = pygame.font.SysFont("Arial", 20, bold=False)
text = font.render("Tere, olen Kermon", True, (255, 255, 255))

# Mängutsükkel
running = True
while running:
    screen.blit(bg_shop, (0, 0))  # Tausta lisamine
    screen.blit(seller_scaled, (105, 159))  # Väiksem poemüüja
    screen.blit(chat_scaled, (246, 60))  # Väiksem jutumull
    screen.blit(text, (290, 135))  # Teksti asukoha korrigeerimine

    # Sündmuste kontroll
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.display.flip()

pygame.quit()