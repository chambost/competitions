puzzleinput = r""""""

testinput0 = r"""Immune System:
17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3

Infection:
801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4"""

from functools import partial

class System() :
    def __init__(self) :
        self.groups = []
        
    def add(self,group) :
        self.groups.append( group )
        
    def remove(self,group) :
        self.groups.remove( group )
        
    def untag_all(self) :
        for g in self.groups :
            g.tag = False
            
    def __len__(self) :
        return self.groups.__len__()
    
    def __iter__(self) :
        return self.groups.__iter__()
    
    def __add__(self,other) :
        return self.groups + other.groups
    
class Group() :
    def __init__(self,enemies,units,hp,immunities,weaknesses,dmg,dmgtype,initiative) :
        self.enemies = enemies
        self.units = units
        self.hp = hp
        self.immunities = immunities
        self.weaknesses = weaknesses
        self.dmg = dmg
        self.dmgtype = dmgtype
        self.initiative = initiative
        self.tag = False
        
    def __repr__(self) :
        return "I {}, {} hp, {} units, {} dmg, {} power, {}, imm: {}, weak: {}".format(
            self.initiative, self.hp, self.units, self.dmg, self.power(), self.dmgtype, self.immunities, self.weaknesses)
        
    def power(self) :
        return self.units * self.dmg
        
    def attack(self,other) :
        modifier = 2 if self.dmgtype in other.weaknesses else 1
        strength = self.units * self.dmg * modifier
        other.units -= strength // other.hp
        if other.units <= 0 :
            other.units = 0
            self.enemies.remove(other)
            
    def create_attack_action(self) :
        for e in sorted( [ e for e in self.enemies if self.dmgtype in e.weaknesses and not e.tag ]
                       , reverse=True 
                       , key=lambda x:(x.power(),x.initiative)
                       ) :
            e.tag = True
            return partial(self.attack,e)
        for e in sorted( [ e for e in self.enemies if self.dmgtype not in e.weaknesses and not e.tag and self.dmgtype not in e.immunities ]
                       , reverse=True 
                       , key=lambda x:(x.power(),x.initiative)
                       ) :          
            e.tag = True
            return partial(self.attack,e)
        return lambda : None
        

def extract(group,enemies) :
    if "(" in group :
        a,z = group.split("(")
        b,c = z.split(")")
        if ";" in b :
            first,second = b.split("; ")
            if first.startswith("immune to ") :
                immunities = tuple( first.lstrip("immune to ").split(", ") )
                weaknesses = tuple( second.lstrip("weak to ").split(", ") )
            else :
                immunities = tuple( second.lstrip("immune to ").split(", ") )
                weaknesses = tuple( first.lstrip("weak to ").split(", ") )                
        elif b.startswith("immune to ") :
            immunities = tuple( b.lstrip("immune to ").split(", ") )
            weaknesses = tuple()
        else :
            immunities = tuple()
            weaknesses = tuple( b.lstrip("weak to ").split(", ") )
        units,_,_,_,hp,_,_ = a.strip().split(" ")
        _,_,_,_,_,dmg,dmgtype,_,_,_,initiative = c.strip().split(" ")
    else :
        units,_,_,_,hp,_,_,_,_,_,_,_,dmg,dmgtype,_,_,_,initiative = group.split(" ")
        immunities = tuple()
        weaknesses = tuple()
    units = int(units)
    hp = int(hp)
    dmg = int(dmg)
    initiative = int(initiative)                               
    return Group(enemies,units,hp,immunities,weaknesses,dmg,dmgtype,initiative)


def initialise(choseninput) :
    first,second = choseninput.split("\n\n")
    first = first.lstrip("Immune System:\n")
    immune_system = System()
    infect_system = System()
    for group in first.split("\n") :
        immune_system.add( extract(group,infect_system) )
    second = second.lstrip("Infection:\n")
    for group in second.split("\n") :
        infect_system.add( extract(group,immune_system) ) 
    return immune_system, infect_system
    

def solve_day24a_aoc_2018(choseninput) :
    immune_system, infect_system = initialise(choseninput)
    while immune_system and infect_system :
        actions = []
        immune_system.untag_all()
        infect_system.untag_all()
        for g in sorted(infect_system + immune_system
                       ,reverse=True
                       ,key=lambda x:(x.power(),x.initiative)) :
            actions.append( ( g.initiative 
                            , g.create_attack_action() 
                            ) )
        for i,action in sorted(actions
                              ,reverse=True
                              ,key=lambda x:x[0]
                              ) :
            action()

    return sum( g.units for g in infect_system + immune_system )
    
solve_day24a_aoc_2018(testinput0)

