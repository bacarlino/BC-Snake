from src.enums import SnakeID
from src.factories import create_two_player_snakes
from src.game_states.play_state.play_state import PlayState
from src.game_states.play_state.play_state_ui import PlayStateUI
from src.game_states.match_over import MatchOver
from src.game_world.score_strategy import no_fruit_scoring
from src.ui.ui_elements import TwoPlayerScoreBanner


class PlayDeathMatch(PlayState):

    def __init__(self, game, level_config):
        super().__init__(game, level_config)
        self.ui = PlayStateUI(TwoPlayerScoreBanner(self.get_scores()))
        self.game_world.set_fruit_score_strategy(no_fruit_scoring)
                
    def check_game_over(self):
        if self.game_world.any_snake_dead():
            for snake in self.game_world.snakes:
                snake.moving = False
                if not snake.dead:
                    self.scores[snake.id] += 1
                if self.scores[snake.id] >= 3:
                    self.game.push_game_over()
                    return
            self.game.push_game_state(MatchOver(self.game))

        self.reset_command_flags()

    def get_scores(self):
        return (self.scores[SnakeID.ONE], self.scores[SnakeID.TWO])

    def get_snakes(self):
        return create_two_player_snakes(self.game.window_size, self.level_config)
