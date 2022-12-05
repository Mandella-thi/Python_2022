class NewSample():
    pass
new_obj = NewSample()
print(type(new_obj))
#Player = type('Player',(Team), {})

class Player:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.number = 7
    def init(self, name, roll):
        self.name = name
        self.rool =roll
        self.number =7

    Player= type('Player', (),{'__init__': init})
    new_obj = Player("Ahmed",'70')
    print(new_obj.__class__)

class NewMeta(type):
    __metaclass__ = type
class NewDemo:
    __metaclass__ = NewMeta
new_object = NewDemo()
print(new_object.__metaclass__)
print(NewMeta.__metaclass__)