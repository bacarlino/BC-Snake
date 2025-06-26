class LevelConfigController:

    def __init__(self):
        self.has_border = True
        self.start_speed = 6
        self.acceleration = 0
        self.cell_size = 32
        self.fruit_qty = 1
        self.growth_rate = 1 

    def has_border_sub_text(self):
        return "On" if self.has_border else "Off"
    
    def cell_size_sub_text(self):
        print(f"Cell Size: {self.cell_size}")
        if self.cell_size == 16:
            return "Small"
        elif self.cell_size == 32:
            return "Medium"
        elif self.cell_size == 64:
            return "Big"
        
    def start_speed_sub_text(self):
        print(f"Start Speed: {self.start_speed}")
        if self.start_speed == 6:
            return "Slow"
        elif self.start_speed == 8:
            return "Medium"
        elif self.start_speed == 10:
            return "Fast"

    def acceleration_sub_text(self):
        print("Speed up: ", self.acceleration)
        if self.acceleration == 0:
            return "Off"
        elif self.acceleration == 1.5:
            return "Low"
        elif self.acceleration == 2.5:
            return "High"
        else:
            return "Error"
     
    def fruit_qty_sub_text(self):
        print("Fruit qty: ", self.fruit_qty)
        if self.fruit_qty == 1:
            return "Low"
        elif self.fruit_qty == 5:
            return "Medium"
        elif self.fruit_qty == 25:
            return "High"
        
    def growth_rate_sub_text(self):
        if self.growth_rate == 1:
            return "Low"
        elif self.growth_rate == 3:
            return "Medium"
        elif self.growth_rate == 10:
            return "High"