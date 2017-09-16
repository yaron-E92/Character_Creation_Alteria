def insert_dat(legal,index,message):
    """This function receives a list of legal inputs,
     ,the index in character in which to input the data
     and the message to give the user as long as he/she is not finished.
     The function prompts the user for input and will continue so
     if the input is not in legal. If it is, the function will still
     give the user the opportunity to change the input"""

    flag = '0';  # A flag for the while loop
    while (flag == '0'):
        print(message);  # Prompting the user to choose a race using the letters in brackets
        character.summary[index] = input();  # Getting input
        # Using the "not in" operation and the pre-prepared list to check whether the input is legal.
        if (character.summary[index] not in legal):
            flag = '0';  # If the input is illegal continue in the loop (This line is a precaution)
            print("Illegal input. Try again")
        else:
            print("Do you want to change your mind? If so, enter (Y)");
            flagi = input();  # A flag to check if the user changed his/her mind
            if (flagi == 'y' or flagi == 'Y'):
                flag = '0';  # Again, Just in case
            else:
                flag = '1';

class Character:
    '''A class containing the data about a character. Both the old data,
    the name, race, soc and eco, and the attributes'''

    def __init__(self, summary, attributes):
        """The initialization prepares 2 'dictionary' variables"""
        self.summary = summary;
        self.attributes = attributes;

    def raceup(self, updict):
        """This function changes the self.summary['Race'] from single letters to race names.
        The updict dictionary will have the translations"""
        self.summary['Race'] = updict[self.summary['Race']];



def ratt(mister):
    """Applying the race related benefits and drawbacks to the attributes.
    Accepting a Character class variable (mister).
    :type mister: Character"""
    #  b&d == benefits and drawbacks
    stre = {"Human": 0, "Basil": 3, "Dwarf": 2, "Elf": 0, "Gnome": 0, "CP": 0}; #The strength b&d
    dex = {"Human": 0, "Basil": -2, "Dwarf": -1, "Elf": 2, "Gnome": 0, "CP": 0};  # The dexterity b&d
    cha = {"Human": 0, "Basil": 0, "Dwarf": 0, "Elf": 1, "Gnome": 0, "CP": 0};  # The charisma b&d
    int = {"Human": 0, "Basil": 1, "Dwarf": 1, "Elf": 2, "Gnome": 2, "CP": 0};  # The intelligence b&d
    wis = {"Human": 0, "Basil": 0, "Dwarf": 0, "Elf": 2, "Gnome": 2, "CP": 0};  # The wisdom b&d
    end = {"Human": 0, "Basil": 3, "Dwarf": 3, "Elf": -2, "Gnome": 1, "CP": 0};  # The endurance b&d
    attri1=(stre, dex, cha, int, wis, end); # A tuple for the above dictionaries
    attri2 = ('Str', 'Dex', 'Cha', 'Int', 'Wis', 'End'); # A tuple for the keys of the Character.attributes
    # Now, a for loop to update all the attributes. The loop will run over the values of attri2 and will use them to
    # update the Character.attributes[attri2[i]] with the values in attri1[i]
    for i in range(len(attri2)):
        mister.attributes[attri2[i]] += attri1[i][mister.summary['Race']]; # Hopefully updating properly



# Preparing the attributes 'dictionary' for the character initialization
attr = {'Str': 8, 'Dex': 8, 'Cha': 8, 'Int': 8, 'Wis': 8, 'End': 8}; # The attributes start at 8
# The character contains a name, race,
# The "social" general status of the character
# and The economical if the character is urban or rural
# (Noble and Tribal are assigned automatically).
# In addition it contains the attributes.
character = Character({'Name': 0, 'Race': '0', 'Soc': '0', 'Eco': '0'}, attr);

print("Choose Your name (maximum 24 characters)");
character.summary['Name'] = input(); # Getting the name from the user
print("The character's name is:", character.summary['Name']); # TEST printing the name
# print("Hello {name}. How are you".format(name=character.summary['Name'])); # TEST printing the name

