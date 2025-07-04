from src.level_config.level_config import LevelConfig
from src.level_config import options


class LevelConfigController:

    def __init__(self):
        self.has_border = options.BORDER_ON
        self.start_speed = options.START_SPEED_SLOW
        self.acceleration = options.ACCELERATION_NONE
        self.cell_size = options.CELL_SIZE_MEDIUM
        self.fruit_qty = options.FRUIT_QTY_LOW
        self.growth_rate = options.GROWTH_RATE_LOW
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