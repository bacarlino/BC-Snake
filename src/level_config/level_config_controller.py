from src.level_config.level_config import LevelConfig
from src.level_config import level_attributes as lvl_attr


class LevelConfigController:

    def __init__(self):
        self.has_border = lvl_attr.BORDER_ON
        self.start_speed = lvl_attr.START_SPEED_SLOW
        self.acceleration = lvl_attr.ACCELERATION_NONE
        self.cell_size = lvl_attr.CELL_SIZE_MEDIUM
        self.fruit_qty = lvl_attr.FRUIT_QTY_LOW
        self.growth_rate = lvl_attr.GROWTH_RATE_LOW
        (self.has_border.value)


    def get_level_config(self):
        return LevelConfig(
            has_border=self.has_border.value,
            start_speed=self.start_speed.value,
            acceleration=self.acceleration.value,
            cell_size=self.cell_size.value,
            fruit_qty=self.fruit_qty.value,
            growth_rate=self.growth_rate.value      
        )
    
    def set_attr(self, attr):
        pass