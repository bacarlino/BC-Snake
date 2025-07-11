import pygame

from src.game_world.game_world import GameWorld
from src.game_world.score_strategy import fruit_scoring
from src.ui.border import Border
from src.enums import Play, SnakeID
from src.factories import create_one_player_snakes
from src.game_states.game_state import GameState
from src.ui.ui_elements import ScoreBanner
from src.game_states.play_state.play_state_ui import PlayStateUI


class PlayState(GameState):
    """Single player and base state for 2 player modes"""

    def __init__(self, game, level_config):
        super().__init__(game)
        
        self.level_config = level_config
        self.match_over = False
        self.scores = {SnakeID.ONE: 0, SnakeID.TWO: 0}

        self.game_world = GameWorld(
            self.game.window_size,
            self.game.display_size,
            self.get_snakes(), 
            self.get_border(), 
            self.level_config,
            self.scores,
        )
        self.game_world.set_fruit_score_strategy(fruit_scoring)

        self.ui = PlayStateUI(ScoreBanner(self.scores[SnakeID.ONE]))
        self.ui.layout()
        

        self.commands = {
            Play.START: False, 
            Play.PAUSE: False,
            Play.QUIT: False
        }

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.commands[Play.PAUSE] = True
            if event.key == pygame.K_ESCAPE:
                self.commands[Play.QUIT] = True

            self.game_world.handle_event(event)
       
    def update(self):
        if self.update_commands(): return
        self.match_over = self.game_world.update()
        self.check_game_over()
        self.ui.update(self.get_scores())
        self.reset_command_flags()

    def match_over_update(self):
        self.game_world.update_snakes_no_collision()

    def draw(self, window):
        self.game_world.draw(window)
        self.ui.draw(window)

    def update_commands(self):
        if self.commands[Play.PAUSE]:
            self.game.push_pause()
        if self.commands[Play.QUIT]:
            self.game.reset_game()
            return True
        return False

    def get_scores(self):
        return self.scores[SnakeID.ONE]

    def check_game_over(self):
        if self.game_world.all_snakes_dead():
            self.game.push_game_over()


    def get_snakes(self):
        return create_one_player_snakes(self.game.window_size, self.level_config)

    def reset_snakes(self):
        self.game_world.reset_snakes()

    def get_border(self):
        if self.level_config.has_border:
            return Border(self.game.window_size, self.level_config.cell_size, self.level_config.border_color)
        else:
            return None