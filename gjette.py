import random
x = 1
en=random.randint(1,100)
while x == 1:
    to = int(input("Gjett et tall mellom 1 og 100: "))
    if to < en:
        print("Du gjettet for lavt")
    if to > en:
        print("Du gjettet for høyt")
    if to == en:
        print("Det er riktig!")
        x = 0
input("Gratulerer!")

      