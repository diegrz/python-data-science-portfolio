from scoreboard import Scoreboard

class GameStats:
	""" Track stastistics for Alien Invasion"""

	def __init__(self,ai_game):
		"""Initialize statistics"""
		self.settings = ai_game.settings
		self.reset_stats()

		# Start Alien Invasion in an inactive state
		self.game_active = False

		# High score should never be reset
		filename = 'all_time_highscore.txt'
		with open(filename) as file_object:
			self.high_score = int(file_object.read())

		self.level = 1

	def reset_stats(self):
		"""Initialize statistics that can change during the game """
		self.ships_left = self.settings.ship_limit
		self.score = 0
