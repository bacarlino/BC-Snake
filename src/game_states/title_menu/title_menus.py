import src.app_config as cfg
from src.enums import MenuTypes
import src.level_config.level_config as levels
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
        MenuTypes.PERIMETER: build_perimeter_menu(controller),
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
            # lambda: controller.menu.push(controller.custom_level_menu_grid),
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
                "Perimeter\nWall", 
                lambda: controller.stack.push(controller.menus[MenuTypes.PERIMETER]),
                f"{controller.level_config.has_border_sub_text()}"
            ),
            MenuItem(
                "Cell\nSize",
                lambda: controller.stack.push(controller.menus[MenuTypes.CELL_SIZE]),
                f"{controller.level_config.cell_size_sub_text()}"
            ),
            MenuItem(
                "Start\nSpeed",
                lambda: controller.stack.push(controller.menus[MenuTypes.START_SPEED]),
                f"{controller.level_config.start_speed_sub_text()}"
            ),
            MenuItem(
                "Speed\nUp", 
                lambda: controller.stack.push(controller.menus[MenuTypes.ACCELERATION]),
                f"{controller.level_config.acceleration_sub_text()}"
            ),
        ],
        [
            MenuItem(
                "Fruit\nQuantity", 
                lambda: controller.stack.push(controller.menus[MenuTypes.FRUIT_QTY]),
                f"{controller.level_config.fruit_qty_sub_text()}"
            ),
            MenuItem(
                "Start\nGame",
                controller.start_custom_game,
                "Confirm Settings"
            ),  
            MenuItem(
                "Growth\nRate",
                lambda: controller.stack.push(controller.menus[MenuTypes.GROWTH_RATE]),
                f"{controller.level_config.growth_rate_sub_text()}"
            ),

        ]
    ]
    return MenuGrid(custom_level_items, MENU_GRID_POS, MENU_GRID_SIZE, MENU_FONT_CONFIG)
    
    
def build_perimeter_menu(controller):
    perimeter_menu_items = [
        MenuItem("On", controller.perimeter_on, sub_text=None),
        MenuItem("Off", controller.perimeter_off, sub_text=None)
    ]
    return MenuGrid(perimeter_menu_items, CENTER, MENU_SIZE, MENU_FONT_CONFIG)


def build_cell_size_menu(controller):
    cell_size_menu_items = [
        MenuItem("Big", controller.cell_size_large, sub_text=None),
        MenuItem("Medium", controller.cell_size_medium, sub_text=None),
        MenuItem("Small", controller.cell_size_small, sub_text=None),
    ]
    return MenuGrid(cell_size_menu_items, CENTER, MENU_SIZE, MENU_FONT_CONFIG)


def build_start_speed_menu(controller):
    start_speed_menu_items = [
        MenuItem("Slow", controller.start_speed_slow, sub_text=None),
        MenuItem("Medium", controller.start_speed_medium, sub_text=None),
        MenuItem("Fast", controller.start_speed_fast, sub_text=None)
    ]
    return MenuGrid(start_speed_menu_items, CENTER, MENU_SIZE, MENU_FONT_CONFIG)


def build_acceleration_menu(controller):
    acceleration_menu_items = [
        MenuItem("Off", controller.acceleration_off, sub_text=None),
        MenuItem("Low", controller.acceleration_low, sub_text=None),
        MenuItem("High", controller.acceleration_high, sub_text=None)
    ]
    
    return MenuGrid(acceleration_menu_items, CENTER, MENU_SIZE, MENU_FONT_CONFIG)


def build_fruit_qty_menu(controller):
    fruit_qty_menu_items = [
        MenuItem("Low", controller.fruit_qty_low, sub_text=None),
        MenuItem("Medium", controller.fruit_qty_medium, sub_text=None),
        MenuItem("High", controller.fruit_qty_high, sub_text=None)
    ]
    return MenuGrid(fruit_qty_menu_items, CENTER, MENU_SIZE, MENU_FONT_CONFIG)


def build_growth_rate_menu(controller):
    growth_rate_menu_items = [
        MenuItem("Low", controller.growth_rate_low, sub_text=None),
        MenuItem("Medium", controller.growth_rate_medium, sub_text=None),
        MenuItem("High", controller.growth_rate_high, sub_text=None)
    ]
    return MenuGrid(growth_rate_menu_items, CENTER, MENU_SIZE, MENU_FONT_CONFIG)