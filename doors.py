class Doors:
    def __init__(self):
        pass
    
    def load_images(self):
        pass

    def make_rects(self):
        pass

    def get_fire_door_loc(self):
        pass

    def get_water_door_loc(self):
        pass

    def try_raise_door(self, door):
        pass



class DoorsLevel1(Doors):
    fire_door_location = (0,0)
    water_door_locaton = (0,0)
    super().__init__()