import random
#yo next time, point buy system, keep track of turns so initiative is only checked at combat start, possibility to find new items to add to inventory whne you explore
# inventory system
## add axe to monster inventory
###bonus randomize weapon in inventory
##when enemy is defeated get axe from monster inventory
##append axe to player inventory as usual
#add function to enemy class to generate random item/inventory
def test():
    print ("we are trying to print the first item in the enemy's inventory list, which is", enemy.inventory[1])
class Character:
    def __init__(self, name, health, attack, speed):
        self.name = name
        self.health = health
        self.inventory = ["wispy string"]
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
        speed = random.randint(1, 10)

    def check_inventory(self):
        #inventory = []
        for i in self.inventory: 
            print ("you have", {i})

class Monster(Character):
    def __init__(self, name, health, attack, speed):
        super().__init__(name, health, attack, speed)
        enemy_inventory=["air", "crumbs", "sword", "DECK OF MANY THINGS"]
        random_item = random.choice(enemy_inventory)
        print(random_item)
class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description

def main():
    print("Welcome to this weird RPG Adventure!")
    player_name = input("Enter your character's dumb name: ")
    speed = random.randint(1,10)
    turn = 0
    player = Character(player_name, health=100, attack=20, speed=speed)
   # print("Your character's heath is set to " +player.health) 
  #  player.set_speed()
    print("Your character's speed is set to " ,{speed}) 
    pause = input("Press enter to continue, young buck")
    locations = [
        Location("Village", "You are in a peaceful village. You see minecraft Steve off in the distance."),
        Location("Forest", "You find yourself in a dense forest. A giant ape jumps onto your head yesterday."),
        Location("Cave", "A dark cave lies ahead. You have traveled back in time 20 million years and find a dinosaur standing on Elon Musk."),
    ]

    current_location = locations[1]  # Start in the forest

    monsters = [Monster("Goblin", health=30, attack=10, speed=7),
                Monster("Orc", health=50, attack=15, speed=3),
                Monster("Dragon", health=100, attack=30, speed=9)]

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
                player_choice = input("Do you want to go into the forest, young buck? y/n?")
                if player_choice == y:

                    current_location = locations[1]
            if current_location.name == "Forest":
                # Chance of encountering a monster in the forest
               # if random.random(0,.3) < 0.3:
                enemy = random.choice(monsters)
                print(f"You encountered a {enemy.name}!")
                while player.is_alive() and enemy.is_alive():
                    #beginning of um initiative if statement
                    if turn == 0:
                        #like this will happen the first time player encounters an enemy acutally. the first thing we will do is see who goes first, if the player goes frist they can choose to attack or run. the enemy always attacks. alright done NO dont type that
                        print(f"The enemy's speed is {enemy.speed}. Prepare to die! (Initiative has been rolled for you, you're welcome.)")
                        if speed > enemy.speed:
                            #give player choice to run or fight
                            answer = input("Do you and then do do you [r]un or [f]ight")
                            # Check the user's input using if statements
                            if answer == "r" or answer.lower() == "run":
                                print("You chose to run.")
                            elif answer == "f" or answer.lower() == "fight":
                                print("You chose to fight.")
                                player.attack_enemy(enemy)
                            else:
                                print("Invalid choice. Please enter 'r' or 'run' to run, or 'f' or 'fight' to fight.")
                            turn += 1
                        else:
                            enemy.attack_enemy(player)
                            turn += 2
                        #end of um intiative if statement
                    else:
                        if enemy.is_alive():
                            #Putting test code here
                            if (turn % 2)==0:
                                #print("CONGRATULATIONS! ITS YOUR TURN!")
                                #option to run or fight
                              #  if speed > enemy.speed:
                            #give player choice to run or fight
                                answer = input("Do you [r]un or [f]ight")
                                # Check the user's input using if statements
                                if answer == "r" or answer.lower() == "run":
                                    print("You chose to run.")
                                elif answer == "f" or answer.lower() == "fight":
                                    print("You chose to fight.")
                                    player.attack_enemy(enemy)
                                else:
                                    print("Invalid choice. Please enter 'r' or 'run' to run, or 'f' or 'fight' to fight.")
                            else:
                                enemy.attack_enemy(player)
                            turn += 1
                            pause = input("Bro you tryinna continue? Say no to run away, or any other key to continue bro.")
                            if pause == "no":
                                print(f"{player.name} runs away from {enemy.name}, you whimp.")
                                break
                            if not player.is_alive():
                                print(f"{player.name} has been defeated by {enemy.name}. You suck!")
                                break
                        else:
                            print(f"You defeated the {enemy.name}!")
                            for i in enemy.inventory: 
                                print ("you find", {i})
                if not enemy.is_alive():
                    print(f"You loot the {enemy.name}'s corpse.")
                    print(f"You find a nice iron sword.")
                    try:
                        player.inventory.append("nice iron sword")
                        for item in player.inventory:
                            print(f"You have a {item}")
                    except:
                        print(f"Your code doesn't work, and you suck at programming")
           #        Do the loot test here bc the player is alive but the enemy is not
            # use later:    print("You explore the area but find nothing of interest.")

        elif choice == '2':
            # Add inventory functionality here if desired
            player.check_inventory()        
        else:
            print("Invalid choice. Please choose a valid option, bro.")

    print("Game over!")

if __name__ == "__main__":
    main()
    test()