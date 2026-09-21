class vechile:
    def brand(self):
        print("BMW")
        
class car(vechile):
    def model(self):
        print("2025")
        
        
class color(vechile):
    def display(self):
        print("Blue")
d1=vechile()
d1.brand()
d2=car()
d2.model()
d3=color()
d3.display()