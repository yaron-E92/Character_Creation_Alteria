import skill_lists; # Importing skill_lists, so it will be executed and then usable

class Char_class:
    '''A class that will contain the character classes'''

    def __init__(self, claskills, name):
        """Will contain the Claskills dictionary, which will contain all class skills with their values. Added name
        and will call the Char_class variable with the same name for compatability"""
        self.Claskills = claskills;
        self.Name = name;

def insert_dat(legal, message):
    """This function receives a list of legal inputs
     and the message to give the user as long as he/she is not finished.
     The function prompts the user for input and will continue so
     if the input is not in legal. If it is, the function will still
     give the user the opportunity to change the input"""

    flag = '0';  # A flag for the while loop
    cflagt = None; # So that the warning about "bla bla might be returned before assignment" will stop. And maybe it is
    # good practice in general
    while (flag == '0'):
        print(message);  # Prompting the user to choose a class using the letters in brackets
        cflagt = input();  # Getting input
        # Using the "not in" operation and the pre-prepared list to check whether the input is legal.
        if (cflagt not in legal):
            flag = '0';  # If the input is illegal continue in the loop (This line is a precaution)
            print("Illegal input. Try again")
        else:
            print("Do you want to change your mind? If so, enter (Y)");
            flagi = input();  # A flag to check if the user changed his/her mind
            if (flagi == 'y' or flagi == 'Y'):
                flag = '0';  # Again, Just in case
            else:
                flag = '1';
    return cflagt; # After the user inserted a final legal input, it is returned.

# Changed the input from a print(message) and input() to an insert_dat.
legal = ["druid", "cleric", "fighter"]; # Preparing the "legal" list for the classes.
cflag = insert_dat(legal, "Choose Your class (all lower case)"); # Getting the name of the class from the user.
# Using insert_dat
if (cflag == "druid"):
    # Changed the input from a print(message) and input() to an insert_dat.
    legal = ["empath", "wild", "power"];  # Preparing the "legal" list for the subclasses.
    cflag = insert_dat(legal, "Choose Your subclass between empath, power and wild (all lower case)");
    # Getting the name of the subclass from the user.
    # Using insert_dat
    # Creating the dictionary for the basic Druid
    Charclass = Char_class({skill_lists.Skills.Arcane.conn[4]: 3, skill_lists.Skills.Arcane.conn[5]: 3,
                    skill_lists.Skills.Arcane.conn[7]: 1, skill_lists.Skills.Arcane.skills[7]: 35,
                    skill_lists.Skills.Arcane.skills[2]: 25, skill_lists.Skills.Arcane.skills[8]: 20,
                    skill_lists.Skills.Arcane.skills[9]: 20, skill_lists.Skills.Physical.skills[12]: 15,
                    skill_lists.Skills.Knowledge.skills[4]: 25, skill_lists.Skills.Finesse.skills[6]: 25}, "Druid");
    # Updating the dictionary according to subclass
    if (cflag == "empath"):
        Charclass.Claskills.update({skill_lists.Skills.Arcane.skills[5]: 25, skill_lists.Skills.Practical.skills[2]: 25});
    elif (cflag == "wild"):
        Charclass.Claskills.update({skill_lists.Skills.Arcane.skills[11]: 25, skill_lists.Skills.Physical.skills[3]: 25});
    elif (cflag == "power"):
        Charclass.Claskills[skill_lists.Skills.Arcane.skills[2]] += 10;
elif (cflag == "cleric"):
    # Creating the dictionary for the basic Cleric
    Charclass = Char_class({skill_lists.Skills.Arcane.conn[4]: 3, skill_lists.Skills.Arcane.conn[3]: 3,
                        skill_lists.Skills.Arcane.conn[7]: 1, skill_lists.Skills.Arcane.skills[7]: 35,
                        skill_lists.Skills.Arcane.skills[8]: 20, skill_lists.Skills.Arcane.skills[6]: 20,
                        skill_lists.Skills.Arcane.skills[9]: 20, skill_lists.Skills.Arcane.skills[5]: 25,
                        skill_lists.Skills.Physical.skills[12]: 15,
                        skill_lists.Skills.Knowledge.skills[8]: 25, skill_lists.Skills.Knowledge.skills[7]: 15,
                         skill_lists.Skills.Social.skills[1]: 20, skill_lists.Skills.Social.skills[4]: 20}, "Cleric");
elif (cflag == "fighter"):
    # Creating the dictionary for the basic Fighter
    Charclass = Char_class({skill_lists.Skills.Physical.skills[3]: 40, skill_lists.Skills.Physical.skills[8]: 25,
                            skill_lists.Skills.Physical.skills[9]: 25, skill_lists.Skills.Physical.skills[0]: 20,
                            skill_lists.Skills.Social.skills[2]: 15}, "Fighter");
    # Choosing the main weapon proficiency
    legal = ["O", "T", "R"];  # Preparing the "legal" list for the subclasses.
    cflag = insert_dat(legal, "Choose Your main weapon proficiency between (O)ne handed & shield, (T)wo handed and "
                              "(R)anged");
    # Updating the dictionary according to subclass
    if (cflag == "O"):
        Charclass.Claskills.update({skill_lists.Skills.Physical.skills[5]: 30,
                                    skill_lists.Skills.Physical.skills[7]: 30});
    elif (cflag == "T"):
        Charclass.Claskills.update({skill_lists.Skills.Physical.skills[10]: 30});
    elif (cflag == "R"):
        Charclass.Claskills.update({skill_lists.Skills.Physical.skills[6]: 30});

print(Charclass.Claskills); # TEST






# 25.9.2017, 21:06 approx. - Created the file and the class Char_class with a dummy __init__ for now.
# 23:30 - imported skill_lists
# by 23:49 - created most of the dictionary for druid. But then had a problem. The  druid has 3 sub classes. What to do?
# by 23:57 - I found a solution. Ask the user in this file to choose class, and only this class will be created, by use
# of a dictionary and a flag variable. Theflag will be a 2 digit number, with one being the class and the other the
# subclass or 0 if no subclasses.
# 26.9.2017 00:01 - changed my mind. there will be a flag for class and if necessary another prompt for subclass.
# 00:21 - implemented druid class and the 3 subclasses, using an if for the class, and then another prompt for subclass
# and if and 2 elif for updating the dictionary accordingly
# 00:28 - seems to be working for the druid class. will need to implement more though.
# 28.9.2017, 14:32 - Have changed the input for the class choice to use a slightly altered version of the "insert_dat"
# function I have created for Char_Crea. Implemented bu 14:39. Now to do that for the Druid's subclasses.
# Aaaaaaand implemented as well by 14:42. Now it is time to start the process of implementing the other classes,
# but not right now.
# 18:04 - Implemented the Cleric's Dictionary
# 18:13 - Added name to Char_class and will call the Char_class variable with the same name for compatability. Changed
# the name of the variables to Charclass and added the names "Druid" and "Cleric in the right places.
# 18:30 - Implemented the basic Fighter skills and the main weapon proficiency. Remains: Secondary weapon proficiency,
# Armor type and whether he is a nature, medic or urban subclass
