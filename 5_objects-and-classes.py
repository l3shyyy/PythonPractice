class Robot:
    #Constructor
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
    def introduce_self(self):
        print("Hello, my name is " + self.name)

class Person: 
    def __init__(self, name, personality, isSitting):
        self.name = name
        self.personality = personality
        self.isSitting = isSitting
        
    def sit_down(self):
        self.isSitting = False
    def stand_up(self):
        self.isSitting = True

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

p1 = Person("Jane","Friendly", False)
p1.robot_owned = r2

p1.robot_owned.introduce_self()