import pygame

class Ship(object):
	"""Spaceship that will be made for player usage"""
	
	def __init__(self, ai_settings, screen):
		"""Spaceship initialization and his starting position"""

		self.screen = screen
		self.ai_settings = ai_settings


		#Loading the spaceship image and downloading his rectangle
		self.image = pygame.image.load("images/ship.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#Each new spaceship respawn on the bottom of the screen
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#center point of spaceship
		self.centerox = float(self.rect.centerx)
		self.centeroy = float(self.rect.centery)

		#Options that show spaceship is moving
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False

	def update(self):
		"""Updating spaceship localization by his moves"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.centerox += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.centerox -= self.ai_settings.ship_speed_factor
		if self.moving_up and self.rect.top > self.screen_rect.bottom/2:
			self.centeroy -= self.ai_settings.ship_speed_factor
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.centeroy += self.ai_settings.ship_speed_factor

		#upadting rect by the value of self.center
		
		if self.moving_up or self.moving_down:
			self.rect.centery = self.centeroy 
		if self.moving_left or self.moving_right:
			self.rect.centerx = self.centerox

	def blitme(self):
		"""Displaying the spaceship in his actual position"""
		self.screen.blit(self.image, self.rect)

	def center_ship(self):
		"""Place spaceship to the center bottom edge."""
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		self.centerox = float(self.rect.centerx)
		self.centeroy = float(self.rect.centery)
