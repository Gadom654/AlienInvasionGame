import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""Class make to manage bullets shooted by spaceship"""
	
	def __init__(self, ai_settings, screen, ship):
		"""Initialization bullet object in his current position"""
		super(Bullet, self).__init__()
		self.screen = screen
		#Making bullet in position 0,0 and then giving him correct 
		#localization
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
		 ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		#making a float to give bullet correct position
		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		"""moving bullet on screen"""
		#updating bullet position
		self.y -= self.speed_factor

		#updating postion of bullet rect
		self.rect.y = self.y

	def draw_bullet(self):
		"""Display bullet"""
		pygame.draw.rect(self.screen, self.color, self.rect)