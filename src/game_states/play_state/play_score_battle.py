from src.enums import SnakeID
from src.factories import create_two_player_snakes
from src.game_states.play_state.play_state import PlayState
from src.ui.ui_elements import TwoPlayerScoreBanner
from src.game_states.play_state.play_state_ui import PlayStateUI


class PlayScoreBattle(PlayState):

    def __init__(self, game, level_config):
        super().__init__(game, level_config)
        self.ui = PlayStateUI(TwoPlayerScoreBanner(self.get_scores()))

    def check_game_over(self):
        if self.game_world.any_snake_dead():
            for snake in self.game_world.snakes:
                snake.moving = False
            self.game.push_game_over()

    def get_scores(self):
        return (self.scores[SnakeID.ONE], self.scores[SnakeID.TWO])

    def get_snakes(self):
        return create_two_player_snakes(self.game.window_size, self.level_config)