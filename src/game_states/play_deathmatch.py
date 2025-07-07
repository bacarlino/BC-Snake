
from src.factories import create_two_player_snakes
from src.game_states.play_state import PlayState
from src.game_states.match_over import MatchOver
import src.ui.ui_elements as ui


class PlayDeathMatch(PlayState):

    def __init__(self, game, level_config):
        super().__init__(game, level_config)
                
    def check_game_over(self):
        if self.match_over:
            for snake in self.snakes:
                snake.moving = False
                if not snake.dead:
                    snake.add_score(1)
                if snake.score >= 3:
                    self.game.push_game_over()
                    return
            self.game.push_game_state(MatchOver(self.game))

        self.reset_command_flags()

    def draw_score(self, window):
        score_surf, score_rect = ui.create_2player_score_banner(
            self.snakes[0].score, self.snakes[1].score
        )
        window.blit(score_surf, score_rect)

    def setup_snakes(self):
        self.snakes = create_two_player_snakes(self.game.window_size, self.level_config)
   
    def handle_fruit_collision(self, snake):
        if snake.head_position in self.fruits:
            snake.eat(self.level_config.growth_rate)
            self.fruits.remove(snake.head_position)
            self.add_fruit()