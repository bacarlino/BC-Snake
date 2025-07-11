from src.ui.ui_config import SCORE_BANNER_CENTER

class PlayStateUI:

    def __init__(self, score_banner):
        self.score_banner = score_banner
    
    def layout(self):
        self.score_banner.rect.center = SCORE_BANNER_CENTER

    def update(self, scores):
        self.score_banner.update(scores)

    def draw(self, window):
        self.score_banner.draw(window)

