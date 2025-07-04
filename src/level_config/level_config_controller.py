from src.level_config.level_config import LevelConfig


class LevelConfigController:

    def __init__(self):
        self.has_border = True
        self.start_speed = 6
        self.acceleration = 0
        self.cell_size = 40
        self.fruit_qty = 1
        self.growth_rate = 1


    def get_level_config(self):
        return LevelConfig(
            has_border=self.has_border,
            start_speed=self.start_speed,
            acceleration=self.acceleration,
            cell_size=self.cell_size,
            fruit_qty=self.fruit_qty,
            growth_rate=self.growth_rate      
        )