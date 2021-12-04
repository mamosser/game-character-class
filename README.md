# game-character-class
This program contains a class which is modeled after a general video game character.

Description of the class: This is a class that is modeled after a general video game character. It contains different private variables that describe the character, including: name, gender, model size (height), weapon, element, and experience points. It contains multiple get-set methods, as well as two additional methods to add experience points to a character's total amoount of experience points as well as change the character's weapon.

Description of the data variables:
name: The name of the video game character.
gender: The gender identity of the video game character.
model_size: The size of the character's in-game model as a string. For example: short, tall.
weapon: The weapon that the character is currently using. Can consist of a claymore, sword, polearm, bow, or catalyst.
element: The element that the character uses. For example: fire, water, ice, earth, air.
experience: The amount of experience points that the character has. Experience points are gained when the character defeats an enemy.

Description of the methods:
add_experience: This is a method that will tell you how many experience points your character has gained, their total experience points, as well as their corresponding level based on their experience points. It should be called after the character defeats an enemy, since that is how you level up.
switch_weapon: This is a method that takes in user input and allows the user to switch their character's weapon if needed. It should prompt you to change your weapon when it is unusable against a certain enemy.

Description of the demo program:
The demo program showcases the info of two different characters with different values. It demonstrates a possible fight situation in which your first character defeats an enemy and gains experience points. It also demonstrates your second character encountering an enemy wherein their weapon cannot reach, so you are prompted to change your weapon. Overall, it shows how each character's attributes interact with their environment.

Demo program instructions:
You may make up a character with any attributes you'd like or model the character after an existing one by replacing their name, gender, model size, weapon, element, and experience points. The program will prompt you to switch your weapon mid-battle. The outcome of the battle is the same no matter what weapon you choose. The demo program will also tell you what level your character is based on how many experience points you gave them in the beginning, and how many they gain from going into battle.
