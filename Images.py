# This is where all images used in the game will be stored as static variables
import pygame
import Colors

paddle = pygame.image.load(r"res\paddle.png")
paddle.set_colorkey(Colors.PINK)

table = pygame.image.load(r"res\table.png")
table.set_colorkey(Colors.PINK)

net = pygame.image.load(r"res\net.png")

ball = pygame.image.load(r"res\ball.png")
ball.set_colorkey(Colors.PINK)