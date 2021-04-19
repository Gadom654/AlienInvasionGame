import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group

def run_game():
    #Game, settings initialization and creating a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("AlienInvasion")

    # Set the background color.
    bg_color = (230, 230, 230)

    #Creating spaceship
    ship = Ship(ai_settings, screen)

    #Creating group manage to storege bullets
    bullets = Group()

    #Starting main game loop
    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)

run_game()