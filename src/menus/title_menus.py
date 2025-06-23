import src.app_config as cfg
import src.level_config as levels
from src.menus.menu import Menu, MenuGrid, MenuItem
from src.game_states.run_co_op import RunCoOp
from src.game_states.run_deathmatch import RunDeathMatch
from src.game_states.run_score_battle import RunScoreBattle
import src.ui_elements as ui


MENU_HEIGHT = ui.PRESS_SPACE_RECT.top - ui.TITLE_RECT.bottom 
MENU_POS = (ui.TITLE_RECT.midbottom)
MENU_SIZE = (cfg.WINDOW_W * 0.9, MENU_HEIGHT)

MENU_GRID_HEIGHT = ui.PRESS_SPACE_RECT.top - ui.PING_PANG_RECT.bottom
MENU_GRID_POS = (ui.PING_PANG_RECT.midbottom[0], ui.PING_PANG_RECT.midbottom[1] + MENU_GRID_HEIGHT * .15)
MENU_GRID_SIZE = (cfg.WINDOW_W * 0.9, MENU_GRID_HEIGHT)


MENU_COLORS = {            
    "main_font": ui.MENU_FONT, 
    "highlight_font": ui.HIGHTLIGHT_FONT,
    "sub_font": ui.SUB_FONT,
    "main_color": cfg.PINK, 
    "highlight_color": cfg.WHITE,
    "sub_color": cfg.AQUA,
    "bg_color": cfg.BLACK, 
}

def build_title_menus(state):
    return {
        "players": build_players_menu(state),
        "level": build_level_menu(state),
        "multiplayer": build_multiplayer_menu(state),
        "custom": build_custom_menu(state),
        "perimeter": build_perimeter_menu(state),
        "cell_size": build_cell_size_menu(state),
        "start_speed": build_start_speed_menu(state),
        "acceleration": build_acceleration_menu(state),
        "fruit_qty": build_fruit_qty_menu(state),
        "growth_rate": build_growth_rate_menu(state)
    }


def build_players_menu(state):
    players_menu_items = [
        MenuItem("1 Player", state.select_one_player, sub_text=None),
        MenuItem("2 Player", state.select_two_player, sub_text=None)
    ]
    return Menu(players_menu_items, MENU_POS, MENU_SIZE, **MENU_COLORS)


def build_level_menu(state):
    level_menu_items = [
        MenuItem(
            "Classic",
            lambda: state.select_level(levels.CLASSIC),
            "The classic snake experience",
        ),     
        MenuItem(
            "Zooomed",
            lambda: state.select_level(levels.BIG),
            "Zooomed in. Classic with a twist - ZOOM"
        ),
        MenuItem(
            "Super\nClassic",
            lambda: state.select_level(levels.SUPER),
            "More Fruit. More Growth. More Speed.",
        ),
        MenuItem(
            "Extreme",
            lambda: state.select_level(levels.EXTREME), 
            "Everything turned up to 11 on a large map",
        ),
    
        MenuItem(
            "Insane",
            lambda: state.select_level(levels.INSANE),
            "What even is this?"
        ),
        
        MenuItem(
            "Custom",
            # lambda: state.menu.push(state.custom_level_menu_grid),
            state.custom_level_menu,
            "Create your own game",
        )
    ]
    return Menu(level_menu_items, MENU_POS, MENU_SIZE, **MENU_COLORS)


def build_multiplayer_menu(state):
    multiplayer_menu_items = [
        MenuItem(
            "Death\nMatch", 
            lambda: state.select_multiplayer_mode(RunDeathMatch),
            "Score when the other snake dies. 3 to win"
        ),
        MenuItem(
            "Score\nBattle", 
            lambda: state.select_multiplayer_mode(RunScoreBattle),
            "Highest score held when the first snake dies wins"
        ),
        MenuItem(
            "Co-Op", 
            lambda: state.select_multiplayer_mode(RunCoOp),
            "Work together to get a high score"
        )
    ]
    return Menu(
        multiplayer_menu_items, MENU_POS, MENU_SIZE, **MENU_COLORS
    )


