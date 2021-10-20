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
        
        
    #Liquid
    if line[4] == "0":
      Liquid = image.open("Waterless.png")
      
    elif line[4] == "1":
      Liquid = image.open("Methane Oceans.png")
        
    elif line[4] == "2":
      Liquid = image.open("Methane Rivers.png")
        
    elif line[4] == "3":
      Liquid = image.open("Water Oceans.png")
        
    elif line[4] == "4":
      Liquid = image.open("Water Rivers.png")
      
    elif line[4] == "5":
      Liquid = image.open("Frozen Oceans.png")
        
    elif line[4] == "6":
      Liquid = image.open("Frozen Rivers.png")
        
    elif line[4] == "7":
      Liquid = image.open("Dry Oceans.png")
        
    elif line[4] == "8":
      Liquid = image.open("Dry Rivers.png")
        
    elif line[4] == "9":
      Liquid = image.open("Waterless.png")
        
    #Craters
    if line[5] == "0":
      Crater = image.open("No Craters.png")
      
    elif line[5] == "1":
      Crater = image.open("Large Impact.png")
        
    elif line[5] == "2":
      Crater = image.open("Large Impact and Volcanic Caldera.png")
        
    elif line[5] == "3":
      Crater = image.open("Volcanic Caldera.png")
      
    elif line[5] == "4":
      Crater = image.open("No Crater.png")
      
    #Magma
    if line[6] == "0":
      Magma = image.open("No Magma.png")
      
    elif line[6] == "1":
      Magma = image.open("Magma Oceans.png")
        
    elif line[6] == "2":
      Magma = image.open("Magma Rivers.png")
        
    elif line[6] == "3":
      Magma = image.open("No Magma.png")
      
    #Volcano
    if line[7] == "0":
      Volcano = image.open("No Volcano.png")
      
    elif line[7] == "1":
      Volcano = image.open("Volcano.png")
        
    elif line[7] == "2":
      Volcano = image.open("No Volcano.png")
      
    #Clouds
    if line[8] == "1":
      Clouds = image.open("Veil Clouds.png")
        
    elif line[8] == "2":
      Clouds = image.open("Stratocumulus Clouds.png")
        
    elif line[8] == "3":
      Clouds = image.open("Cumulus Clouds (White).png")
       
    elif line[8] == "4":
      Clouds = image.open("No Clouds.png")
      
    elif line[8] == "5":
      Clouds = image.open("Cumulus Clouds (White).png")
        
    elif line[8] == "6":
      Clouds = image.open("Cumulus Clouds (Silicate).png")
        
    elif line[8] == "7":
      Clouds = image.open("Cumulus CLouds (Ammonia).png")
        
    elif line[8] == "8":
      Clouds = image.open("Cumulonimbus Clouds (White).png")
        
    elif line[8] == "9":
      Clouds = image.open("Cumulonimbus Clouds (Silicate).png")
      
    elif line[8] == "k":
      Clouds = image.open("Cumulonimbus Clouds (Ammonia).png")
        
    elif line[8] == "l":
      Clouds = image.open("No Clouds.png")
      
    #Moons
    if line [9] == "0":
      Moons = image.open("No Moons.png")
    
    elif line[9] == "1":
      Moons = image.open("One Moon Brown.png")
        
    elif line[9] == "2":
      Moons = image.open("One Moon Green.png")
       
    elif line[9] == "3":
      Moons = image.open("One Moon Iron.png")
      
    elif line[9] == "4":
      Moons = image.open("One Moon Blue.png")
        
    elif line[9] == "5":
      Moons = image.open("One Moon Red.png")
        
    elif line[9] == "6":
      Moons = image.open("Two Moons Brown.png")
        
    elif line[9] == "7":
      Moons = image.open("Two Moons Green.png")
        
    elif line[9] == "8":
      Moons = image.open("Two Moons Iron.png")
      
    elif line[9] == "9":
      Moons = image.open("Two Moons Blue.png")
        
    elif line[9] == "k":
      Moons = image.open("Two Moons Red.png")
      
    elif line[9] == "l":
      Moons = image.open("Two Moons Brown and Green.png")
      
    elif line[9] == "m":
      Moons = image.open("Two Moons Brown and Iron.png")
      
    elif line[9] == "n":
      Moons = image.open("Two Moons Brown and Blue.png")
      
    elif line[9] == "o":
      Moons = image.open("Two Moons Brown and Red.png")
      
    elif line[9] == "p":
      Moons = image.open("Two Moons Green and Iron.png")
      
    elif line[9] == "q":
      Moons = image.open("Two Moons Green and Blue.png")
      
    elif line[9] == "r":
      Moons = image.open("Two Moons Green and Red.png")
      
    elif line[9] == "s":
      Moons = image.open("Two Moons Iron and Blue.png")
      
    elif line[9] == "t":
      Moons = image.open("Two Moons Iron and Red.png")
      
    elif line[9] == "u":
      Moons = image.open("Two Moons Blue and Red.png")
      
    elif line[9] == "v":
      Moons = image.open("No Moons.png")
    
    #Rings
    if line[10] == "0"
      Rings = image.open("No Rings.png")
      
    elif line[10] == "1":
      Rings = image.open("One Ring Brown.png")
        
    elif line[10] == "2":
      Rings = image.open("One Ring Brown (Vertical).png")
       
    elif line[10] == "3":
      Rings = image.open("One Ring Iron.png")
      
    elif line[10] == "4":
      Rings = image.open("One Ring Iron (Vertical).png")
        
    elif line[10] == "5":
      Rings = image.open("One Ring Green.png")
        
    elif line[10] == "6":
      Rings = image.open("One Ring Green (Vertical).png")
        
    elif line[10] == "7":
      Rings = image.open("Two Brown Rings (One Vertical).png")
        
    elif line[10] == "8":
      Rings = image.open("Two Iron Rings (One Vertical).png")
      
    elif line[10] == "9":
      Rings = image.open("Two Green Rings (One Vertical).png")
        
    elif line[10] == "k":
      Rings = image.open("Two Brown and Green Rings (One Vertical).png")
      
    elif line[10] == "l":
      Rings = image.open("Two Grey and Brown Rings (One Vertical).png")
      
    elif line[10] == "m":
      Rings = image.open("Two Green and Grey Rings (One Vertical).png")
      
    elif line[10] == "n":
      Rings = image.open("No Rings.png")
      
    elif line[10] == "o":
      Rings = image.open("Two Brown Rings (45°).png")
      
    elif line[10] == "p":
      Rings = image.open("Two Iron Rings (45°).png")
      
    elif line[10] == "q":
      Rings = image.open("Two Green Rings (45°).png")
      
    elif line[10] == "r":
      Rings = image.open("Two Brown and Green Rings (45°).png")
      
    elif line[10] == "s":
      Rings = image.open("Two Grey and Brown Rings (45°).png")
      
    elif line[10] == "t":
      Rings = image.open("Two Green and Grey Rings (45°).png")
      
    elif line[10] == "u":
      Rings = image.open("No Rings.png")
    
    Layer1 = Base.paste(Liquid)
    Layer2 = Layer1.paste(Crater)
    Layer3 = Layer2.paste(Magma)
    Layer4 = Layer3.paste(Volcano)
    Layer5 = Layer4.paste(Clouds)
    Layer6 = Layer5.paste(Moons)
    Layer7 = Layer6.paste(Rings)
    
    x = 1 
    
    Layer7.save("AlgoPlanet" + x + ".png")
    x+=1
      
   
       
    
