from src.ui.ui_elements import NameBanner, TitleBanner, PressSpaceEscBanner


class TitleMenuUI:

    def __init__(self, menu=None):
        self.name_banner = NameBanner()
        self.title_banner = TitleBanner()
        self.cmd_banner = PressSpaceEscBanner()
        self.menu = menu

    def draw_title(self, window):
        self.name_banner.draw(window)
        self.title_banner.draw(window)

    def draw_command_bar(self, window):
        self.cmd_banner.draw(window)

    