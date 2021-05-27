import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard(object):
	"""Class created for displaying Scoreboard"""
	def __init__(self, ai_settings, screen, stats):
		"""Initialization attributes about scoreboard"""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		self.score = 0

		#setting font to inform player about score
		self.text_color = (30, 30, 30)
		self.font = pygame.font.SysFont(None, 48)

		#preparting starting picture with scores
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()

	def prep_score(self):
		#Changing score to generate image
		rounded_score = int(round(self.stats.score, -1))
		score_str = "{:,}".format(rounded_score)
		self.score_image = self.font.render(score_str, True, self.text_color
			, self.ai_settings.bg_color)

		#Displaying image to the right top edge of the screen
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right -20
		self.score_rect.top = 20

	def show_score(self):
		#Dispaying the score to the screen
		self.screen.blit(self.score_image, self.score_rect)
		self.screen.blit(self.high_score_image, self.high_score_rect)
		self.screen.blit(self.level_image, self.level_rect)
		#displaying the ships
		self.ships.draw(self.screen)

	def prep_high_score(self):
		"""Conversation the best score into game generated image"""
		high_score = int(round(self.stats.high_score, -1))
		high_score_str = "{:,}".format(high_score)
		self.high_score_image = self.font.render(high_score_str, True,
			self.text_color, self.ai_settings.bg_color)

		#Displaying the best score
		self.high_score_rect = self.high_score_image.get_rect()
		self.high_score_rect.right = self.screen_rect.centerx
		self.high_score_rect.top = self.score_rect.top

	def prep_level(self):
		#Converting level into image
		self.level_image = self.font.render(str(self.stats.level),
		 True, self.text_color, self.ai_settings.bg_color)

		#Displaying image to the right top edge of the screen
		self.level_rect = self.level_image.get_rect()
		self.level_rect.right = self.score_rect.right
		self.level_rect.top = self.score_rect.bottom + 10

	def prep_ships(self):
		"""preparing a number of avaible ships"""
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = Ship(self.ai_settings, self.screen)
			ship.rect.x = 10 + ship_number * ship.rect.width
			ship.rect.y = 10
			self.ships.add(ship)


