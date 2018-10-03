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

	HB_WIDTH = 20
	HB_HEIGHT = 90
	
	def __init__(self, screen, position, is_client):
		super(Paddle, self).__init__(screen, Images.paddle, position, (Paddle.HB_WIDTH, Paddle.HB_HEIGHT))
		self.__velocity = (0, 0)
		self.__is_client = is_client
	
	def tick(self):
		self.__last_x = self.x
		self.__last_y = self.y
		
		if self.__is_client:
			mx, my = Input.get_mouse_pos()
			self.x = mx - 0.5*Paddle.HB_WIDTH
			self.y = my - Paddle.HB_HEIGHT
			# This is where data will be sent to the server
		else:
			pass # This is where data from server will be received
		
		# Update velocity - velocity is in px / ticks
		self.__velocity = (self.x - self.__last_x, self.y - self.__last_y)
		
	def on_impact(self, entity): # What to do when impact occurs
		if isinstance(entity, Table):
			if self.x <= 800 and self.x >= 180:
				self.y = 350-90
		elif isinstance(entity, Net):
			mx, my = Input.get_mouse_pos()
			if mx >= 501:
				self.x = 503
			else:
				self.x = 499 - 20
	
	def get_velocity(self):
		return self.__velocity
	
	def is_client(self):
		return self.__is_client

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

	GY = 0.5 # px / ticks^2
	
	def __init__(self, screen, position):
		super(Ball, self).__init__(screen, Images.ball, position, (25, 25))
		self.__last_x, self.__last_y = (self.x, self.y)
		self.__velocity = [0, 0]
		self.__movable = False
	
	def tick(self):
		if self.__movable:
			self.__last_x = self.x
			self.__last_y = self.y
			
			self.__velocity[1] = self.__velocity[1] + Ball.GY
			
	def render(self):
		# Update position
		self.x, self.y = Math.get_new_pos(self.get_position(), self.__velocity)
		self.screen.blit(self.image, (self.x, self.y))
			
		
	def on_impact(self, entity): # What to do when impact occures
		if isinstance(entity, Paddle):
			if not self.__movable:
				self.__movable = True
			self.__velocity = Math.get_collision_vel(self.__velocity, entity.get_velocity(), 0.4)
			# Fix for 'stuck on paddle' bug
			if entity.get_velocity()[0] > 0:
				self.x = entity.get_position()[0] + entity.get_hitbox()[0] + 2
			elif entity.get_velocity()[0] < 0:
				self.x = entity.get_position()[0] - self.get_hitbox()[0] - 2
			else:
				if (self.x > entity.get_position()[0] + 0.5*entity.get_hitbox()[0]):
					self.x = entity.get_position()[0] + entity.get_hitbox()[0] + 2
				elif (self.x < entity.get_position()[0] + 0.5*entity.get_hitbox()[0]):
					self.x = entity.get_position()[0] - self.get_hitbox()[0] - 2
		elif isinstance(entity, Table):
			self.y = self.__last_y # Fix for 'ball stuck in table' bug
			self.__velocity[1] = -self.__velocity[1]
		
	def get_velocity(self):
		return self.__velocity
	
def check_impacts(entities):
	for entity1 in entities:
		for entity2 in entities:
			if entity1 != entity2:
				if Math.boxes_converging(entity1.get_position(), entity1.get_hitbox(), entity2.get_position(), entity2.get_hitbox()):
					entity1.on_impact(entity2)
					entity2.on_impact(entity1)