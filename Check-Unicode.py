with open("AlgoPlanet_Unicode.txt","r") as file:
    
    C = 0
    R = 0
    SR = 0
    UR = 0
    Secret = 0
    
    for line in file:
    
        if line[0] == "4" or line[0] == "5" or line[0] == "6" or line[0] == "7":
            Secret +=1    

        elif line[4] == "7" or line[4] == "8" or line[7] == "1" or line[5] == "2" or line[6] == "1" or line[9] == "n" or line[9] == "o" or line[9] == "p" or line[9] == "q" or line[9] == "r" or line[9] == "s" or line[9] == "t" or line[9] == "u" or line[9] == "v" or line[9] == "w" or line[9] == "x" or line[9] == "y" or line[10] == "o" or line[10] == "p" or line[10] == "q" or line[10] == "r" or line[10] == "s" or line[10] == "t":
            UR +=1

        elif line[4] == "1" or line[4] == "2" or line[5] == "1" or line[6] == "2" or line[9] == "7" or line[9] == "8" or line[9] == "9" or line[9] == "k" or line[9] == "l" or line[9] == "m" or line[10] == "7" or line[10] == "8" or line[10] == "9" or line[10] == "k" or line[10] == "l" or line[10] == "m": 
            SR +=1

        elif line[4] == "5" or line[4] == "6" or line[5] == "3" or line[8] == "2" or line[8] == "8" or line[8] == "9" or line[8] == "k" or line[9] == "1" or line[9] == "2" or line[9] == "3" or line[9] == "4" or line[9] == "5" or line[9] == "6":
            R +=1

        else:
            C +=1
         
print("Secret Rare =", Secret)  
print("Ultra Rare =", UR)
print("Super Rare =", SR)
print("Rare =", R)
print("Common =", C)
