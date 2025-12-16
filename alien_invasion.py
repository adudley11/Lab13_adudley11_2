import sys
import pygame

from arsenal import Arsenal
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
from alien_fleet import AlienFleet
from time import sleep
from button import Button


class AlienInvasion:
    """Overall class to manage game and behavior"""
    
    def __init__(self):
        """iInitialize the game, and create the game resources"""
        
        pygame.init()
        
        self.running = True
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.game_stats = GameStats(self.settings.starting_ship_count)
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self, Arsenal(self))
        self.alien_fleet = AlienFleet(self)
        self.alien_fleet.create_fleet()
        
        self.play_button = Button(self, 'Play')
        self.game_active = False
        
    def run_game(self):
        """Start the main loop for the game"""
        while self.running:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self.alien_fleet.update_fleet()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(60)
          
    def _check_collisions(self):
        if self.ship.check_collisions(self.alien_fleet.fleet):
            self._check_game_status()
        
        if self.alien_fleet.check_fleet_bottom():
            self._check_game_status()
            
        collisions = self.alien_fleet.check_collisions(self.ship.arsenal.arsenal)
        
        if self.alien_fleet.check_destroyed_status():
            self._reset_level()
        
    def _check_game_status(self):
        if self.game_stats.ships_left > 0:
            self.game_stats.ships_left -=1
            self._reset_level()
            sleep(0.5)
            
        else:
            self.game_active = False
            
    
    def _reset_level(self):
        self.ship.arsenal.arsenal.empty()
        self.alien_fleet.fleet.empty()
        self.alien_fleet.create_fleet()
        
    def restart_game(self):
        
        self._reset_level()
        self.ship._center_ship()
        self.game_active = True
        pygame.mouse.set_visible(False)
        
    def _check_events(self):
        """Respond to kepresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and self.game_active == True:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_button_clicked()

    def _check_button_clicked(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.play_button.check_clicked(mouse_pos):
            self.restart_game()
                
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.ship.fire()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images on the screeen, and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)
        self.ship.draw()
        self.alien_fleet.draw()
        
        if not self.game_active:
            self.play_button.draw()
            pygame.mouse.set_visible(True)
            
        pygame.display.flip()
            
            
if __name__ == '__main__':
    # Make a game instance, and run the game
    ai = AlienInvasion()
    ai.run_game()
    
