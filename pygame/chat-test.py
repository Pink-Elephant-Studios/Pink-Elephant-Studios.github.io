import random

class Character:
    def __init__(self, name, health, attack, speed):
        self.name = name
        self.health = health
        self.inventory = []
        self.attack = attack
        self.speed = speed

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        return self.health > 0

    def attack_enemy(self, enemy):
        damage = random.randint(1, self.attack)
        enemy.take_damage(damage)
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")

    def set_speed(self):
        self.speed = random.randint(1, 10)

    def check_inventory(self):
        for item in self.inventory: 
            print(f"You have {item}")

def create_inventory(player):
    print("In your inventory currently is", player.inventory)

class Monster(Character):
    def __init__(self, name, health, attack, speed):
        super().__init__(name, health, attack, speed)
        self.inventory = ["air", "crumbs", "sword", "DECK OF MANY THINGS"]
        random_item = random.choice(self.inventory)
        print(random_item)

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def main():
    print("Welcome to this weird RPG Adventure!")
    player_name = input("Enter your character's dumb name: ")
    print("Now we are going to test to see if we can put something in the inventory, and list the inventory. Next step will be moving things from the monster's inventory to yours.")
    
    speed = random.randint(1, 10)
    turn = 0

    player = Character(player_name, health=100, attack=20, speed=speed)
    player.set_speed()
    print(f"Your character's speed is set to {speed}") 
    pause = input("Press enter to continue, young buck")
    
    create_inventory(player)  # Call the function after it's defined

    locations = [
        Location("Village", "You are in a peaceful village. You see minecraft Steve off in the distance."),
        Location("Forest", "You find yourself in a dense forest. A giant ape jumps onto your head yesterday."),
        Location("Cave", "A dark cave lies ahead. You have traveled back in time 20 million years and find a dinosaur standing on Elon Musk."),
    ]

    current_location = locations[1]  # Start in the forest

    monsters = [
        Monster("Goblin", health=30, attack=10, speed=7),
        Monster("Orc", health=50, attack=15, speed=3),
        Monster("Dragon", health=100, attack=30, speed=9)
    ]

    while player.is_alive():
        print("\n" + "=" * 20)
        print(f"Your HP: {player.health}")
        print(f"Current Location: {current_location.name}")
        print(current_location.description)
        
        print("Options:")
        print("1. Explore")
        print("2. Check Inventory")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '3':
            print("Thanks for playing! Your adventure ends here. (Why would you leave me :( )")
            break

        if choice == '1':
            if current_location.name == 'Village':
                player_choice = input("Do you want to go into the forest, young buck? y/n?")
                if player_choice.lower() == 'y':
                    current_location = locations[1]

            if current_location.name == "Forest":
                enemy = random.choice(monsters)
                print(f"You encountered a {enemy.name}!")
                while player.is_alive() and enemy.is_alive():
                    if turn == 0:
                        print(f"The enemy's speed is {enemy.speed}. Prepare to die!")
                        if speed > enemy.speed:
                            answer = input("Do you [r]un or [f]ight")
                            if answer.lower() == "r":
                                print("You chose to run.")
                            elif answer.lower() == "f":
                                print("You chose to fight.")
                                player.attack_enemy(enemy)
                            else:
                                print("Invalid choice. Please enter 'r' or 'run' to run, or 'f' or 'fight' to fight.")
                            turn += 1
                        else:
                            enemy.attack_enemy(player)
                            turn += 2
                    else:
                        if enemy.is_alive():
                            if (turn % 2) == 0:
                                answer = input("Do you [r]un or [f]ight")
                                if answer.lower() == "r":
                                    print("You chose to run.")
                                elif answer.lower() == "f":
                                    print("You chose to fight.")
                                    player.attack_enemy(enemy)
                                else:
                                    print("Invalid choice. Please enter 'r' or 'run' to run, or 'f' or 'fight' to fight.")
                            else:
                                enemy.attack_enemy(player)
                            turn += 1
                            pause = input("Press 'no' to run away, or any other key to continue.")
                            if pause.lower() == "no":
                                print(f"{player.name} runs away from {enemy.name}. You whimp.")
                                break
                            if not player.is_alive():
                                print(f"{player.name} has been defeated by {enemy.name}. You suck!")
                                break
                        else:
                            print(f"You defeated the {enemy.name}!")
                            for item in enemy.inventory:
                                print(f"You find {item}")
                            if not enemy.is_alive():
                                print(f"You loot the {enemy.name}'s corpse.")
                                print("You find a nice iron sword.")
                                try:
                                    player.inventory.append("nice iron sword")
                                    for item in player.inventory:
                                        print(f"You have a {item}")
                                except:
                                    print("Your code doesn't work, and you suck at programming")
        elif choice == '2':
            player.check_inventory()
        else:
            print("Invalid choice. Please choose a valid option, bro.")

    print("Game over!")

if __name__ == "__main__":
    main()
