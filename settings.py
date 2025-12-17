from pathlib import Path
class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the games settings"""
        
        # Screen/Game settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.difficulty_scale = 1.5
        self.scores_file = Path.cwd() / 'files' / 'scores.json'
        
        # Ship settings
        self.ship_file = Path.cwd() / 'images' / 'ship.bmp'
        self.ship_limit = 3
        self.ship_w = 60
        self.ship_h = 60
        
        # Bullet settings
        self.bullet_width = 6
        self.bullet_height = 30
        self.bullet_color = (143, 26, 7)
        
        # Alien settings
        self.alien_w = 70
        self.alien_h = 70
        
        # Fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        
        # Button settings
        self.button_w = 200
        self.button_h = 50
        self.button_color = (86, 164, 152)
        
        # Font settings
        self.text_color = (5, 5, 5)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'fonts' / 'RacingSansOne-Regular.ttf'
        
    def initialize_dynamic_settings(self):
        # Ship
        self.ship_speed = 2
        self.starting_ship_count = 2
        
        # Alien
        self.alien_speed = 1
        self.fleet_drop_speed = 15
        self.alien_points = 50

        # Bullets
        self.bullet_speed = 3
        self.bullets_allowed = 5

    def increase_difficulty(self):
        self.ship_speed *= self.difficulty_scale
        self.bullet_speed *= self.difficulty_scale
        self.alien_speed *= self.difficulty_scale