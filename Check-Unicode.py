with open("Unicode.txt","r") as file:
    
    C = 0
    R = 0
    SR = 0
    UR = 0
    Secret = 0
    
    for line in file:
    
        if line[0] == "3" or line[0] == "4" or line[0] == "5" or line[0] == "6":
            Secret +=1    

        elif line[4] == "6" or line[4] == "7" or line[7] == "0" or line[5] == "1" or line[6] == "0" or line[9] == "m" or line[9] == "n" or line[9] == "o" or line[9] == "p" or line[9] == "q" or line[9] == "r" or line[9] == "s" or line[9] == "t" or line[9] == "u" or line[9] == "v" or line[9] == "w" or line[9] == "line": #Rings fehlen Skript muss angepasst werden
            UR +=1

        elif line[4] == "0" or line[4] == "1" or line[5] == "0" or line[6] == "1" or line[9] == "g" or line[9] == "h" or line[9] == "i" or line[9] == "j" or line[9] == "k" or line[9] == "l": #Rings fehlen
            SR +=1

        elif line[4] == "4" or line[4] == "5" or line[5] == "2" or line[8] == "1" or line[8] == "7" or line[8] == "8" or line[8] == "9" or line[9] == "a" or line[9] == "b" or line[9] == "c" or line[9] == "d" or line[9] == "e" or line[9] == "f":
            R +=1

        elif line[4] == "2" or line[4] == "3" or line[4] == "8" or line[8] == "0" or line[8] == "2" or line[8] == "4" or line[8] == "5" or line[8] == "6" or line[8] == "3" or line[8] == "10" or line[9] == "y" or line[5] == "3" or line[6] == "2" or line[7] == "1": #Rings fehlen
            C +=1
         
print("Secret Rare =", Secret)  
print("Ultra Rare =", UR)
print("Secret Rare =", SR)
print("Rare =", R)
print("Common =", C)
