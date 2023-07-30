import math

class GeometryCalculator:
    def __init__(self): 
        self.math=math
        
    def calculate_cicrcle_area(self, *radius):
        return math.pi * radius ** 2
    