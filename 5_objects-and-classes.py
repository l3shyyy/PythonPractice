class Robot:
    def introduce_self(self):
        print("Hello, my name is " + self.name)
#Constructor
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

#r1 = Robot()
#r1.name = "Joe"
#r1.color = "Green"
#r1.weight = "250"

#r2 = Robot()
#r2.name = "Rob"
#r2.color = "Blue"
#r2.weight = "400"

#r1.introduce_self()
#r2.introduce_self()

r1 = Robot("Ruth", "Teal", 50)
r2 = Robot("Jacob", "Orange", 340)

r1.introduce_self()
