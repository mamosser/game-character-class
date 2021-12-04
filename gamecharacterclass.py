# Malia Mosser
# Assignment 10.1: Your Own Class
# This is a class that is modeled after a basic video game character.

# Implement the class.
class GameCharacter:
    def __init__(self, name, gender, model_size, weapon, element, experience):
        # Set the data variables.
        self.__name = name
        self.__gender = gender
        self.__model_size = model_size
        self.__weapon = weapon
        self.__element = element
        self.__experience = experience

    # Get-set methods. These will help us retrieve the data variables, since they are private and must be accessed this way.

    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_modelsize(self):
        return self.__model_size

    def set_modelsize(self, model_size):
        self.__model_size = model_size
    
    def get_weapon(self):
        return self.__weapon

    def set_weapon(self, weapon):
        self.__weapon = weapon
    
    def get_element(self):
        return self.__element

    def set_element(self, element):
        self.__element = element

    def get_experience(self):
        return int(self.__experience)

    def set_experience(self, experience):
        self.__experience = experience

    # This is a method that will tell you what level your character is based on how many experience points they have.
    def add_experience(self, more_exp):
        # Initialize the character's level.
        self.__level = 0
        # If the total number of experience and gained experience is less than 10, the character's level is at 1. 
        if self.__experience + more_exp < 10:
            self.__level = 1
            self.__experience = self.__experience + more_exp
            print(f"{self.__name} has gained {more_exp} exp. They now have {self.__experience} total exp. Their level is at {self.__level}.")
        # If the total number of experience and gained experience is in the range 10-20, the character's level is at 2.
        elif self.__experience + more_exp in range (10, 20):
            self.__level = 2
            self.__experience = self.__experience + more_exp
            print(f"{self.__name} has gained {more_exp} exp. They now have {self.__experience} total exp. Their level is at {self.__level}.")
        # If the total number of experience and gained experience is in the range 21-30, the character's level is at 3.
        elif self.__experience + more_exp in range (21, 30):
            self.__level = 3
            self.__experience = self.__experience + more_exp
            print(f"{self.__name} has gained {more_exp} exp. They now have {self.__experience} total exp. Their level is at {self.__level}.")
        # The current max level is 3. If the number of experience and gained experience is above, the level will not go up, but the experience points will.
        elif self.__experience > 30:
            self.__level = 3
            self.__experience = self.__experience + more_exp
            print(f"{self.__name} has gained {more_exp} exp. Their total exp of {self.__experience} is now beyond the max level of {self.__level}.")

    # This is a method that takes in user input and allows the person's character to switch their weapon if they want to.
    def switch_weapon(self, weapon):
        print(f"Your current weapon is a {self.__weapon}. Please enter 'yes' if you'd like to change it, and 'no' if you would not like to change it.")
        command = input(">>> ")
        if command == "yes":
            print("Choose a weapon: claymore, sword, polearm, bow, catalyst")
            command = input(">>> ")
            if command == "claymore":
                self.__weapon = "claymore"
                print("You have changed your weapon to a claymore.")
                print(f"Weapon equipped: {self.__weapon}")
            elif command == "sword":
                self.__weapon = "sword"
                print("You have changed your weapon to a sword.")
                print(f"Weapon equipped: {self.__weapon}")
            elif command == "polearm":
                self.__weapon = "polearm"
                print("You have changed your weapon to a polearm.")
                print(f"Weapon equipped: {self.__weapon}")
            elif command == "bow":
                self.__weapon = "bow"
                print("You have changed your weapon to a bow.")
                print(f"Weapon equipped: {self.__weapon}")
            elif command == "catalyst":
                self.__weapon = "catalyst"
                print("You have changed your weapon to a catalyst.")
                print(f"Weapon equipped: {self.__weapon}")
            else:
                print("Invalid command. Please enter claymore, sword, polearm, bow, or catalyst.")
        elif command == "no":
            print("No changes have been made.")
            print(f"Weapon equipped: {self.__weapon}")

    # This is a magic method that returns all of the character's info as a string.
    def __str__(self):
        return(f"Character Info: Name - {self.__name}, Gender - {self.__gender}, Model Size - {self.__model_size}, Weapon Type - {self.__weapon}, Element - {self.__element}, Experience - {self.__experience}.")

def main():
    character1 = GameCharacter("Amber", gender="female", model_size="short", weapon="bow", element="fire", experience=19)
    print(str(character1))
    print("\n")
    print(f"While you were away, your character {character1.get_name()} encountered a living, breathing, angry ice slime! Using their {character1.get_element()}-infused {character1.get_weapon()}, they defeated it.")
    print("\n")
    print(f"After {character1.get_name()} returned from battle: ")
    character1.add_experience(2)
    print("\n")
    character2 = GameCharacter("Kaeya", gender="male", model_size="tall", weapon="sword", element="ice", experience=31)
    print(str(character2))
    print("\n")
    print(f"Uh oh! {character2.get_name()} has encountered a dragon, but their {character2.get_weapon()} cannot reach it.")
    character2.switch_weapon("sword")
    print("\n")
    print(f"With their {character2.get_weapon()}, {character2.get_name()} was suddenly filled with renewed fervor and slayed the dragon!")
    print(f"After {character2.get_name()} returned from battle: ")
    character2.add_experience(10)

if __name__ == '__main__':
    main()

with open("README.txt", "w") as f:
    f.write("Description of the class: This is a class that is modeled after a general video game character. It contains different private variables that describe the character, including: name, gender, model size (height), weapon, element, and experience points. It contains multiple get-set methods, as well as two additional methods to add experience points to a character's total amoount of experience points as well as change the character's weapon.")
    f.write("\n")
    f.write("Description of the data variables:")
    f.write("\n")
    f.write("name: The name of the video game character.")
    f.write("gender: The gender identity of the video game character.")
    f.write("model_size: The size of the character's in-game model as a string. For example: short, tall.")
    f.write("weapon: The weapon that the character is currently using. Can consist of a claymore, sword, polearm, bow, or catalyst.")
    f.write("element: The element that the character uses. For example: fire, water, ice, earth, air.")
    f.write("experience: The amount of experience points that the character has. Experience points are gained when the character defeats an enemy.")
    f.write("\n")
    f.write("Description of the methods:")
    f.write("\n")
    f.write("add_experience: This is a method that will tell you how many experience points your character has gained, their total experience points, as well as their corresponding level based on their experience points. It should be called after the character defeats an enemy, since that is how you level up.")
    f.write("switch_weapon: This is a method that takes in user input and allows the user to switch their character's weapon if needed. It should prompt you to change your weapon when it is unusable against a certain enemy.")
    f.write("\n")
    f.write("Description of the demo program:")
    f.write("\n")
    f.write("The demo program showcases the info of two different characters with different values. It demonstrates a possible fight situation in which your first character defeats an enemy and gains experience points. It also demonstrates your second character encountering an enemy wherein their weapon cannot reach, so you are prompted to change your weapon. Overall, it shows how each character's attributes interact with their environment.")
    f.write("Demo program instructions:")
    f.write("\n")
    f.write("You may make up a character with any attributes you'd like or model the character after an existing one by replacing their name, gender, model size, weapon, element, and experience points. The program will prompt you to switch your weapon mid-battle. The outcome of the battle is the same no matter what weapon you choose. The demo program will also tell you what level your character is based on how many experience points you gave them in the beginning, and how many they gain from going into battle.")