# Prompting the user to choose his race
print("Choose Your race amongst the following:");
legal = ['H', 'h', 'E', 'e', 'D', 'd', 'G', 'g', 'B', 'b', 'C', 'c']; # Creating a list of legal input for the races so
# that it can easily be checked whether the input is legal.
# Will keep asking the user for a race as long as he didn't put a legal input. Using the insert_dat function.
insert_dat(legal,'Race',"(H)uman, (E)lf, (D)warf, (G)nome, (B)asil, (C)P");
rup = {'H': "Human", 'h': "Human", 'E': "Elf", 'e': "Elf", 'D': "Dwarf", 'd': "Dwarf", 'G': "Gnome", 'g': "Gnome",
       'B': "Basil", 'b': "Basil", 'C': "CP", 'c': "CP"}; # Preparing the updating dictionary for race
character.raceup(rup); # Updating the race from a single letter to a word
print("The character's race is:", character.summary['Race']); # TEST printing the characer's race
legal = ['N','n','U','u','R','r','T','t']; # Creating a list of legal input for soc so that it can easily be checked
# whether the input is legal.
print("Choose Your background amongst the following:");
# Prompting the user to choose a soc using the letters in brackets.
# The list of legal inputs has changed.
insert_dat(legal,'Soc',"(N)oble, (U)rban, (R)ural, (T)ribal (or from a small community)");
print("The character's soc is:", character.summary['Soc']); # TEST printing the characer's soc
if (character.summary['Soc'] == 'N' or character.summary['Soc'] == 'n'):
    character.summary['Eco'] = 'h'; # Giving Noble characters the "higher class" economical status
    print("Nobles are automatically rich (at least for now)");
elif (character.summary['Soc'] == 'T' or character.summary['Soc'] == 't'):
    character.summary['Eco'] = 'l'; # Giving Tribal characters the "lower class" economical status
    print("Tribals are automatically from the lower economical class");
else:
    legal = ['H', 'h', 'M', 'm', 'L', 'l', 'S', 's'];  # Creating a list of legal input for eco so that it can easily be
    #  checked whether the input is legal.
    print("Choose Your background amongst the following:");
    # Prompting the user to choose a eco IF he chose urban or rural using the letters in brackets.
    # The list of legal inputs has changed
    insert_dat(legal, 'Eco', "(H)igher class, (M)iddle class, (L)ower class, (S)treet urchin");
print("The character's eco is:", character.summary['Eco']);  # TEST printing the characer's eco
print("The character's endurance is:", character.attributes['End']);  # TEST printing the characer's endurance before ratt
ratt(character); # Using the ratt function to apply race dependant b&d (benefits and drawbacks) to the starting attributes
print("The character's endurance is:", character.attributes['End']);  # TEST printing the characer's endurance after ratt

# Update log:
# 15.9.2017, 18:01 - Changed "character" from a list to a dictionary.
# and added extra "padding" to the messages showing the chosen input.
# 18:05 - Fixed something that I just noticed. Added 'c' to the legal list of race input.
# 22:10 - NEW IN V0.2 - Decided to create a 'class' for character, so that it will have the current data and a seperate
# dictionary for attributes.
# 22:42 - Created a new Instance variable in the 'Character' class: a dictionary of attributes.
# 16.9.2017, 13:46 - Created the ratt function for later implementation (will add race related bonuses and drawbacks to
# starting attributes), and implemented a function for converting race from single letters to words. IT WORKS!
# 14:36 - Changing the location of the race update to right after the race input.
# 17:43 - First implementation attempt of ratt function - a function that is supposed to apply race dependant
# b&d (benefits and drawbacks) to the starting attributes. It works!

# NEED TO ADD LATER:
# Writing a character to a file,
# Adding another Program which can read a character from a file
# Adding a program which the other program can use, containing all sort of functions,
# like getting a character's stats, changing them etc.



