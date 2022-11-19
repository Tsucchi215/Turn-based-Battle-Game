import random

class GameCharacter:
    def __init__(self, unit_type, unit_name):
        self.unit_type = unit_type
        self.unit_name = unit_name
        self.hp = 20
        self.ak = 0
        self.df = 0
        self.xp = 0
        self.rk = 0
        if unit_type == "w":
            self.setup_warrior()
        elif unit_type == "t":
            self.setup_tanker()

    def setup_warrior(self):
        self.ak = random.randint(10, 20)
        self.df = random.randint(1, 10)
        self.rk = 1

    def setup_tanker(self):
        self.ak = random.randint(5, 10)
        self.df = random.randint(5, 15)
        self.rk = 1

    def __str__(self):
        text = "Name: " + self.unit_name
        text += "HP: " + str(self.hp) + "\n"
        return text

    def attack(self, target):
        self.damage = self.ak - target.df + random.randint(-5, 10)
        target.hp -= self.damage
    
        if (self.damage > 0):
            self.xp += self.damage

        target.xp += target.df

        print(f'{self.unit_name} Attack {target.unit_name} with {self.damage} Damage')

        if (self.damage > 10):
            target.xp += (target.df / 100) * 20   
        elif(self.damage <= 0):
            target.xp += (target.df / 100) * 50
        
        if (self.xp > 100):
                self.xp -= 100
                self.rk += 1
                self.ak += 2
                self.df += 1
        if (target.xp > 100):
                target.xp -= 100
                target.rk += 1
                target.rk += 2
                target.rk += 1