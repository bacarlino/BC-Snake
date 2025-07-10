from src.ui.ui_elements import NameBanner, TitleBanner, PressSpaceEscBanner
from src.ui.ui_helpers import layout_title_banners


class TitleMenuUI:

    def __init__(self, menu):
        self.name_banner = NameBanner()
        self.title_banner = TitleBanner()
        self.cmd_banner = PressSpaceEscBanner()
        self.menu = menu

    def layout(self):
        layout_title_banners(
            self.name_banner, self.title_banner, self.cmd_banner
        )

    def draw(self, window):
        self.name_banner.draw(window)
        self.title_banner.draw(window)
        self.menu.draw(window)
        self.cmd_banner.draw(window)

    def update_menu(self, menu):
        self.menu = menu


    