import pygame
from pygame.sprite import Sprite 

class Alien(Sprite):
	"""Class showing single alien"""

	def __init__(self, ai_settings, screen):
		"""Initialization alien and defining his starting position."""
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		#Loading alien photo and defining his rect attrib
		alien_image = pygame.image.load('images/alien.PNG').convert_alpha()
		alien_image = pygame.transform.scale(alien_image, (50, 50)) 
		self.image = alien_image
		self.rect = self.image.get_rect()

		#Defining starting position of alien to left upper corner"""
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#Storage actual alien position
		self.x = float(self.rect.x)

	def blitme(self):
		"""Display the alien to the screen"""
		self.screen.blit(self.image, self.rect)

	def check_edges(self):
		"""Returning value True, if alien is near to right edge"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True

	def update(self):
		"""Moving alien to the right or to theleft."""
		self.x += (self.ai_settings.alien_speed_factor *
		 			self.ai_settings.fleet_direction)
		self.rect.x = self.x
