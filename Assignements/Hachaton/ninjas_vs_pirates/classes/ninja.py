class Character:
    def __init__(self, name, strengh, speed, health):
        self.name = name
        self.strength = strengh
        self.speed = speed
        self.health = health
        
    def show_stats(self):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , obj ):
        obj.health -= self.strength
        return self

    def is_alive(self):
        return self.health > 0

class Ninja(Character):

    def __init__( self , name, strengh=10, speed=5, health=100 ):
        super().__init__(name, strengh, speed, health)
     

class Pirate(Character):

    def __init__( self , name, strengh=15, speed=3, health=100 ):
        super().__init__(name, strengh, speed, health)

class Battle:
    @staticmethod
    def start_battle(ninja, pirate):
        round = 1
        while ninja.is_alive() and pirate.is_alive():
            print(f"Round: {round}")
            ninja.attack(pirate)
            if pirate.is_alive():
                pirate.attack(ninja)
            else:
                print(f"{pirate.name} is defeated")
                break
            if not ninja.is_alive():
                print(f"{ninja.name} is defeated")
                break
            ninja.show_stats()
            pirate.show_stats()
            round+=1
            
    #declare_winner
    @staticmethod
    def declare_winner(ninja, pirate):
        if(ninja.is_alive()):
            print(f"{ninja.name} is the Winner")
        elif(pirate.is_alive()):
            print(f"{pirate.name} is the Winner")
        else:
            print("Draw")
    
    
michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

#michelangelo.attack(jack_sparrow)
#jack_sparrow.show_stats()

Battle.start_battle(michelangelo, jack_sparrow)