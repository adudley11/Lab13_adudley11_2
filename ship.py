import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    """A class to manage the ship"""
    
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        """Initalize the ship and set its starting position"""
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
 
        # Load the ship image and get its rect
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, (self.settings.ship_w, self.settings.ship_h))

        self.rect = self.image.get_rect()
        
        self._center_ship()


        # Movement flag; start with a ship that's not moving
        self.moving_right = False
        self.moving_left = False
        
        self.arsenal = arsenal

    def _center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        self._update_ship_movement()
        self.arsenal.update_arsenal()
        
    def _update_ship_movement(self):
        """Update the ship's position based on the movement flags"""
        # Update the ship's x value, not the rect
        temp_speed = self.settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
            
        # Update rect object from self.x
        self.rect.x = self.x
        
    def draw(self):
        """Draw the ship at its current location"""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

        
    def fire(self):
        self.arsenal.fire_bullet()
        
    def check_collisions(self, other_group):
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False