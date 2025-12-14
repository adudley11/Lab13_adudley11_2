class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the games settings"""
        
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        #Ship settings
        self.ship_speed = 5
        self.ship_limit = 3
        self.ship_w = 60
        self.ship_h = 60
        self.starting_ship_count = 2
        
        # Bullet settings
        self.bullet_speed = 10
        self.bullet_width = 3
        self.bullet_height = 30
        self.bullet_color = (143, 26, 7)
        self.bullets_allowed = 5
        
        # Alien settings
        self.alien_speed = 2
        self.fleet_drop_speed = 15
        self.alien_w = 70
        self.alien_h = 70
        
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        