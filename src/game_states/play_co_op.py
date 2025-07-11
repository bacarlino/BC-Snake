from src.factories import create_two_player_snakes
from src.game_states.play_state import PlayState
from src.ui.ui_elements import ScoreBanner



class PlayCoOp(PlayState):

    def __init__(self, game, level_config):
        super().__init__(game, level_config)
        score = (self.snakes[0].score + self.snakes[1].score)
        self.score_banner = ScoreBanner(score)

    def check_game_over(self):
        if all([snake.dead for snake in self.snakes]):
            self.game.push_game_over()

    def update_score_banner(self):
        self.score_banner.update(self.get_score())
        
    def get_score(self):
        return (self.snakes[0].score + self.snakes[1].score)

    def setup_snakes(self):
        self.snakes = create_two_player_snakes(self.game.window_size, self.level_config)
