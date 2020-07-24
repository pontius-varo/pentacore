#this is the index of text. All text is fetched from here\
#Be sure to put a space at the end of each sentence! (This does not apply to the last sentence in each description.)
rms = {"ROOM1":{ "UNVISTED_TEXT" : "From the abyss of sleep does your consciousness emerge. Your vision is blury and your mouth is dry. "
                                    "You have no recollection of where you are, and find yourself very much confused. "
                                    "After a few seconds your vision clears and you are finally able to observe your surroundings........ "
                                    "You find yourself in what seems to be a log cabin. The walls are made of what looks to be fine oak logs. "
                                    "The room is relatively small. In addition, there is a fine red door to the NORTH, a small window in the SOUTH, "
                                    "and what appears to be a basement enterance in the EAST.",

                  "VISTED_TEXT" :   "Again, you find yourself in the room where you awoke. The walls are made of fine oak logs. "
                                    "The room is relatively small. There is a fine red door to the NORTH, a small window in the SOUTH, "
                                    "and what appears to be a basement enterance in the EAST.",

                  "ROUTES" : ["NORTH", "SOUTH", "EAST"],
                  },
        "ROOM2":{ "UNVISTED_TEXT": "You go NORTH and open the fine red door. You enter another room similar to the last, except it appears to be more of a bedroom. "
                                    "The walls are made of the same fine oak logs. There is a bed in the North corner of the room, and a small boarded window above it. "
                                    "There appears to be a closet in the WEST, a chest in the EAST, and the door returning to the previous room in the SOUTH.",

                  "VISTED_TEXT": "You go NORTH and open the fine red door. There is a bed in the North corner of the room, and a small boarded window above it. "
                                 "There appears to be a closet in the WEST, a chest in the EAST, and the door returning to the previous room in the SOUTH.",

                  "ROUTES": ["WEST", "EAST", "SOUTH"],
                },
        "ROOM3":{ "UNVISTED_TEXT": "You go SOUTH through the window. You are now outside of the log cabin. "
                                    "In front of you is a meadow to the SOUTH. To the EAST there appears to be a forest, while behind you to the NORTH is the window. ",
                   "VISTED_TEXT": "You find yourself outside of the log cabin. In front of you is a meadow to the SOUTH, while there is a forest in the EAST. "
                                    "Behind you to the NORTH is the window leading to the inside of the log cabin.",
                "ROUTES": ["NORTH", "SOUTH", "EAST"],
                },

        "ROOM4":{ "UNVISTED_TEXT": "You enter the basement. It is very dark and you can hear some-sort of noise in the distance. It is very likely that you will be eaten by a Grue....",
                    "VISTED_TEXT": "NULL",
                    "ROUTES": ["WEST"],
                },
        "ROOM5":{ "UNVISTED_TEXT": "You enter the closet in the NORTH. It is very dark and you feel as if you're being watched. You are likely to be eaten by a Grue.",
                "UNVISTED_TEXT": "NULL"}
            }

#==========#
items = { "SWORD":              {"DESC": "A fine silver sword decorated with a plethora of jewels. It seems to glow whenever enemies are nearby, which reminds you "
                                        "of a certain story concerning hobbits.",
                                        "USE": None },

           "RING":              {"DESC": "A small golden ring that is very plain looking. However, you can't help but feel as if an odd, maybe even evil, power is radiating "
                                        "from it.",
                                        "USE": None },
        }
