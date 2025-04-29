class PaintBrush:
    def __init__(self, size, color, brand, brush_type):
        self.size = size
        self.color = color
        self.brand = brand
        self.brush_type =  brush_type

    def paint (self):
        print (f"Size: {self.size}, Color: {self.color}, Brand: {self.brand}, Type: {self.brush_type}")

# Creating an instance for PaintBrusg
my_brush = PaintBrush('Medium', 'Red', 'Winson & Newton', 'Round')

# Calling the print method
my_brush.paint()