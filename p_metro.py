"""
    This is a transliteration of the Pascal program in "Murder at the
    Metropolitan Club" in Elementary Pascal by Ledgard and Singer.
"""

unknown = 0
red = 1
black = 2
grey = 3
brown = 4

pincenez = 1
goldwatch = 2
rubyring = 3
tatteredcuffs = 4

colwoodley = 1
mrholman = 2
mrpope = 3
sirraymond = 4

jasper = "Sir Raymond Jasper"
woodley = "Colonel Woodley"
pope = "Mr. Pope"
holman = "Mr. Holman"

names = (0, woodley, holman, pope, jasper)

murderer = unknown
# Pascal arrays begin with 1 so our zero-th element is unused.
hair = [0 for i in range(5)]
attire = [0 for j in range(5)]
room = [0 for k in range(5)]

room[sirraymond] = 10
attire[mrpope] = goldwatch
attire[mrholman] = rubyring
room[mrholman] = 12

suspect = colwoodley
while murderer == unknown:
    if room[suspect] == 14:
        hair[suspect] = black
    if attire[sirraymond] and attire[sirraymond] != pincenez:
        attire[colwoodley] = pincenez
    if attire[colwoodley] and attire[colwoodley] != pincenez:
        attire[sirraymond] = pincenez
    if attire[suspect] == pincenez:
        hair[suspect] = brown
    if attire[suspect] == tatteredcuffs:
        hair[suspect] = red
    if room[suspect] == 16:
        attire[suspect] = tatteredcuffs
    if room[suspect] == 12:
        hair[suspect] = grey
    if attire[suspect] == goldwatch:
        room[suspect] = 14
    if room[suspect] == 10 and suspect != colwoodley:
        room[colwoodley] = 16
    if room[suspect] == 16 and suspect != colwoodley:
        room[colwoodley] = 10
    if hair[suspect] == brown:
        murderer = suspect
    if suspect == sirraymond:
        suspect = colwoodley
    else:
        suspect += 1
print(f'The murderer is {names[murderer]}.')
