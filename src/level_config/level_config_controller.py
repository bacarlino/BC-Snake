from src.level_config.level_config import LevelConfig
from src.level_config import level_attributes


class LevelConfigController:

    def __init__(self):
        self.has_border = level_attributes.BORDER_ON
        self.start_speed = level_attributes.START_SPEED_SLOW
        self.acceleration = level_attributes.ACCELERATION_NONE
        self.cell_size = level_attributes.CELL_SIZE_MEDIUM
        self.fruit_qty = level_attributes.FRUIT_QTY_LOW
        self.growth_rate = level_attributes.GROWTH_RATE_LOW
        print(self.has_border.value)


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