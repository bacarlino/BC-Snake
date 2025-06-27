from src.level_config.level_config import LevelConfig


class LevelConfigController:

    def __init__(self):
        self.level_config = LevelConfig(
            has_border=True,
            start_speed=6,
            acceleration=0,
            cell_size=40,
            fruit_qty=1,
            growth_rate=1      
        )
    def get_level_config(self):
        return self.level_config

    def has_border_sub_text(self):
        return "On" if self.level_config.has_border else "Off"
    
    def cell_size_sub_text(self):
        print(f"Cell Size: {self.level_config.cell_size}")
        if self.level_config.cell_size == 20:
            return "Small"
        elif self.level_config.cell_size == 40:
            return "Medium"
        elif self.level_config.cell_size == 80:
            return "Big"
        
    def start_speed_sub_text(self):
        print(f"Start Speed: {self.level_config.start_speed}")
        if self.level_config.start_speed == 6:
            return "Slow"
        elif self.level_config.start_speed == 8:
            return "Medium"
        elif self.level_config.start_speed == 10:
            return "Fast"

    def acceleration_sub_text(self):
        print("Speed up: ", self.level_config.acceleration)
        if self.level_config.acceleration == 0:
            return "Off"
        elif self.level_config.acceleration == 1.5:
            return "Low"
        elif self.level_config.acceleration == 2.5:
            return "High"
        else:
            return "Error"
     
    def fruit_qty_sub_text(self):
        print("Fruit qty: ", self.level_config.fruit_qty)
        if self.level_config.fruit_qty == 1:
            return "Low"
        elif self.level_config.fruit_qty == 5:
            return "Medium"
        elif self.level_config.fruit_qty == 25:
            return "High"
        
    def growth_rate_sub_text(self):
        if self.level_config.growth_rate == 1:
            return "Low"
        elif self.level_config.growth_rate == 3:
            return "Medium"
        elif self.level_config.growth_rate == 10:
            return "High"