#Starting Statement
#Super() function is used to call the parent class constructor
#Creating Parent Class
class Bird:
    def __init__(self):
        print('Bird is ready')

    def whoisThis(self):
        print('Bird')
    
    def swim(self):
        print('Swim faster')

#Creating Child Class

class Pengiun(Bird):
    def __init__(self): 
        #Calling the super() function
        super().__init__()
        print('Penguin is ready')

    def whoisThis(self):
        print('Penguin')

    def run(self):
        print('Run faster')

#Creating obejct of child class

peggy = Pengiun()
peggy.whoisThis()
peggy.swim()
peggy.run()
#Ending Statement
# Output
# Bird is ready
# Penguin is ready
# Penguin
# Swim faster
# Run faster
# The output shows that the super() function is used to call the parent class constructor
# and the child class constructor is called using the super() function.
# The output also shows that the child class method is called instead of the parent class method.    