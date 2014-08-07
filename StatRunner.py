# Constants
AGI_SKILLS = ('Archery','Automatics','Blades','Clubs','Exotic Ranged Weapon',
              'Heavy Weapons','Long Arms','Pistols','Throwing Weapons','Unarmed Combat',
              'Gunnery','Gymnastics','Escape Artist','Exotic Melee Weapon','Locksmith',
              'Palming','Sneaking',)
BOD_SKILLS = ('Diving','Freefall')
REA_SKILLS = ('Pilot Aerospace','Pilot Aircraft','Pilot Walker','Pilot Exotic Vehicle',
              'Pilot Ground Craft','Pilot Water Craft')
STR_SKILLS = ('Running','Swimming')
CHR_SKILLS = ('Con','Etiquette','Instruction','Intimidation','Leadership','Negotiation',
              'Performance','Impersonation','Animal Handling')
INT_SKILLS = ('Artisan','Assensing','Disguise','Navigation','Perception','Tracking')
LOG_SKILLS = ('Aeronautics Mechanics','Arcane','Armorer','Automotive Mechanic',
              'Biotechnology','Chemistry','Computer','Cybertechnology','Cybercombat',
              'Demolitions','Electronic Warfare','First Aid','Industrial Mechanics',
              'Hacking','Hardware','Medicine','Nautical Mechanics','Software','Forgery')

def Engineer_Master_Skill_Dictionary():
    """
    Returns a dictionary of every skill in SR5.
    Skill_Name : [Rating, Specification, Attribute]
    """
    skill_list = {}
    for skill_name in AGI_SKILLS:    skill_list[skill_name] = [0,None,'AGI']
    for skill_name in BOD_SKILLS:    skill_list[skill_name] = [0,None,'BOD']
    for skill_name in REA_SKILLS:    skill_list[skill_name] = [0,None,'REA']
    for skill_name in STR_SKILLS:    skill_list[skill_name] = [0,None,'STR']
    for skill_name in CHR_SKILLS:    skill_list[skill_name] = [0,None,'CHR']
    for skill_name in INT_SKILLS:    skill_list[skill_name] = [0,None,'INT']
    for skill_name in LOG_SKILLS:    skill_list[skill_name] = [0,None,'LOG']
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
            print skill+": "+str(self.Skills[skill][0])+'\t',

    def Reset_Skills(self):
        for skill in self.Skills:
            self.Skills[skill][0] = 0
            self.Skills[skill][1] = None
