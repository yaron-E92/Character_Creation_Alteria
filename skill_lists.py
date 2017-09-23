class Skill_list:
    '''A class that will contain all the skills. Maybe there is no need for a class for that, but for now I will define
    one anyway. I will see if I will change it. It will contain a list of all skills divided to the types'''

    def __init__(self, knowledge, arcane, physical, finesse, social, practical):
        """Nothing fancy here. Just initializing The skill types are Knowledge, Arcane, Physical, Finesse, Social and
        Practical"""
        self.Knowledge = knowledge;
        self.Arcane = arcane;
        self.Physical = physical;
        self.Finesse = finesse;
        self.Social = social;
        self.Practical = practical;


class Skill_type_list:
    '''A class which has the list of all skills pertaining to a specific type. The second list will
    contain the related attributes for each skill, and the third will contain the over skill index (or 0 if there is
    none). There is a fourth list of 0 or 1 or 2 to see if the skill is hidden by default, where 1 is hidden except for
    level up, and 2 is hidden completely'''

    def __init__(self,skills):
        """Initializing the four lists."""
        self.skills = skills;
        self.relatt = [];
        self.upskill = [];
        self.ishidden = [];

    def ifarc(self, conlist):
        """If it is the arcane type, define a separate list for connection to the sources"""
        self.conn = conlist;



# defining the 6 lists which will go into the 3 skill_type_list
knolist = ["Arcana", "History(general)", "History(specific countries)", "History(specific races)", "Nature",
           "Sociology(general)", "Sociology(knowledge about specific cultures)", "Theology and religion(general)",
           "Theology and religion(specific religions)"];
arlist = [];
phylist = [];
filist = ["Acrobatics", "Investigation", "Lockpicking", "Perception", "Sleight of hand", "Stealth", "Survival"];
solist = ["Deception", "Insight", "Intimidation", "Performance", "Persuasion", "Streetwise"];
pralist = [];
# And defining the connection to the sources list
conlist = ["Astronomical bodies", "Elemental", "Higher beings", "Light", "Magic field", "Nature", "Planet", "Soul",
           "Void"];





# 22.9.2017 - after 17:05: Created the file. Created a prelimiary class Skill_list:.
# Created a prelimiary def listing(name): which will probably be replaced
# Between 21:30 and 21:42? - Created a new class Skill_type_list:
# 23.9.2017 - 10:02: Finally had a breakthrough. In the new class from yesterday night, I created two new variables.
# And I've decided all variables here will be lists. The first list will contain the skill names, the second list will
# contain the related attributes for each skill, and the third will contain the over skill index (or 0 if there is
# none). There is a fourth list of 0 or 1 or 2 to see if the skill is hidden by default, where 1 is hidden except for
# level up, and 2 is hidden completely. Created 3 of the 6 list and the extra connection to the sources list. Added a
# function to the skill_type_list that adds the connection list if the type is arcane.

