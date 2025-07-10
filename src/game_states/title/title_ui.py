from src.ui.ui_elements import NameBanner, TitleBanner, PressSpaceBanner
from src.ui.ui_helpers import layout_title_banners


class TitleUI:

    def __init__(self):
        self.name_banner = NameBanner()
        self.title_banner = TitleBanner()
        self.press_space_banner = PressSpaceBanner()

    def layout(self):
        layout_title_banners(
            self.name_banner, self.title_banner, self.press_space_banner
        )

    def draw(self, window):
        self.name_banner.draw(window)
        self.title_banner.draw(window)
        self.press_space_banner.draw(window)