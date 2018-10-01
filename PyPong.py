import pygame
import sys

import State
import Input

WIDTH = 1000
HEIGHT = 400
TITLE = "PyPong"
REFRESH_RATE = 60


def main():
	pygame.init() # Initialize Pygame
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	pygame.display.set_caption(TITLE)
	clock = pygame.time.Clock()
	
	State.game_state.init(screen)
	State.menu_state.init(screen)
	while True:
		Input.update_input()
		if Input.QUIT:
			sys.exit()
		State.active_state().tick()
		State.active_state().render()
		pygame.display.flip()
		clock.tick(REFRESH_RATE)
			


if __name__ == "__main__":
	main()