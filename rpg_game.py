class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, opponent):
        if opponent.health <= 0:
            print(f"{opponent.name} is already defeated!")
        else:
            opponent.health -= self.attack_power
            print(f"{self.name} attacks {opponent.name}! {opponent.name}'s health is now {opponent.health}")
            if opponent.health <= 0:
                print(f"{self.name} wins!")

batman=Character("batman",100,30)
superman=Character("superman",100,40)
batman.attack(superman)
superman.attack(batman)
batman.attack(superman)
superman.attack(batman)
superman.attack(batman)
