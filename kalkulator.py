import math

x = 1
svar = float(input("Skriv inn et tall: "))
while x == 1:
    svar3 = input("Hva vil du med disse tallene, +, -, * eller /, skriv FERDIG for å ende: ").lower()
   
    if svar3 == "+":
        svar2 = float(input("Skriv et tall du vil plusse til: "))
        svar = svar + svar2
    if svar3 == "-":
        svar2 = float(input("Skriv et tall du vil minuse:  "))  
        svar = svar - svar2
    if svar3 == "*":
        svar2 = float(input("Skriv et tall du vil gange med: "))
        svar = svar*svar2
    if svar3 == "/":
        svar2 = float(input("Skriv et tall du vil dele med: "))
        svar = svar/svar2
    if svar3 == "ferdig":
        x =0
    print(svar)
print("Det blir", svar)
input("GG")


    
