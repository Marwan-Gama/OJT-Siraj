import random

class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.health = 100
        self.score = 0


class Location:
    def __init__(self, name, description, challenges):
        self.name = name
        self.description = description
        self.challenges = challenges

class Game:
    def __init__(self):
        self.character = None
        self.locations = [
            Location("Forest", "A dense forest with mysterious creatures.", ["Goblin", "Wolf"]),
            Location("Castle", "An ancient castle with hidden treasures.", ["Dragon", "Ghost"]),
            Location("Cave", "A dark cave filled with valuable minerals.", ["Bat", "Spider"])
        ]

    def create_character(self):
        name = input("Enter your character's name: ")
        character_class = input("Choose your character class (Warrior/Mage/Rogue): ")
        self.character = Character(name, character_class)
        print(f"Character created: {name} - {character_class}")

    def explore_location(self, location):
        print(f"You are in the {location.name}. {location.description}")

        for challenge in location.challenges:
            self.encounter_creature(challenge)

    def encounter_creature(self, creature):
        print(f"An aggressive {creature} appears!")
        action = input("Do you want to (A)ttack or (R)un? ").upper()

        if action == "A":
            self.attack_creature(creature)
        elif action == "R":
            print("You successfully ran away.")
        else:
            print("Invalid choice. The creature attacks you!")

    def attack_creature(self, creature):
        damage = random.randint(1, 20)
        print(f"You attack the {creature} and deal {damage} damage.")
        print(f"The {creature} retaliates with a counter-attack.")
        self.character.health -= damage
        self.character.score += 20 - damage


    def display_score(self):
        print(f"Score: {self.character.score}")
        if self.character.score > 50:
            print("You Win!")
        else:
            print("You Lose!")


    def play(self):
        self.create_character()

        for location in self.locations:
            self.explore_location(location)

        self.display_score()


if __name__ == "__main__":
    game = Game()
    game.play()
