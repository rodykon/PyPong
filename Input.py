import pygame

LEFT = 1
SCROLL = 2
RIGHT = 3

# FLAGS
QUIT = False
MOUSE_LEFT = False

def get_mouse_pos():
	return pygame.mouse.get_pos()

def update_input():
	global QUIT
	global MOUSE_LEFT
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			QUIT = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == LEFT:
				MOUSE_LEFT = True
		elif event.type == pygame.MOUSEBUTTONUP:
			if event.button == LEFT:
				MOUSE_LEFT = False
			