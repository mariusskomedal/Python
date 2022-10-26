
import random
x=1
ting= ["saks","stein","papir"]
while x ==1:
    tilfeldig = random.randint(0,2)
    en = input("Stein, saks eller papir?: ").lower()
    if ting[tilfeldig] =="saks":
        if en == "papir":
            print("Du tapte")
    if ting[tilfeldig] =="saks":
        if en == "stein":
            print("Du vant")
            x = 0
    if ting[tilfeldig] =="saks":
        if en == "saks":
            print("Uavgjort, prøv igjen")
    if ting[tilfeldig] =="stein":
        if en == "papir":
            print("Du vant")
            x = 0
    if ting[tilfeldig] =="stein":
        if en == "saks":
            print("Du tapte")
    if ting[tilfeldig] =="stein":
        if en == "stein":
            print("Uavgjort, prøv igjen")
    if ting[tilfeldig] =="papir":
        if en == "papir":
            print("Uavgjort, prøv igjen")
    if ting[tilfeldig] =="papir":
        if en == "stein":
            print("Du vant")
            x = 0
    if ting[tilfeldig] =="papir":
        if en == "saks":
            print("Du tapte")
print(ting[tilfeldig])

