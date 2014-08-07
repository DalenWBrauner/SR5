class Skill(object):
    
    def __init__(self,Name,Attribute):
        self.Name = Name
        self.Attribute = Attribute
        self.Rating = 0
        self.Specification = None

    def __str__(self):
        if self.Specification == None:
            return self.Name + ": " + str(self.Rating)
        else:
            return self.Name + ": " + str(self.Rating) + ", " + self.Specification

def Engineer_Master_Skill_Dictionary():
    """
    Returns a dictionary of every skill in SR5.
    Skill_Name : [Rating, Specification, Attribute]
    """
    skill_list = {}
    # AGI Skills
    for skill_name in ['Archery','Automatics','Blades','Clubs','Exotic Ranged Weapon',
                       'Heavy Weapons','Long Arms','Pistols','Throwing Weapons',
                       'Unarmed Combat','Gunnery','Gymnastics','Escape Artist',
                       'Exotic Melee Weapon','Locksmith','Palming','Sneaking',]:
        skill_list[skill_name] = [0,None,'AGI']
    # BOD Skills
    for skill_name in ['Diving','Freefall']:
        skill_list[skill_name] = [0,None,'BOD']
    # REA Skills
    for skill_name in ['Pilot Aerospace','Pilot Aircraft','Pilot Walker',
                       'Pilot Exotic Vehicle','Pilot Ground Craft','Pilot Water Craft']:
        skill_list[skill_name] = [0,None,'REA']
    # STR Skills
    for skill_name in ['Running','Swimming']:
        skill_list[skill_name] = [0,None,'STR']
    # CHR Skills
    for skill_name in ['Con','Etiquette','Instruction','Intimidation','Leadership',
                       'Negotiation','Performance','Impersonation','Animal Handling']:
        skill_list[skill_name] = [0,None,'CHR']
    # INT Skills
    for skill_name in ['Artisan','Assensing','Disguise','Navigation','Perception',
                       'Tracking']:
        skill_list[skill_name] = [0,None,'INT']
    # LOG Skills
    for skill_name in ['Aeronautics Mechanics','Arcane','Armorer','Automotive Mechanic',
                       'Biotechnology','Chemistry','Computer','Cybertechnology',
                       'Cybercombat','Demolitions','Electronic Warfare','First Aid',
                       'Industrial Mechanics','Hacking','Hardware','Medicine',
                       'Nautical Mechanics','Software','Forgery']:
        skill_list[skill_name] = [0,None,'LOG']
    # WIL Skills
    for skill_name in ['Astral Combat','Survival']:
        skill_list[skill_name] = [0,None,'WIL']
    # All done!
    return skill_list

class Hero(object):

    def __init__(self,Name="Nameless",Attributes=(1,1,1,1,1,1,1,1,1),Race='Human'):
        self.Name = Name
        self.BOD = Attributes[0]
        self.AGI = Attributes[1]
        self.REA = Attributes[2]
        self.STR = Attributes[3]
        self.WIL = Attributes[4]
        self.LOG = Attributes[5]
        self.INT = Attributes[6]
        self.CHR = Attributes[7]
        self.EDG = Attributes[8]
        self.Race = Race
        self.Skills = Engineer_Master_Skill_Dictionary()

    def Print_Skills(self):
        for skill in self.Skills:
            print skill+": "+str(self.Skills[skill][0])

    def Reset_Skills(self):
        for skill in self.Skills:
            self.Skills[skill][0] = 0
            self.Skills[skill][1] = None
