from PIL import Image

with open("Unicode.txt", "r") as file:

  #BASE PLANET
  for line in file:
    #Terrestrial
    if line[1] == "1":
      Base = image.open("Blue Terrestrial Planet.png")
      
    elif line[1] == "2":
        Base = image.open("Green Terrestrial Planet.png")
        
    elif line[1] == "3":
        Base = image.open("Brown Terrestrial Planet.png")
        
    elif line[1] == "4":
        Base = image.open("Iron Terrestrial Planet.png")
        
    elif line[1] == "5":
        Base = image.open("Red Terrestrial Planet.png")
        
    elif line[1] == "6":
        Base = image.open("Yellow Terrestrial Planet.png")
        
    elif line[1] == "7":
        Base = image.open("Purple Terrestrial Planet.png")
    
    #Gas
    if line[2] == "1":
      Base = image.open("Sand Gas Planet.png")
      
    elif line[2] == "2":
        Base = image.open("Turquoise Gas Planet.png")
        
    elif line[2] == "3":
        Base = image.open("Brown Gas Planet.png")
        
    elif line[2] == "4":
        Base = image.open("Red Gas Planet.png")
        
    #IceGiant
    if line[3] == "1":
      Base = image.open("Dark Blue Ice Giant Planet.png")
      
    elif line[3] == "2":
        Base = image.open("Icy White Ice Giant Planet.png")
        
    elif line[3] == "3":
        Base = image.open("Light Blue Ice Giant Planet.png")
       
    
