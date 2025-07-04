from functools import partial

import src.app_config as cfg
from src.enums import MenuTypes
import src.level_config.level_config as levels
from src.level_config import options
from src.ui.menu import Menu, MenuGrid, MenuItem
from src.game_states.run_co_op import RunCoOp
from src.game_states.run_deathmatch import RunDeathMatch
from src.game_states.run_score_battle import RunScoreBattle
import src.ui.ui_elements as ui


MENU_HEIGHT = ui.PRESS_SPACE_RECT.top - ui.TITLE_RECT.bottom 
MENU_POS = (ui.TITLE_RECT.midbottom)
MENU_SIZE = (cfg.WINDOW_W * 0.9, MENU_HEIGHT)

MENU_GRID_HEIGHT = ui.PRESS_SPACE_RECT.top - ui.PING_PANG_RECT.bottom
MENU_GRID_POS = (ui.PING_PANG_RECT.midbottom[0], ui.PING_PANG_RECT.midbottom[1] + MENU_GRID_HEIGHT * .1)
MENU_GRID_SIZE = (cfg.WINDOW_W * 0.9, MENU_GRID_HEIGHT)

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
        MenuTypes.PLAYERS: build_players_menu(controller),
        MenuTypes.LEVEL: build_level_menu(controller),
        MenuTypes.MULTIPLAYER: build_multiplayer_menu(controller),
        MenuTypes.CUSTOM: build_custom_menu(controller),
        MenuTypes.BORDER: build_border_menu(controller),
        MenuTypes.CELL_SIZE: build_cell_size_menu(controller),
        MenuTypes.START_SPEED: build_start_speed_menu(controller),
        MenuTypes.ACCELERATION: build_acceleration_menu(controller),
        MenuTypes.FRUIT_QTY: build_fruit_qty_menu(controller),
        MenuTypes.GROWTH_RATE: build_growth_rate_menu(controller)
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
            lambda: controller.select_level(levels.CLASSIC),
            "The classic snake experience",
        ),     
        MenuItem(
            "Zooomed",
            lambda: controller.select_level(levels.BIG),
            "Zooomed in. Classic with a twist - ZOOM"
        ),
        MenuItem(
            "Super\nClassic",
            lambda: controller.select_level(levels.SUPER),
            "More Fruit. More Growth. More Speed.",
        ),
        MenuItem(
            "Extreme",
            lambda: controller.select_level(levels.EXTREME), 
            "Everything turned up to 11 on a large map",
        ),
    
        MenuItem(
            "Insane",
            lambda: controller.select_level(levels.INSANE),
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
                "Border\nWall", 
                lambda: controller.stack.push(controller.menus[MenuTypes.BORDER]),
                options.BORDER_ON.name
            ),
            MenuItem(
                "Cell\nSize",
                lambda: controller.stack.push(controller.menus[MenuTypes.CELL_SIZE]),
                options.CELL_SIZE_MEDIUM.name
            ),
            MenuItem(
                "Start\nSpeed",
                lambda: controller.stack.push(controller.menus[MenuTypes.START_SPEED]),
                options.START_SPEED_SLOW.name
            ),
            MenuItem(
                "Speed\nUp", 
                lambda: controller.stack.push(controller.menus[MenuTypes.ACCELERATION]),
                options.ACCELERATION_NONE.name
            ),
        ],
        [
            MenuItem(
                "Fruit\nQuantity", 
                lambda: controller.stack.push(controller.menus[MenuTypes.FRUIT_QTY]),
                options.FRUIT_QTY_LOW.name
            ),
            MenuItem(
                "Start\nGame",
                controller.start_custom_game,
                "Confirm Settings"
            ),  
            MenuItem(
                "Growth\nRate",
                lambda: controller.stack.push(controller.menus[MenuTypes.GROWTH_RATE]),
                options.GROWTH_RATE_LOW.name
            ),

        ]
    ]
    return MenuGrid(custom_level_items, MENU_GRID_POS, MENU_GRID_SIZE, MENU_FONT_CONFIG)
    
    
