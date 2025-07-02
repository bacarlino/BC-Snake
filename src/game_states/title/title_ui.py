from src.ui.ui_elements import NameBanner, TitleBanner, PressSpaceBanner


class TitleUI:
    
    def __init__(self):
        self.name_banner = NameBanner()
        self.title_banner = TitleBanner()
        self.press_space_banner = PressSpaceBanner()

    def draw(self, window):
        self.name_banner.draw(window)
        self.title_banner.draw(window)
        self.press_space_banner.draw(window)