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

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def main():
    print("Welcome to the RPG Adventure!")
    player_name = input("Enter your character's name: ")
    player = Character(player_name, health=100, attack=20)

    locations = [
        Location("Village", "You are in a peaceful village."),
        Location("Forest", "You find yourself in a dense forest."),
        Location("Cave", "A dark cave lies ahead."),
    ]

    current_location = locations[0]  # Start in the village

    monsters = [Monster("Goblin", health=30, attack=10),
                Monster("Orc", health=50, attack=15),
                Monster("Dragon", health=100, attack=30)]

    while player.is_alive():
        print("\n" + "=" * 20)
        print(f"Your HP: {player.health}")
        print(f"Current Location: {current_location.name}")
        print(current_location.description)
        
        # Explore options
        print("Options:")
        print("1. Explore")
        print("2. Check Inventory")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '3':
            print("Thanks for playing! Your adventure ends here.")
            break

        if choice == '1':
            # Explore the location
            if current_location.name == "Forest":
                # Chance of encountering a monster in the forest
                if random.random() < 0.3:
                    enemy = random.choice(monsters)
                    print(f"You encountered a {enemy.name}!")
                    while player.is_alive() and enemy.is_alive():
                        player.attack_enemy(enemy)
                        if enemy.is_alive():
                            enemy.attack_enemy(player)
                            if not player.is_alive():
                                print(f"{player.name} has been defeated by {enemy.name}. Game over!")
                                break
                        else:
                            print(f"You defeated the {enemy.name}!")
                else:
                    print("You explore the forest but find nothing of interest.")
            else:
                print("You explore the area but find nothing of interest.")

        elif choice == '2':
            # Add inventory functionality here if desired
            print("Inventory feature not implemented yet.")
        
        else:
            print("Invalid choice. Please choose a valid option.")

    print("Game over!")

if __name__ == "__main__":
    main()
