from functools import partial

import src.app_config as cfg
from src.enums import MenuType
from src.level_config import pre_made
from src.level_config import level_attributes as lvl_attr
from src.ui.menu import Menu, MenuGrid, MenuItem
from src.game_states.run_co_op import RunCoOp
from src.game_states.run_deathmatch import RunDeathMatch
from src.game_states.run_score_battle import RunScoreBattle
import src.ui.ui_elements as ui


MENU_HEIGHT = ui.PRESS_SPACE_RECT.top - ui.TITLE_RECT.bottom 
MENU_POS = (ui.TITLE_RECT.midbottom)
MENU_SIZE = (cfg.WINDOW_W * 0.9, MENU_HEIGHT)

PADDING = 80
MENU_GRID_POS = (cfg.CENTER[0], PADDING)
MENU_GRID_SIZE = (cfg.WINDOW_W - PADDING * 2, cfg.WINDOW_H - PADDING * 2)

CENTER = (cfg.WINDOW_W // 2, cfg.WINDOW_H // 2)


MENU_FONT_CONFIG = {            
    "main_font": ui.MENU_FONT, 
    "highlight_font": ui.HIGHTLIGHT_FONT,
    "sub_font": ui.SUB_FONT,
    "main_color": cfg.PINK, 
    "highlight_color": cfg.WHITE,
    "sub_color": cfg.AQUA,
    "bg_color": cfg.BLACK, 
}


def build_title_menus(controller):
    return {
        MenuType.PLAYERS: build_players_menu(controller),
        MenuType.LEVEL: build_level_menu(controller),
        MenuType.MULTIPLAYER: build_multiplayer_menu(controller),
        MenuType.CUSTOM: build_custom_menu(controller),
        MenuType.BORDER: build_border_menu(controller),
        MenuType.CELL_SIZE: build_cell_size_menu(controller),
        MenuType.START_SPEED: build_start_speed_menu(controller),
        MenuType.ACCELERATION: build_acceleration_menu(controller),
        MenuType.FRUIT_QTY: build_fruit_qty_menu(controller),
        MenuType.GROWTH_RATE: build_growth_rate_menu(controller)
    }


def build_players_menu(controller):
    players_menu_items = [
        MenuItem("1 Player", controller.select_one_player, sub_text=None),
        MenuItem("2 Player", controller.select_two_player, sub_text=None)
    ]
    return Menu(players_menu_items, MENU_POS, MENU_SIZE, **MENU_FONT_CONFIG)


def build_level_menu(controller):
    level_menu_items = [
        MenuItem(
            "Classic",
            lambda: controller.select_level(pre_made.CLASSIC),
            "The classic snake experience",
        ),     
        MenuItem(
            "Zooomed",
            lambda: controller.select_level(pre_made.BIG),
            "Zooomed in. Classic with a twist - ZOOM"
        ),
        MenuItem(
            "Super\nClassic",
            lambda: controller.select_level(pre_made.SUPER),
            "More Fruit. More Growth. More Speed.",
        ),
        MenuItem(
            "Extreme",
            lambda: controller.select_level(pre_made.EXTREME), 
            "Everything turned up to 11 on a large map",
        ),
    
        MenuItem(
            "Insane",
            lambda: controller.select_level(pre_made.INSANE),
            "What even is this?"
        ),
        
        MenuItem(
            "Custom",
            controller.custom_level_menu,
            "Create your own game",
        )
    ]
    return Menu(level_menu_items, MENU_POS, MENU_SIZE, **MENU_FONT_CONFIG)


def build_multiplayer_menu(controller):
    multiplayer_menu_items = [
        MenuItem(
            "Death\nMatch", 
            lambda: controller.select_multiplayer_mode(RunDeathMatch),
            "Score when the other snake dies. 3 to win"
        ),
        MenuItem(
            "Score\nBattle", 
            lambda: controller.select_multiplayer_mode(RunScoreBattle),
            "Highest score held when the first snake dies wins"
        ),
        MenuItem(
            "Co-Op", 
            lambda: controller.select_multiplayer_mode(RunCoOp),
            "Work together to get a high score"
        )
    ]
    return Menu(
        multiplayer_menu_items, MENU_POS, MENU_SIZE, **MENU_FONT_CONFIG
    )


def build_custom_menu(controller):
    custom_level_items = [
        [
            MenuItem(
                "Cell\nSize",
                lambda: controller.menu_stack.push(controller.menus[MenuType.CELL_SIZE]),
                lvl_attr.CELL_SIZE_MEDIUM.name
            ),
            MenuItem(
                "Start\nSpeed",
                lambda: controller.menu_stack.push(controller.menus[MenuType.START_SPEED]),
                lvl_attr.START_SPEED_SLOW.name
            ),
            MenuItem(
                "Speed\nUp", 
                lambda: controller.menu_stack.push(controller.menus[MenuType.ACCELERATION]),
                lvl_attr.ACCELERATION_NONE.name
            ),
        ],
        [
             MenuItem(
                "Border\nWall", 
                lambda: controller.menu_stack.push(controller.menus[MenuType.BORDER]),
                lvl_attr.BORDER_ON.name
            ),
            MenuItem(
                "Fruit\nQuantity", 
                lambda: controller.menu_stack.push(controller.menus[MenuType.FRUIT_QTY]),
                lvl_attr.FRUIT_QTY_LOW.name
            ),
            MenuItem(
                "Growth\nRate",
                lambda: controller.menu_stack.push(controller.menus[MenuType.GROWTH_RATE]),
                lvl_attr.GROWTH_RATE_LOW.name
            ),

        ],
        [
            MenuItem(
                "Start\nGame",
                controller.start_custom_game,
                "Confirm Settings"
            )
        ]
    ]
    return MenuGrid(custom_level_items, MENU_GRID_POS, MENU_GRID_SIZE, MENU_FONT_CONFIG)
    
    
def build_border_menu(controller):
    word_banner = ui.WordBanner("Border Wall", False, cfg.PINK, 60)
    border_menu_items = [
        MenuItem(
            lvl_attr.BORDER_ON.name, 
            partial(controller.set_lvl_attr, lvl_attr.BORDER_ON)
        ),
        MenuItem(
            lvl_attr.BORDER_OFF.name, 
            partial(controller.set_lvl_attr, lvl_attr.BORDER_OFF)
        )
    ]
    return MenuGrid(border_menu_items, CENTER, MENU_GRID_SIZE, MENU_FONT_CONFIG, word_banner)


def build_cell_size_menu(controller):
    word_banner = ui.WordBanner("Cell Size", False, cfg.PINK, 60)
    cell_size_menu_items = [
        MenuItem(
            lvl_attr.CELL_SIZE_LARGE.name, 
            partial(controller.set_lvl_attr, lvl_attr.CELL_SIZE_LARGE)
        ),
        MenuItem(
            lvl_attr.CELL_SIZE_MEDIUM.name, 
            partial(controller.set_lvl_attr, lvl_attr.CELL_SIZE_MEDIUM)
        ),
        MenuItem(
            lvl_attr.CELL_SIZE_SMALL.name, 
            partial(controller.set_lvl_attr, lvl_attr.CELL_SIZE_SMALL)
        ),
        MenuItem(
            lvl_attr.CELL_SIZE_TINY.name, 
            partial(controller.set_lvl_attr, lvl_attr.CELL_SIZE_TINY)
        )
    ]
    return MenuGrid(cell_size_menu_items, CENTER, MENU_GRID_SIZE, MENU_FONT_CONFIG, word_banner)


def build_start_speed_menu(controller):
    word_banner = ui.WordBanner("Start Speed", False, cfg.PINK, 60)
    start_speed_menu_items = [
        MenuItem(
            lvl_attr.START_SPEED_SLOW.name, 
            partial(controller.set_lvl_attr, lvl_attr.START_SPEED_SLOW)
        ),
        MenuItem(
            lvl_attr.START_SPEED_MEDIUM.name, 
            partial(controller.set_lvl_attr, lvl_attr.START_SPEED_MEDIUM)
        ),
        MenuItem(
            lvl_attr.START_SPEED_FAST.name, 
            partial(controller.set_lvl_attr, lvl_attr.START_SPEED_FAST)
        ),
    ]
    return MenuGrid(start_speed_menu_items, CENTER, MENU_GRID_SIZE, MENU_FONT_CONFIG, word_banner)


def build_acceleration_menu(controller):
    word_banner = ui.WordBanner("Speed Up", False, cfg.PINK, 60)
    acceleration_menu_items = [
        MenuItem(
            lvl_attr.ACCELERATION_NONE.name, 
            partial(controller.set_lvl_attr, lvl_attr.ACCELERATION_NONE)
        ),
        MenuItem(
            lvl_attr.ACCELERATION_LOW.name, 
            partial(controller.set_lvl_attr, lvl_attr.ACCELERATION_LOW)
        ),
        MenuItem(
            lvl_attr.ACCELERATION_HIGH.name, 
            partial(controller.set_lvl_attr, lvl_attr.ACCELERATION_HIGH)
        ),
    ]
    
    return MenuGrid(acceleration_menu_items, CENTER, MENU_GRID_SIZE, MENU_FONT_CONFIG, word_banner)


def build_fruit_qty_menu(controller):
    word_banner = ui.WordBanner("Fruit Quantity", False, cfg.PINK, 60)
    fruit_qty_menu_items = [
        MenuItem(
            lvl_attr.FRUIT_QTY_LOW.name, 
            partial(controller.set_lvl_attr, lvl_attr.FRUIT_QTY_LOW)
        ),
        MenuItem(
            lvl_attr.FRUIT_QTY_MEDIUM.name, 
            partial(controller.set_lvl_attr, lvl_attr.FRUIT_QTY_MEDIUM)
        ),
        MenuItem(
            lvl_attr.FRUIT_QTY_HIGH.name, 
            partial(controller.set_lvl_attr, lvl_attr.FRUIT_QTY_HIGH)
        ),
    ]
    return MenuGrid(fruit_qty_menu_items, CENTER, MENU_GRID_SIZE, MENU_FONT_CONFIG, word_banner)


def build_growth_rate_menu(controller):
    word_banner = ui.WordBanner("Growth Rate", False, cfg.PINK, 60)
    growth_rate_menu_items = [
        MenuItem(
            lvl_attr.GROWTH_RATE_LOW.name, 
            partial(controller.set_lvl_attr, lvl_attr.GROWTH_RATE_LOW)
        ),
        MenuItem(
            lvl_attr.GROWTH_RATE_MEDIUM.name, 
            partial(controller.set_lvl_attr, lvl_attr.GROWTH_RATE_MEDIUM)
        ),
        MenuItem(
            lvl_attr.GROWTH_RATE_HIGH.name, 
            partial(controller.set_lvl_attr, lvl_attr.GROWTH_RATE_HIGH)
        ),
    ]
    return MenuGrid(growth_rate_menu_items, CENTER, MENU_GRID_SIZE, MENU_FONT_CONFIG, word_banner)