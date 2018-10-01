import Math
import Input
import Images
import pygame
# This class defines a game entity.
class Entity(object):
	
	def __init__(self, screen, image, position, hitbox):
		self.screen = screen
		self.image = image
		self.x = position[0]
		self.y = position[1]
		self.hitbox = hitbox
		
	def tick(self):
		pass
	
	def render(self):
		self.screen.blit(self.image, (self.x, self.y))
	
	def on_impact(self, entity): # What to do when impact occures
		pass
	
	def get_position(self):
		return self.x, self.y
		
	def get_hitbox(self):
		return self.hitbox
		

class Paddle(Entity):
	
	def __init__(self, screen, position):
		super(Paddle, self).__init__(screen, Images.paddle, position, (20, 90))
	
	def tick(self):
		self.__last_x = self.x
		self.__last_y = self.y
		mx, my = Input.get_mouse_pos()
		self.x = mx - 0.5*20
		self.y = my - 90
		
	def on_impact(self, entity): # What to do when impact occures
		if isinstance(entity, Table):
			if self.x <= 800 and self.x >= 180:
				self.y = 350-90
		elif isinstance(entity, Net):
			mx, my = Input.get_mouse_pos()
			if mx >= 501:
				self.x = 503
			else:
				self.x = 499 - 20

class Table(Entity):
	def __init__(self, screen, position):
		super(Table, self).__init__(screen, Images.table, position, (600, 50))
		
	def on_impact(self, entity): # What to do when impact occures
		pass
	
class Net(Entity):
	def __init__(self, screen, position):
		super(Net, self).__init__(screen, Images.net, position, (4, 50))
		
	def on_impact(self, entity): # What to do when impact occures
		pass

class Ball(Entity):
	pass
	
def check_impacts(entities):
	for entity1 in entities:
		for entity2 in entities:
			if entity1 != entity2:
				if Math.boxes_converging(entity1.get_position(), entity1.get_hitbox(), entity2.get_position(), entity2.get_hitbox()):
					entity1.on_impact(entity2)
					entity2.on_impact(entity1)