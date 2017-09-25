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
    contain the related attributes for each skill, and the third will contain the over skill index (or -1 if there is
    none). There is a fourth list of 0 or 1 or 2 to see if the skill is hidden by default, where 1 is hidden except for
    level up, and 2 is hidden completely'''

    def __init__(self,skills):
        """Initializing the four lists. And because apparently it is customary to initialize everything in __init__
        I added the conn. And later the connhidden"""
        self.skills = skills;
        self.relatt = [];
        self.upskill = [];
        self.ishidden = [];
        self.conn = None;
        self.connhidden = None;

    def ifarc(self, clist):
        """If it is the arcane type, define a separate list for connection to the sources. And a list for which is
        hidden"""
        self.conn = clist;
        self.connhidden = [2, 2, 2, 2, 1, 2, 2, 2, 2];

    def updef(self, uplist):
        """Defining the upskill list"""
        self.upskill = uplist;

    def uphid(self,uplist):
        """Defining the ishidden list"""
        self.ishidden = uplist;

    def uprel(self, uplist):
        """Defining the relatt list"""
        self.relatt = uplist;


# defining the 6 lists which will go into the 3 skill_type_list
knolist = ["Arcana", "History(general)", "History(specific countries)", "History(specific races)", "Nature(knowledge)",
           "Sociology(general)", "Sociology(knowledge about specific cultures)", "Theology and religion(general)",
           "Theology and religion(specific religions)"];
arlist = ["Air magic", "Dark magic", "Earth magic", "Electricity magic", "Fire magic", "Healing magic", "Light magic",
          "Magical power", "Mana allocation", "Mana regeneration", "Necromancy", "Shapeshifting", "Telekinesis",
          "Telepathy", "Water magic", "Warging", "Weather magic"];
phylist = ["Athletics", "Heavy", "Light", "Martial prowess", "Medium", "One handed", "Ranged", "Shield",
           "Stamina allocation", "Stamina regeneration", "Two handed", "Unarmed", "Unarmored"];
filist = ["Acrobatics", "Investigation", "Lockpicking", "Perception", "Sleight of hand", "Stealth", "Survival"];
solist = ["Deception", "Insight", "Intimidation", "Performance", "Persuasion", "Streetwise"];
pralist = ["Crafting skills", "Dance", "Medicine", "Music", "Profession skills"];
# And defining the connection to the sources list
conlist = ["Astronomical bodies", "Elemental", "Higher beings", "Light", "Magic field", "Nature", "Planet", "Soul",
           "Void"];
# Now to create the type lists
knowledge_type = Skill_type_list(knolist);
arcane_type = Skill_type_list(arlist);
# Let's not forget to add the conlist
arcane_type.ifarc(conlist);
physical_type = Skill_type_list(phylist);
finesse_type = Skill_type_list(filist);
social_type = Skill_type_list(solist);
practical_type = Skill_type_list(pralist);
# Now, to define the over skills lists
knowledge_type.updef([-1, -1, 1, 1, -1, -1, 5, -1, 7]);
# TEST
# print(knowledge_type.skills);
# print(knowledge_type.upskill);
# for i in range(0, 9):
#     if (knowledge_type.upskill[i] != -1):
#         print("The over skill of", knowledge_type.skills[i], "is", knowledge_type.skills[knowledge_type.upskill[i]]);
# TEST
arcane_type.updef([-1] * len(arcane_type.skills));
# TEST
# print(arcane_type.upskill);
# print(len(arcane_type.skills));
# print(len(arcane_type.upskill));
# TEST

physical_type.updef([-1, -1, -1, -1, -1, 3, 3, 3, -1, -1, 3, 3, -1]);
# TEST
# print(physical_type.skills);
# print(physical_type.upskill);
# for i in range(0, len(physical_type.upskill)):
#     if (physical_type.upskill[i] != -1):
#         print("The over skill of", physical_type.skills[i], "is", physical_type.skills[physical_type.upskill[i]]);
# TEST
finesse_type.updef([-1] * len(finesse_type.skills));
social_type.updef([-1] * len(social_type.skills));
practical_type.updef([-1] * len(practical_type.skills));
# Now: the ishidden
knowledge_type.uphid([0, 0, 1, 1, 0, 0, 1, 0, 1]);
arcane_type.uphid([2, 2, 2, 2, 2, 2, 2, 0, 1, 0, 2, 2, 2, 2, 2, 2, 2]);
physical_type.uphid([0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0]);
finesse_type.uphid([0, 1, 2, 0, 1, 1, 0]);
social_type.uphid([0, 0, 0, 2, 0, 0]);
practical_type.uphid([2, 2, 0, 2, 2]);
attu = ['Str', 'Dex', 'Cha', 'Int', 'Wis', 'End']; # Attributes list for convenience
# Now: the relatt. Not sure about some of them. Like some of the armor skill, and the music skill.
knowledge_type.uprel([attu[3]] * len(knowledge_type.skills));
arcane_type.uprel([attu[3], attu[3], attu[3], attu[3], attu[3], attu[3], attu[3], attu[4], attu[4], attu[4],
                   attu[3], attu[3], attu[3], attu[3], attu[3], attu[3], attu[3]]);
# print(arcane_type.relatt); # TEST
physical_type.uprel([attu[0], attu[0], attu[1], attu[0], attu[0], attu[0], attu[1], attu[0], attu[5], attu[5], attu[0],
                     attu[0], attu[1]]);
finesse_type.uprel([attu[1], attu[3], attu[1], attu[4], attu[1], attu[1], attu[4]]);
social_type.uprel([attu[2], attu[4], attu[2], attu[2], attu[2], attu[2]]);
practical_type.uprel([attu[3], attu[1], attu[4], attu[2], attu[3]]);
# Finally: The Skill_list
Skills = Skill_list(knowledge_type, arcane_type, physical_type, finesse_type, social_type, practical_type);




# 22.9.2017 - after 17:05: Created the file. Created a prelimiary class Skill_list:.
# Created a prelimiary def listing(name): which will probably be replaced
# Between 21:30 and 21:42? - Created a new class Skill_type_list:
# 23.9.2017 - 10:02: Finally had a breakthrough. In the new class from yesterday night, I created two new variables.
# And I've decided all variables here will be lists. The first list will contain the skill names, the second list will
# contain the related attributes for each skill, and the third will contain the over skill index (or 0 if there is
# none). There is a fourth list of 0 or 1 or 2 to see if the skill is hidden by default, where 1 is hidden except for
# level up, and 2 is hidden completely. Created 3 of the 6 list and the extra connection to the sources list. Added a
# function to the skill_type_list that adds the connection list if the type is arcane.
# 17:20 - Finished with the skill lists (at least for now). Now to create the Skill_type_lists
# 18:05 - Defined all Skill_type_lists, implemented a function for creating upskill, and defined it for all
# Skill_type_lists.
# 21:30 - 22:22 - implemented and defined for ishidden. Added a similiar is hidden for the connections connhidden,
# implemented uprel and started defining the related attributes. Defined for knowledge arcane and physical.
# 24.9.2017 - 14:58 - Finished doing uprel for all types.
# 26.9.2017, 00:25 - Added to the Nature knowledge skill (knowledge) to the name bacause of a problem with the class
# skills in the relevant file: the connection to the nature source and the nature knowledge had the same name so the
# value was changed instead of creating the new key. Would probably try at least to implement some other fix? We'll see
# later. I want to finish quickly for now.

