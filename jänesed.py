#kuidagi ümbernurga lahendus tundub tahaks paremat viisi teada.
ringid = int(input("Mitu ringi?  "))
tulemus = int(0)
a=int(0)

if ringid<0:
    
    print("hoopis lammas?")
   
else:

    while ringid-2>=a:
             
        tulemus = int(tulemus+a+2)
        a = a+2
        
    print("Porgandite koguarv on ",tulemus )


