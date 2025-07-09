from src.ui.ui_elements import NameBanner, TitleBanner, PressSpaceEscBanner


class TitleMenuUI:

    def __init__(self, menu):
        self.name_banner = NameBanner()
        self.title_banner = TitleBanner()
        self.cmd_banner = PressSpaceEscBanner()
        self.menu = menu

    def layout(self):
        pass

    def draw(self, window):
        self.name_banner.draw(window)
        self.title_banner.draw(window)
        self.menu.draw(window)
        self.cmd_banner.draw(window)

    def update_menu(self, menu):
        self.menu = menu


    