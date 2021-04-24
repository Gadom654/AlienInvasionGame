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

    #Creating spaceship, group of bullets and group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #Creating aliens fleet
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Starting main game loop
    while True:

        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()