from src.factories import create_two_player_snakes
from src.game_states.play_state import PlayState
import src.ui.ui_elements as ui


class PlayScoreBattle(PlayState):

    def __init__(self, game, level_config):
        super().__init__(game, level_config)

    def check_game_over(self):
        if self.match_over:
            for snake in self.snakes:
                snake.moving = False
            self.game.push_game_over()

    def draw_score(self, window):
        score_surf, score_rect = ui.create_2player_score_banner(
            self.snakes[0].score, self.snakes[1].score
        )
        window.blit(score_surf, score_rect)

    def setup_snakes(self):
        self.snakes = create_two_player_snakes(self.game.window_size, self.level_config)
  