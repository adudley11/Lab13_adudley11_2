import pygame
from typing import TYPE_CHECKING
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_fleet import AlienFleet
    
class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        """Initialize the alien and set its starting position."""
        
        super().__init__()
        
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.scale(self.image, 
            (self.settings.alien_w, self.settings.alien_h)
            )
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def update(self):
        temp_speed = self.settings.alien_speed
            
        self.x += temp_speed * self.fleet.fleet_direction
        self.rect.x = self.x
        self.rect.y = self.y
        
    def check_edges(self):
        return (self.rect.right >= self.boundries.right or  self.rect.left <= self.boundries.left)
    
    def draw_alien(self):
        self.screen.blit(self.image, self.rect)