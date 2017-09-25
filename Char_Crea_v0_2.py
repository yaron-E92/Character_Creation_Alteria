import skill_lists; # Importing skill_lists, so it will be executed and then usable

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
        self.skills = [];

    def raceup(self, updict):
        """This function changes the self.summary['Race'] from single letters to race names.
        The updict dictionary will have the translations"""
        self.summary['Race'] = updict[self.summary['Race']];

    def skillin(self):
        """Initialize all the skill whose ishidden is 0. Should be used after the choice of class when it will be
        implemented"""
        # We'll use skilladd on all types. Any skill with ishidden == 0 will be added to self.skills
        self.skilladd(skill_lists.Skills.Knowledge,0); # Starting with adding the skills in knowledge type
        self.skilladd(skill_lists.Skills.Arcane, 0); # Adding the skills in Arcane type
        self.skilladd(skill_lists.Skills.Physical, 0);  # Adding the skills in Physical type
        self.skilladd(skill_lists.Skills.Finesse, 0);  # Adding the skills in Finesse type
        self.skilladd(skill_lists.Skills.Social, 0);  # Adding the skills in Social type
        self.skilladd(skill_lists.Skills.Practical, 0);  # Adding the skills in Practical type

    def skilladd(self, stype, flag):
        """A function for adding a new skill to the self.skills list. It will either add all not hidden skills in stype
        (If it gets a 0 in flag) Or a specific skill (if it gets a 1 in flag).
        As of now, I haven't implemented the adding of single skills"""
        if(flag == 0):
            for i in range(len(stype.ishidden)):
                if (stype.ishidden[i] == 0):
                    name = stype.skills[i];
                    attribute = stype.relatt[i];
                    self.skills.append(Skill(attribute, name));



class Skill:
    '''A class containing The data about the skill of a character: The skill level, the proficiency growth, the
    associated attribute, multiplier (like major class multiplier, minor class multiplier, minor multiplier or hobby
    multiplier)'''

    def __init__(self, attribute, name):
        """The initialization prepares 5 variables. The skill lvl, the current xp in skill lvl, the proficiency growth,
        the associated attribute and the multiplier
        The initial proficiency growth will equal the level.
        The default multiplier will be 1. Added a 6th variable - name"""
        self.lvl = 0;
        self.xp = 0;
        self.progro = self.lvl;
        self.attribute = attribute;
        self.mulp = 1;
        self.name = name;

    def classup(self, updict):
        """This function changes the self.lvl from to the starting lvl associated with the class.
        The updict dictionary will have the translations"""
        self.lvl = 0; # Not yet implemented
        self.progro = self.lvl;

    def lvlup(self):
        """This simply level ups the skill level, and if the prof. growth equals the lvl it goes up too"""
        if (self.progro == self.lvl):
            self.progro += 1;
        self.lvl += 1;

    def xpup(self, amount):
        """This adds the specified amount to the xp. If the xp hits 100, then it lvl ups the skill and adds any residual
        xp to the next lvl. In the future, it might morph the residual xp"""
        if ( (self.xp + amount) < 100):
            self.xp += amount; # If the amount doesn't push the xp over 100, then it is just added.
        else:
            self.xp = (self.xp + amount) - 100; # If it flows beyond, the remainder is saved for next lvl and...
            self.lvlup(); # The skill is lvld up.



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
# print(skill_lists.arcane_type.relatt); # TEST
# print(skill_lists.Skills.Knowledge.ishidden); # TEST
# print(len(skill_lists.Skills.Knowledge.ishidden)); # TEST
character.skillin(); #Activating the skill initialization. It is incomplete as of now
# TEST
# for i in range(len(character.skills)):
#     print(character.skills[i].name);  # TEST
# TEST


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
# 22.9.2017, 00:39 - Added the class 'Skill', which has its 5 variables (lvl,xp,profgro,attribute and multiplier)
# Implemented an init, a lvl up function for the skill which also make sure that profgro is at least as high as the lvl
# Implemented an xpup function that gets the amount to add and levels up the skill if goes to 100 or beyond, and any
# residual gets transferred to next lvl. Also, prepared a function classup which wasn't really implemented as of now.
# In a future update the dummy function will be implemented.
# 25.9.2017, 21:13 - added the Skills variable to the Character class, which is a list to be filled with Skill class
# objects.
# 21:17 - Imported skill_lists!
# 21:23 - Added a 6th variable to the Skill class - name
# between 21:00 and 21:49 - Added the skillin function to the Character class, to initialize the skills variable. At the
# future, it will activate after the class choice, and will have the relevant skills
# 21:52 - Added skilladd tothe Character class, a function for adding a new skill to the self.skills list.
# 21:57 - skilladd has two modes - either adding all non hidden skills in a type (for skillin) or a specific skill.
# As of now, I haven't implemented the adding of single skills
# 22:02 - used the skilladd in skillin, and now it adds all not hidden skills to the Character.skills, at level 0.
# Next on the agenda: classes. I think

# NEED TO ADD LATER:
# Writing a character to a file,
# Adding another Program which can read a character from a file
# Adding a program which the other program can use, containing all sort of functions,
# like getting a character's stats, changing them etc.



