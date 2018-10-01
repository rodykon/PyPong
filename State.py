import pygame
import Colors
import Images
from Entities import *

ACTIVE = "game"

class GameState(object):

	def init(self, screen):
		self.screen = screen
		self.__paddle1 = Paddle(self.screen, (50,50))
		self.__table = Table(self.screen, (200, 350))
		self.__net = Net(self.screen, (499, 300))
		self.__entities = [self.__paddle1, self.__table, self.__net]
		
	def tick(self):
		self.__table.tick()
		self.__net.tick()
		self.__paddle1.tick()
		check_impacts(self.__entities)
		
	def render(self):
		self.screen.fill(Colors.WHITE)
		self.__table.render()
		self.__net.render()
		self.screen.blit(Images.ball, (200, 100))
		self.__paddle1.render()
		

class MenuState(object):

	def init(self, screen):
		self.screen = screen
		
	def tick(self):
		pass
		
	def render(self):
		pass
		
		

game_state = GameState()
menu_state = MenuState()

def active_state():
	if ACTIVE == "menu":
		return menu_state
	else:
		return game_state