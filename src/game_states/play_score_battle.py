from src.factories import create_two_player_snakes
from src.game_states.play_state import PlayState
from src.ui.ui_elements import TwoPlayerScoreBanner


class PlayScoreBattle(PlayState):

    def __init__(self, game, level_config):
        super().__init__(game, level_config)
        self.score_banner = TwoPlayerScoreBanner(self.get_score())

    def check_game_over(self):
        if self.match_over:
            for snake in self.snakes:
                snake.moving = False
            self.game.push_game_over()

    def get_score(self):
        return (self.snakes[0].score, self.snakes[1].score)

    def draw_score(self, window):
        self.score_banner.draw(window)

    def setup_snakes(self):
        self.snakes = create_two_player_snakes(self.game.window_size, self.level_config)

    def update_score_banner(self):
        self.score_banner.update(self.get_score())
