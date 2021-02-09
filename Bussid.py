# Matis Maamets ITT20
# 09.02.2021
# Kodutöö2
a = int(input("Kui palju reisijaid? "))
b = int(input("Kui palju kohtasid ühes bussis? "))

bussid = a // b
viimanebuss = a % b
print()
print ("Busside arv: ",bussid)
if viimanebuss != 0:
    print("Inimesi viimases bussis",viimanebuss)
else:
    print("Inimesi viimases bussis",b)

