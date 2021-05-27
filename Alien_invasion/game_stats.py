class GameStats():
	"""Statistical data monitoring in game "AlienInvasion"."""
	
	def __init__(self, ai_settings):
		"""Initialization statistical data."""
		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = False

	def reset_stats(self):
		"""Initialization of statistical data to game"""
		self.ships_left = self.ai_settings.ship_limit
		