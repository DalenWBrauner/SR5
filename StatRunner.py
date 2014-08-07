from random import randint

#
##
### Constants
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
#
##
### Utility
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

#
##
### Hero Object
class Hero(object):

    def __init__(self,Name="Nameless",Attributes=(1,1,1,1,1,1,1,1,1),Race='Human'):
        """
        'Name':         Name of our Hero
        'Attributes':   BOD, AGI, REA, STR, WIL, LOG, INT, CHR, EDG in that order.
        'Race':         Race of our Hero
        """
        self.Name = Name
        self.ATT = {}
        self.ATT['BOD'] = Attributes[0]
        self.ATT['AGI'] = Attributes[1]
        self.ATT['REA'] = Attributes[2]
        self.ATT['STR'] = Attributes[3]
        self.ATT['WIL'] = Attributes[4]
        self.ATT['LOG'] = Attributes[5]
        self.ATT['INT'] = Attributes[6]
        self.ATT['CHR'] = Attributes[7]
        self.ATT['EDG'] = Attributes[8]
        self.Race = Race
        self.Skills = Engineer_Master_Skill_Dictionary()

    def Set_Skill(self,skill_name,new_value):
        # Let's make sure we don't implode our hero...
        if type(skill_name) != str:
            raise TypeError("skill_name "+str(skill_name)+" is not a string.")
        elif type(new_value) != int:
            raise TypeError("new_value "+str(new_value)+" is not an integer.")
        elif (new_value < 0) or (new_value > 6):
            raise ValueError("new_value "+str(new_value)+" is not between 0 and 6.")
        elif skill_name not in self.Skills:
            raise KeyError("Cannot set nonexistant "+skill_name+" skill to "+\
                           str(new_value)+" for "+self.Name+".")
        
        # So if nothing goes wrong,
        else:
            self.Skills[skill_name][0] = new_value

    def Print_Skills(self):
        for skill in self.Skills:
            print skill+": "+str(self.Skills[skill][0])+'\t',

    def Reset_Skills(self):
        for skill in self.Skills:
            self.Skills[skill][0] = 0
            self.Skills[skill][1] = None

    def Skill_Check(self,skill_name,hits_needed):
        # Let's make sure we don't implode our hero...
        if type(skill_name) != str:
            raise TypeError("skill_name "+str(skill_name)+" is not a string.")
        elif type(hits_needed) != int:
            raise TypeError("hits_needed "+str(hits_needed)+" is not an integer.")
        elif hits_needed < 1:
            raise ValueError("hits_needed "+str(hits_needed)+" is not at least 1.")
        elif skill_name not in self.Skills:
            raise KeyError("Cannot check nonexistant "+skill_name+" skill with "+\
                           str(hits_needed)+" hits for "+self.Name+".")

        # So if nothing goes wrong,
        else:
            Skill_Level, blarb, Which_Attribute = self.Skills[skill_name]
            Check(hits_needed, (Skill_Level + self.ATT[Which_Attribute]))
            

#
##
### Chance
def Check(hits_needed,dice_rolled):
    """
    Rolls the dice!
    Informs you if you've passed your check or not.
    """
    hits = 0
    misses = 0
    for dice in xrange(dice_rolled):
        result = randint(1,6)
        if result > 4:  hits +=1
        if result == 1: misses += 1
        print result,
    if hits >= hits_needed:     print "\nSuccess",
    else:                       print "\nFailure",
    print "with",misses,"misses."
