# Matis Maamets ITT20
# 09.02.2021
# Kodutöö2import random

pp = int(input("Mitu pöialpoissi tahab õunu? "))
õunad=int(14)
läinud=int(0)


for x in range(pp):
    loos = random.randint(1,2)
    läinud = läinud+loos
    print(loos)
print("Lumivalgekesele jäi ",õunad-läinud)
