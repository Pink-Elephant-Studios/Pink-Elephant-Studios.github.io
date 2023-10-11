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

    def check_inventory(self, inventory):
        inventory = [string, shield, candle, FOOD, sword]
        for i in inventory: 
            print ("you have a", {i})

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
        Location("Village", "You are in a peaceful village. You see minecraft Steve off in the distance."),
        Location("Forest", "You find yourself in a dense forest. A giant ape jumps onto your head yesterday."),
        Location("Cave", "A dark cave lies ahead. You have traveled back in time 20 million years and find a dinosaur standing on Elon Musk."),
    ]

    current_location = locations[1]  # Start in the forest

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
            print("Thanks for playing! Your adventure ends here. (Why would you leave me :( )")
            break

        if choice == '1':
            # Explore the location
            if current_location.name == 'Villiage':
                player_choice = input("do you want to go into the forest, young buck? y/n?")
                if player_choice == y:

                    current_location = locations[1]
            if current_location.name == "Forest":
                # Chance of encountering a monster in the forest
               # if random.random(0,.3) < 0.3:
                enemy = random.choice(monsters)
                print(f"You encountered a {enemy.name}!")
                while player.is_alive() and enemy.is_alive():
                    player.attack_enemy(enemy)
                    if enemy.is_alive():
                        enemy.attack_enemy(player)
                        pause = input("bro you trying to continue?")
                        if pause == "no":
                            print(f"{player.name} runs away from {enemy.name}")
                            break
                        if not player.is_alive():
                            print(f"{player.name} has been defeated by {enemy.name}. Game over! You suck!")
                            break
                    else:
                        print(f"You defeated the {enemy.name}!")
              #  else:
           #         print("You explore the forest but find nothing of interest.")
            else:
                print("You explore the area but find nothing of interest.")

        elif choice == '2':
            # Add inventory functionality here if desired
            player.check_inventory()        
        else:
            print("Invalid choice. Please choose a valid option, bozo.")

    print("Game over!")

if __name__ == "__main__":
    main()