def build_border_menu(controller):
    border_menu_items = [
        MenuItem(
            options.BORDER_ON.name, 
            partial(controller.set_border, options.BORDER_ON)
        ),
        MenuItem(
            options.BORDER_OFF.name, 
            partial(controller.set_border, options.BORDER_OFF)
        )
    ]
    return MenuGrid(border_menu_items, CENTER, MENU_SIZE, MENU_FONT_CONFIG)


def build_cell_size_menu(controller):
    cell_size_menu_items = [
        MenuItem(
            options.CELL_SIZE_LARGE.name, 
            partial(controller.set_cell_size, options.CELL_SIZE_LARGE)
        ),
        MenuItem(
            options.CELL_SIZE_MEDIUM.name, 
            partial(controller.set_cell_size, options.CELL_SIZE_MEDIUM)
        ),
        MenuItem(
            options.CELL_SIZE_SMALL.name, 
            partial(controller.set_cell_size, options.CELL_SIZE_SMALL)
        ),
    ]
    return MenuGrid(cell_size_menu_items, CENTER, MENU_SIZE, MENU_FONT_CONFIG)


def build_start_speed_menu(controller):
    start_speed_menu_items = [
        MenuItem(
            options.START_SPEED_SLOW.name, 
            partial(controller.set_start_speed, options.START_SPEED_SLOW)
        ),
        MenuItem(
            options.START_SPEED_MEDIUM.name, 
            partial(controller.set_start_speed, options.START_SPEED_MEDIUM)
        ),
        MenuItem(
            options.START_SPEED_FAST.name, 
            partial(controller.set_start_speed, options.START_SPEED_FAST)
        ),
    ]
    return MenuGrid(start_speed_menu_items, CENTER, MENU_SIZE, MENU_FONT_CONFIG)


def build_acceleration_menu(controller):
    acceleration_menu_items = [
        MenuItem(
            options.ACCELERATION_NONE.name, 
            partial(controller.set_acceleration, options.ACCELERATION_NONE)
        ),
        MenuItem(
            options.ACCELERATION_LOW.name, 
            partial(controller.set_acceleration, options.ACCELERATION_LOW)
        ),
        MenuItem(
            options.ACCELERATION_HIGH.name, 
            partial(controller.set_acceleration, options.ACCELERATION_HIGH)
        ),
    ]
    
    return MenuGrid(acceleration_menu_items, CENTER, MENU_SIZE, MENU_FONT_CONFIG)


def build_fruit_qty_menu(controller):
    fruit_qty_menu_items = [
        MenuItem(
            options.FRUIT_QTY_LOW.name, 
            partial(controller.set_fruit_qty, options.FRUIT_QTY_LOW)
        ),
        MenuItem(
            options.FRUIT_QTY_MEDIUM.name, 
            partial(controller.set_fruit_qty, options.FRUIT_QTY_MEDIUM)
        ),
        MenuItem(
            options.FRUIT_QTY_HIGH.name, 
            partial(controller.set_fruit_qty, options.FRUIT_QTY_HIGH)
        ),
    ]
    return MenuGrid(fruit_qty_menu_items, CENTER, MENU_SIZE, MENU_FONT_CONFIG)


def build_growth_rate_menu(controller):
    growth_rate_menu_items = [
        MenuItem(
            options.GROWTH_RATE_LOW.name, 
            partial(controller.set_growth_rate, options.GROWTH_RATE_LOW)
        ),
        MenuItem(
            options.GROWTH_RATE_MEDIUM.name, 
            partial(controller.set_growth_rate, options.GROWTH_RATE_MEDIUM)
        ),
        MenuItem(
            options.GROWTH_RATE_HIGH.name, 
            partial(controller.set_growth_rate, options.GROWTH_RATE_HIGH)
        ),
    ]
    return MenuGrid(growth_rate_menu_items, CENTER, MENU_SIZE, MENU_FONT_CONFIG)