from src.enums import SnakeID
from src.factories import create_two_player_snakes
from src.game_states.play_state import PlayState
from src.ui.ui_elements import ScoreBanner



class PlayCoOp(PlayState):

    def __init__(self, game, level_config):
        super().__init__(game, level_config)
        self.score_banner = ScoreBanner(self.get_score())

    def check_game_over(self):
        if self.game_world.all_snakes_dead():
        # if all([snake.dead for snake in self.snakes]):
            self.game.push_game_over()

    def update_score_banner(self):
        self.score_banner.update(self.get_score())
        
    def get_score(self):
        return (self.scores[SnakeID.ONE] + self.scores[SnakeID.TWO])

    def get_snakes(self):
        return create_two_player_snakes(self.game.window_size, self.level_config)