def build_custom_menu(state):
    custom_level_items = [
        [
            MenuItem(
                "Perimeter\nWall", 
                lambda: state.menu.push(state.menus["perimeter"]),
                f"{state.has_border_sub_text()}"
            ),
            MenuItem(
                "Cell\nSize",
                lambda: state.menu.push(state.menus["cell_size"]),
                f"{state.cell_size_sub_text()}"
            ),
            MenuItem(
                "Start\nSpeed",
                lambda: state.menu.push(state.menus["start_speed"]),
                f"{state.start_speed_sub_text()}"
            ),
            MenuItem(
                "Speed\nUp", 
                lambda: state.menu.push(state.menus["acceleration"]),
                f"{state.acceleration_sub_text()}"
            ),
        ],
        [
            MenuItem(
                "Fruit\nQuantity", 
                lambda: state.menu.push(state.menus["fruit_qty"]),
                f"{state.fruit_qty_sub_text()}"
            ),
            MenuItem(
                "Start\nGame",
                state.start_custom_game,
                "Confirm Settings"
            ),  
            MenuItem(
                "Growth\nRate",
                lambda: state.menu.push(state.menus["growth_rate"]),
                f"{state.growth_rate_sub_text()}"
            ),

        ]
    ]
    return MenuGrid(custom_level_items, MENU_GRID_POS, MENU_GRID_SIZE, MENU_COLORS)
    
    
def build_perimeter_menu(state):
    perimeter_menu_items = [
        MenuItem("On", state.perimeter_on, sub_text=None),
        MenuItem("Off", state.perimeter_off, sub_text=None)
    ]
    return Menu(perimeter_menu_items, MENU_POS, MENU_SIZE, **MENU_COLORS)


def build_cell_size_menu(state):
    cell_size_menu_items = [
        MenuItem("Big", state.cell_size_large, sub_text=None),
        MenuItem("Medium", state.cell_size_medium, sub_text=None),
        MenuItem("Small", state.cell_size_small, sub_text=None),
    ]
    return Menu(cell_size_menu_items, MENU_POS, MENU_SIZE, **MENU_COLORS)


def build_start_speed_menu(state):
    start_speed_menu_items = [
        MenuItem("Slow", state.start_speed_slow, sub_text=None),
        MenuItem("Medium", state.start_speed_medium, sub_text=None),
        MenuItem("Fast", state.start_speed_fast, sub_text=None)
    ]
    return Menu(start_speed_menu_items, MENU_POS, MENU_SIZE, **MENU_COLORS)


def build_acceleration_menu(state):
    acceleration_menu_items = [
        MenuItem("Off", state.acceleration_off, sub_text=None),
        MenuItem("Low", state.acceleration_low, sub_text=None),
        MenuItem("High", state.acceleration_high, sub_text=None)
    ]
    
    return Menu(acceleration_menu_items, MENU_POS, MENU_SIZE, **MENU_COLORS)


def build_fruit_qty_menu(state):
    fruit_qty_menu_items = [
        MenuItem("Low", state.fruit_qty_low, sub_text=None),
        MenuItem("Medium", state.fruit_qty_medium, sub_text=None),
        MenuItem("High", state.fruit_qty_high, sub_text=None)
    ]
    return Menu(fruit_qty_menu_items, MENU_POS, MENU_SIZE, **MENU_COLORS)


def build_growth_rate_menu(state):
    growth_rate_menu_items = [
        MenuItem("Low", state.growth_rate_low, sub_text=None),
        MenuItem("Medium", state.growth_rate_medium, sub_text=None),
        MenuItem("High", state.growth_rate_high, sub_text=None)
    ]
    return Menu(growth_rate_menu_items, MENU_POS, MENU_SIZE, **MENU_COLORS)