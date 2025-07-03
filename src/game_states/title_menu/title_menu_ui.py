from src.ui.ui_elements import NameBanner, TitleBanner, PressSpaceEscBanner


class TitleMenuUI:

    def __init__(self):
        self.name_banner = NameBanner()
        self.title_banner = TitleBanner()
        self.press_space_banner = PressSpaceEscBanner()

    def draw_title(self, window):
        self.name_banner.draw(window)
        self.title_banner.draw(window)

    