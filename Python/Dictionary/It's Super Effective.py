# Date - Oct 7, 2020 By Jatin Sharma

import json
import sys
def calc_eff(effectiveness, attack, defend):
    if defend in effectiveness['super'][attack]:
        eff = 2
    elif defend in effectiveness['nv'][attack]:
        eff = 0.5
    elif defend in effectiveness['immune'][attack]:
        eff = 0
    else:
        eff = 1
    return eff
def cumm_offensive(effectiveness, t1, t2):
    sum = 0
    for i in t1:
        t1_types = i.split(' ')
        for j in t2:
            t2_types = j.split(' ')
            eff1 = calc_eff(effectiveness, t1_types[0], t2_types[0])
            eff2 = 0
            if len(t2_types) == 2:
                eff1 *= calc_eff(effectiveness, t1_types[0], t2_types[1])
            if len(t1_types) == 2:
                eff2 = calc_eff(effectiveness, t1_types[1], t2_types[0])
                if len(t2_types) == 2:
                    eff2 *= calc_eff(effectiveness, t1_types[1], t2_types[1])
            sum += max(eff1, eff2)
    return float(sum)
if __name__== "__main__":
    effectiveness = {
        "super": {
            "Normal": [],
            "Fire": [
                "Grass",
                "Ice",
                "Bug",
                "Steel"
            ],
            "Water": [
                "Fire",
                "Ground",
                "Rock"
            ],
            "Electric": [
                "Water",
                "Flying"
            ],
            "Grass": [
                "Water",
                "Ground",
                "Rock"
            ],
            "Ice": [
                "Grass",
                "Ground",
                "Flying",
                "Dragon"
            ],
            "Fighting": [
                "Normal",
                "Ice",
                "Rock",
                "Dark",
                "Steel"
            ],
            "Poison": [
                "Grass",
                "Fairy"
            ],
            "Ground": [
                "Fire",
                "Electric",
                "Poison",
                "Rock",
                "Steel"
            ],
            "Flying": [
                "Grass",
                "Fighting",
                "Bug"
            ],
            "Psychic": [
                "Fighting",
                "Poison"
            ],
            "Bug": [
                "Grass",
                "Psychic",
                "Dark"
            ],
            "Rock": [
                "Fire",
                "Ice",
                "Flying",
                "Bug"
            ],
            "Ghost": [
                "Psychic",
                "Ghost"
            ],
            "Dragon": [
                "Dragon"
            ],
            "Dark": [
                "Psychic",
                "Ghost"
            ],
            "Steel": [
                "Ice",
                "Rock",
                "Fairy"
            ],
            "Fairy": [
                "Fighting",
                "Dragon",
                "Dark"
            ]
        },
        "normal": {
            "Normal": [
                "Normal",
                "Fire",
                "Water",
                "Electric",
                "Grass",
                "Ice",
                "Fighting",
                "Poison",
                "Ground",
                "Flying",
                "Psychic",
                "Bug",
                "Dragon",
                "Dark",
                "Fairy"
            ],
            "Fire": [
                "Normal",
                "Electric",
                "Fighting",
                "Poison",
                "Ground",
                "Flying",
                "Psychic",
                "Ghost",
                "Dark",
                "Fairy"
            ],
            "Water": [
                "Normal",
                "Electric",
                "Ice",
                "Fighting",
                "Poison",
                "Flying",
                "Psychic",
                "Bug",
                "Ghost",
                "Dark",
                "Steel",
                "Fairy"
            ],
            "Electric": [
                "Normal",
                "Fire",
                "Ice",
                "Fighting",
                "Poison",
                "Psychic",
                "Bug",
                "Rock",
                "Ghost",
                "Dark",
                "Steel",
                "Fairy"
            ],
            "Grass": [
                "Normal",
                "Electric",
                "Ice",
                "Fighting",
                "Psychic",
                "Ghost",
                "Dark",
                "Fairy"
            ],
            "Ice": [
                "Normal",
                "Electric",
                "Fighting",
                "Poison",
                "Psychic",
                "Bug",
                "Rock",
                "Ghost",
                "Dark",
                "Fairy"
            ],
            "Fighting": [
                "Fire",
                "Water",
                "Electric",
                "Grass",
                "Fighting",
                "Ground",
                "Dragon"
            ],
            "Poison": [
                "Normal",
                "Fire",
                "Water",
                "Electric",
                "Ice",
                "Fighting",
                "Flying",
                "Psychic",
                "Bug",
                "Dragon",
                "Dark"
            ],
            "Ground": [
                "Normal",
                "Water",
                "Ice",
                "Fighting",
                "Ground",
                "Psychic",
                "Ghost",
                "Dragon",
                "Dark",
                "Fairy"
            ],
            "Flying": [
                "Normal",
                "Fire",
                "Water",
                "Ice",
                "Poison",
                "Ground",
                "Flying",
                "Psychic",
                "Ghost",
                "Dragon",
                "Dark",
                "Fairy"
            ],
            "Psychic": [
                "Normal",
                "Fire",
                "Water",
                "Electric",
                "Grass",
                "Ice",
                "Ground",
                "Flying",
                "Bug",
                "Rock",
                "Ghost",
                "Dragon",
                "Fairy"
            ],
            "Bug": [
                "Normal",
                "Water",
                "Electric",
                "Ice",
                "Ground",
                "Bug",
                "Rock",
                "Dragon"
            ],
            "Rock": [
                "Normal",
                "Water",
                "Electric",
                "Grass",
                "Poison",
                "Psychic",
                "Rock",
                "Ghost",
                "Dragon",
                "Dark",
                "Fairy"
            ],
            "Ghost": [
                "Fire",
                "Water",
                "Electric",
                "Grass",
                "Ice",
                "Fighting",
                "Poison",
                "Ground",
                "Flying",
                "Bug",
                "Rock",
                "Dragon",
                "Steel",
                "Fairy"
            ],
            "Dragon": [
                "Normal",
                "Fire",
                "Water",
                "Electric",
                "Grass",
                "Ice",
                "Fighting",
                "Poison",
                "Ground",
                "Flying",
                "Psychic",
                "Bug",
                "Rock",
                "Ghost",
                "Dark"
            ],
            "Dark": [
                "Normal",
                "Fire",
                "Water",
                "Electric",
                "Grass",
                "Ice",
                "Poison",
                "Ground",
                "Flying",
                "Bug",
                "Rock",
                "Dragon",
                "Steel"
            ],
            "Steel": [
                "Normal",
                "Grass",
                "Fighting",
                "Poison",
                "Ground",
                "Flying",
                "Psychic",
                "Bug",
                "Ghost",
                "Dragon",
                "Dark"
            ],
            "Fairy": [
                "Normal",
                "Water",
                "Electric",
                "Grass",
                "Ice",
                "Ground",
                "Flying",
                "Psychic",
                "Bug",
                "Rock",
                "Ghost",
                "Fairy"
            ]
        },
        "nv": {
            "Normal": [
                "Rock",
                "Steel"
            ],
            "Fire": [
                "Fire",
                "Water",
                "Rock",
                "Dragon"
            ],
            "Water": [
                "Water",
                "Grass",
                "Dragon"
            ],
            "Electric": [
                "Electric",
                "Grass",
                "Dragon"
            ],
            "Grass": [
                "Fire",
                "Grass",
                "Poison",
                "Flying",
                "Bug",
                "Dragon",
                "Steel"
            ],
            "Ice": [
                "Fire",
                "Water",
                "Ice",
                "Steel"
            ],
            "Fighting": [
                "Poison",
                "Flying",
                "Psychic",
                "Bug",
                "Fairy"
            ],
            "Poison": [
                "Poison",
                "Ground",
                "Rock",
                "Ghost"
            ],
            "Ground": [
                "Grass",
                "Bug"
            ],
            "Flying": [
                "Electric",
                "Rock",
                "Steel"
            ],
            "Psychic": [
                "Psychic",
                "Steel"
            ],
            "Bug": [
                "Fire",
                "Fighting",
                "Poison",
                "Flying",
                "Ghost",
                "Steel",
                "Fairy"
            ],
            "Rock": [
                "Fighting",
                "Ground",
                "Steel"
            ],
            "Ghost": [
                "Dark"
            ],
            "Dragon": [
                "Steel"
            ],
            "Dark": [
                "Fighting",
                "Dark",
                "Fairy"
            ],
            "Steel": [
                "Fire",
                "Water",
                "Electric",
                "Steel"
            ],
            "Fairy": [
                "Fire",
                "Poison",
                "Steel"
            ]
        },
        "immune": {
            "Normal": [
                "Ghost"
            ],
            "Fire": [],
            "Water": [],
            "Electric": [
                "Ground"
            ],
            "Grass": [],
            "Ice": [],
            "Fighting": [
                "Ghost"
            ],
            "Poison": [
                "Steel"
            ],
            "Ground": [
                "Flying"
            ],
            "Flying": [],
            "Psychic": [
                "Dark"
            ],
            "Bug": [],
            "Rock": [],
            "Ghost": [
                "Normal"
            ],
            "Dragon": [
                "Fairy"
            ],
            "Dark": [],
            "Steel": [],
            "Fairy": []
        }
    }
    n1 = int(input())
    n2 = int(input())
    t1 = []
    t2 = []
    for i in range(2, 2 + n1):
        t1.append(input())
    for i in range(2 + n1, 2 + n1 + n2):
        t2.append(input())
    me = cumm_offensive(effectiveness, t1, t2)
    foe = cumm_offensive(effectiveness, t2, t1)
    print(me)
    print(foe)
    if me > foe:
        print("ME")
    elif me == foe:
        print("NONE")
    else:
        print("FOE")