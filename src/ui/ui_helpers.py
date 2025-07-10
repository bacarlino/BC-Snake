from src.ui import ui_config


def layout_title_banners(name, title, cmd_bar):
    name.rect.center = ui_config.NAME_BANNER_CENTER
    title.rect.center = ui_config.TITLE_BANNER_CENTER
    cmd_bar.rect.midbottom = ui_config.COMMAND_BAR_MIDBOTTOM
