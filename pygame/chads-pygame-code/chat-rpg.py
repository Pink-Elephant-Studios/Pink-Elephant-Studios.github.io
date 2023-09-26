import random

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

    def attack_enemy(self, enemy):
        damage = random.randint(1, self.attack)
        enemy.take_damage(damage)
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")

class Monster(Character):
    def __init__(self, name, health, attack):
        super().__init__(name, health, attack)

def main():
    print("Welcome to the Simple RPG!")
    player_name = input("Enter your character's name: ")
    player = Character(player_name, health=100, attack=20)

    monsters = [Monster("Goblin", health=30, attack=10),
                Monster("Orc", health=50, attack=15),
                Monster("Dragon", health=100, attack=30)]

    while player.is_alive():
        print("\n" + "=" * 20)
        print(f"Your HP: {player.health}")
        print("Monsters:")
        for i, monster in enumerate(monsters):
            print(f"{i + 1}. {monster.name} (HP: {monster.health})")

        choice = input("Choose a monster to attack (1-3) or press 'q' to quit: ")
        if choice == 'q':
            print("Thanks for playing! Your adventure ends here.")
            break

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(monsters):
                enemy = monsters[choice - 1]
                player.attack_enemy(enemy)

                if enemy.is_alive():
                    enemy.attack_enemy(player)
                    if not player.is_alive():
                        print(f"{player.name} has been defeated by {enemy.name}. Game over!")
                        break
                else:
                    print(f"{player.name} defeated {enemy.name}!")

                    # Remove defeated enemy from the list
                    monsters.remove(enemy)
            else:
                print("Invalid choice. Please choose a valid monster.")
        else:
            print("Invalid input. Please enter a number or 'q' to quit.")

    print("Game over!")

if __name__ == "__main__":
    main()
