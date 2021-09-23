"""
    Murder at the Metropolitan Club from "Elementary Basic" by
    Ledgard and Singer
"""
from itertools import permutations

jasper = "Sir Raymond Jasper"
woodley = "Colonel Woodley"
pope = "Mr. Pope"
holman = "Mr. Holman"

pincenez = "pince-nez"
watch = "gold pocket watch"
tattered = "tattered cuffs"
ring = "ruby signet ring"

black = "black"
brown = "brown"
red = "red"
grey = "grey"

names = (jasper, woodley, pope, holman)
rooms = (10, 12, 14, 16)
corner_rooms = (10, 16)
hair = (black, brown, red, grey)
attire = (pincenez, watch, tattered, ring)


for current_names in permutations(names):

    for current_rooms in permutations(rooms):
        # 1. Sir Raymond Jasper occupied Room 10.
        if current_names.index(jasper) != current_rooms.index(10):
            continue
        # 9. Mr Holman occupied Room 12.
        if current_names.index(holman) != current_rooms.index(12):
            continue
        # 13.  Colonel Woodley occupied a corner room.
        if current_names.index(woodley) not in (
                current_rooms.index(10), current_rooms.index(16)):
            continue

        for current_hair in permutations(hair):
            # 2. The man occupying Room 14 had black hair.
            if current_rooms.index(14) != current_hair.index(black):
                continue
            # 11. The man in Room 12 had grey hair.
            if current_rooms.index(12) != current_hair.index(grey):
                continue

            for current_attire in permutations(attire):
                # 3. Either Colonel Woodley or Sir Raymond wore a pince-nez.
                if current_attire.index(pincenez) not in (
                        current_names.index(woodley),
                        current_names.index(jasper)):
                    continue
                # 4. Mr. Pope always carried a gold pocket watch.
                if current_names.index(pope) != current_attire.index(watch):
                    continue
                # 6. The man with the pince-nez had brown hair.
                if current_attire.index(pincenez) != current_hair.index(brown):
                    continue
                # 7. Mr. Holman wore a ruby signet ring.
                if current_attire.index(ring) != current_names.index(holman):
                    continue
                # 8. The man in Room 16 had tattered cuffs.
                if current_attire.index(tattered) != current_rooms.index(16):
                    continue
                # 10. The man with tattered cuffs had red hair.
                if current_attire.index(tattered) != current_hair.index(red):
                    continue
                # 12. The man with a gold pocket watch occupied Room 14.
                if current_rooms.index(14) != current_attire.index(watch):
                    continue

                # 14. The murderer had brown hair
                murderer = current_names[current_hair.index(brown)]
                print(f'The murderer is {murderer}')
