x = "20450000300" #test
C = 0
R = 0
SR = 0
UR = 0
Secret = 0

if x[0] == "3" or x[0] == "4" or x[0] == "5" or x[0] == "6":
    Secret +=1
    print("Secret Rare =", Secret)    
    
if x[4] == "6" or x[4] == "7" or x[7] == "0" or x[5] == "1" or x[6] == "0" or x[9] == "m" or x[9] == "n" or x[9] == "o" or x[9] == "p" or x[9] == "q" or x[9] == "r" or x[9] == "s" or x[9] == "t" or x[9] == "u" or x[9] == "v" or x[9] == "w" or x[9] == "x": #Rings fehlen Skript muss angepasst werden
    UR +=1
    print("Ultra Rare =", UR)

if x[4] == "0" or x[4] == "1" or x[5] == "0" or x[6] == "1" or x[9] == "g" or x[9] == "h" or x[9] == "i" or x[9] == "j" or x[9] == "k" or x[9] == "l": #Rings fehlen
    SR +=1
    print("Secret Rare =", SR)

if x[4] == "4" or x[4] == "5" or x[5] == "2" or x[8] == "1" or x[8] == "7" or x[8] == "8" or x[8] == "9" or x[9] == "a" or x[9] == "b" or x[9] == "c" or x[9] == "d" or x[9] == "e" or x[9] == "f":
    R +=1
    print("Rare =", R)
    
if x[4] == "2" or x[4] == "3" or x[4] == "8" or x[8] == "0" or x[8] == "2" or x[8] == "4" or x[8] == "5" or x[8] == "6" or x[8] == "3" or x[8] == "10" or x[9] == "y" or x[5] == "3" or x[6] == "2" or x[7] == "1": #Rings fehlen
    C +=1
    print("Common =", C)
