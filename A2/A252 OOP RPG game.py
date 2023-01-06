import random

class Character:
    def __init__(self, name, max_hp, attack, defense):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def attack_damage(self):
        return self.attack + random.randint(-2, 2)

    def defend(self, damage):
        return max(0, damage - self.defense)

    def is_dead(self):
        return self.hp == 0


def main():
    player = Character("Player", 10, 3, 2)
    enemy = Character("Enemy", 10, 3, 2)

    while not player.is_dead() and not enemy.is_dead():
        print(f"{player.name}: {player.hp} HP  {enemy.name}: {enemy.hp} HP")
        action = input("What do you want to do? A to attack, H to heal: ")
        if action == 'A':
            damage = player.attack_damage()
            enemy.take_damage(damage)
            print(f"{player.name} attacked for {damage} damage!")
        elif action == 'H':
            player.heal(2)
            print(f"{player.name} healed 2 HP!")
        else:
            print("Invalid action")
            continue

        if enemy.is_dead():
            print(f"{enemy.name} is defeated!")
            break
        damage = enemy.attack_damage()
        player.take_damage(damage)
        print(f"{enemy.name} attack for {damage} damage!")

    print(f"{player.name}: {player.hp} HP  {enemy.name}: {enemy.hp} HP")

    if player.is_dead():
        print("You lose!")
    else:
        print("You win!")

main()
