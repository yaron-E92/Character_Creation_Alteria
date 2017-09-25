import skill_lists; # Importing skill_lists, so it will be executed and then usable

class Char_class:
    '''A class that will contain the character classes'''

    def __init__(self, claskills):
        """Will contain the Claskills dictionary, which will contain all class skills with their values"""
        self.Claskills = claskills;


print("Choose Your class (all lower case)");
cflag = input(); # Getting the name of the class from the user
if (cflag == "druid"):
    print("Choose Your subclass between empath, power and wild (all lower case)");
    cflag = input();  # Getting the name of the subclass from the user
    # Creating the dictionary for the basic Druid
    Druid = Char_class({skill_lists.Skills.Arcane.conn[4]: 3, skill_lists.Skills.Arcane.conn[5]: 3,
                    skill_lists.Skills.Arcane.conn[7]: 1, skill_lists.Skills.Arcane.skills[7]: 35,
                    skill_lists.Skills.Arcane.skills[2]: 25, skill_lists.Skills.Arcane.skills[8]: 20,
                    skill_lists.Skills.Arcane.skills[9]: 20, skill_lists.Skills.Physical.skills[12]: 15,
                    skill_lists.Skills.Knowledge.skills[4]: 25, skill_lists.Skills.Finesse.skills[6]: 25});
    # Updating the dictionary according to subclass
    if (cflag == "empath"):
        Druid.Claskills.update({skill_lists.Skills.Arcane.skills[5]: 25, skill_lists.Skills.Practical.skills[2]: 25});
    elif (cflag == "wild"):
        Druid.Claskills.update({skill_lists.Skills.Arcane.skills[11]: 25, skill_lists.Skills.Physical.skills[3]: 25});
    elif (cflag == "power"):
        Druid.Claskills[skill_lists.Skills.Arcane.skills[2]] += 10;
# print(Druid.Claskills); # TEST






# 25.9.2017, 21:06 approx. - Created the file and the class Char_class with a dummy __init__ for now.
# 23:30 - imported skill_lists
# by 23:49 - created most of the dictionary for druid. But then had a problem. The  druid has 3 sub classes. What to do?
# by 23:57 - I found a solution. Ask the user in this file to choose class, and only this class will be created, by use
# of a dictionary and a flag variable. Theflag will be a 2 digit number, with one being the class and the other the
# subclass or 0 if no subclasses.
# 26.9.2017 00:01 - changed my mind. there will be a flag for class and if necessary another prompt for subclass.
# 00:21 - implemented druid class and the 3 subclasses, using an if for the class, and then another prompt for subclass
# and if and 2 elif for updating the dictionary accordingly
# 00:28 - seems to be working for the druid class. will need to implement more though
