import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats 
from button import Button
from scoreboard import Scoreboard

def run_game():
    #Game, settings initialization and creating a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("AlienInvasion")

    #Creating button GAME
    play_button = Button(ai_settings, screen, "Game")

    #Creating a copy intended for storage statistical data about game
    #and creating a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

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

        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
         aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
             bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens,
             bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
            play_button)

run_game()
