from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize statistics."""
        self.settings = game.settings
        self.max_score = 0
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1
        
    def update(self, collisions):
        self._update_score(collisions)
        self._update_max_score()
        
        

    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score
        print(f'Max Score: {self.max_score}')

    def _update_score(self, collisions):
        for alien in collisions.values():
            self.score = self.settings.alien_points
        print(f'Current: {self.score}')
            
    def update_level(self):
        self.level += 1
        
    