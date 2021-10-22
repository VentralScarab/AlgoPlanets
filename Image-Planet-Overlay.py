from PIL import Image, ImageDraw, ImageFilter

with open("AlgoPlanet_Unicode.txt", "r") as file:

  count = 1

  #base PLANET
  for line in file:

    #Terrestrial
    if line[1] == "1":
      base = Image.open("Blue Terrestrial Planet.png")
      
    elif line[1] == "2":
      base = Image.open("Green Terrestrial Planet.png")
        
    elif line[1] == "3":
      base = Image.open("Brown Terrestrial Planet.png")
        
    elif line[1] == "4":
      base = Image.open("Iron Terrestrial Planet.png")
        
    elif line[1] == "5":
      base = Image.open("Red Terrestrial Planet.png")
        
    elif line[1] == "6":
      base = Image.open("Yellow Terrestrial Planet.png")
        
    elif line[1] == "7":
      base = Image.open("Purple Terrestrial Planet.png")
    
    #Gas
    if line[2] == "1":
      base = Image.open("Purple Gas Planet.png")
      
    elif line[2] == "2":
      base = Image.open("Turquoise Gas Planet.png")
        
    elif line[2] == "3":
      base = Image.open("Brown Gas Planet.png")
        
    elif line[2] == "4":
      base = Image.open("Red Gas Planet.png")
        
    #IceGiant
    if line[3] == "1":
      base = Image.open("Dark Blue Ice Giant Planet.png")
      
    elif line[3] == "2":
      base = Image.open("Icy White Ice Giant Planet.png")
        
    elif line[3] == "3":
      base = Image.open("Light Blue Ice Giant Planet.png")

    #SecretRare
    if line[0] == "4":
      base = Image.open("Lava Planet.png")

    elif line[0] == "5":
      base = Image.open("Dwarf Planet.png")

    elif line[0] == "6":
      base = Image.open("Moon Impact Planet.png")
        
        
    #liquid
    if line[4] == "0":
      liquid = Image.open("No Liquid.png").convert("RGBA")
    
    #Methane Oceans
    if line[4] == "1" and line[1] == "1":
      liquid = Image.open("Methane Oceans (Blue).png").convert("RGBA")

    elif line[4] == "1" and line[1] == "2":
      liquid = Image.open("Methane Oceans (Green).png").convert("RGBA")

    elif line[4] == "1" and line[1] == "3":
      liquid = Image.open("Methane Oceans (Brown).png").convert("RGBA")

    elif line[4] == "1" and line[1] == "4":
      liquid = Image.open("Methane Oceans (Iron).png").convert("RGBA")

    elif line[4] == "1" and line[1] == "5":
      liquid = Image.open("Methane Oceans (Red).png").convert("RGBA")

    elif line[4] == "1" and line[1] == "6":
      liquid = Image.open("Methane Oceans (Yellow).png").convert("RGBA")

    elif line[4] == "1" and line[1] == "7":
      liquid = Image.open("Methane Oceans (Purple).png").convert("RGBA")

    #Methane Rivers
    elif line[4] == "2":
      liquid = Image.open("Methane Rivers.png").convert("RGBA")
        
    #Water Oceans
    elif line[4] == "3" and line[1] == "1":
      liquid = Image.open("Water Oceans (Blue).png").convert("RGBA")

    elif line[4] == "3" and line[1] == "2":
      liquid = Image.open("Water Oceans (Green).png").convert("RGBA")

    elif line[4] == "3" and line[1] == "3":
      liquid = Image.open("Water Oceans (Brown).png").convert("RGBA")

    elif line[4] == "3" and line[1] == "4":
      liquid = Image.open("Water Oceans (Iron).png").convert("RGBA")

    elif line[4] == "3" and line[1] == "5":
      liquid = Image.open("Water Oceans (Red).png").convert("RGBA")

    elif line[4] == "3" and line[1] == "6":
      liquid = Image.open("Water Oceans (Yellow).png").convert("RGBA")

    elif line[4] == "3" and line[1] == "7":
      liquid = Image.open("Water Oceans (Purple).png").convert("RGBA")
        
    #Water Rivers
    elif line[4] == "4":
      liquid = Image.open("Water Rivers.png").convert("RGBA")
      
    #Frozen Oceans
    elif line[4] == "5" and line[1] == "1":
      liquid = Image.open("Frozen Oceans (Blue).png").convert("RGBA")

    elif line[4] == "5" and line[1] == "2":
      liquid = Image.open("Frozen Oceans (Green).png").convert("RGBA")

    elif line[4] == "5" and line[1] == "3":
      liquid = Image.open("Frozen Oceans (Brown).png").convert("RGBA")

    elif line[4] == "5" and line[1] == "4":
      liquid = Image.open("Frozen Oceans (Iron).png").convert("RGBA")

    elif line[4] == "5" and line[1] == "5":
      liquid = Image.open("Frozen Oceans (Red).png").convert("RGBA")

    elif line[4] == "5" and line[1] == "6":
      liquid = Image.open("Frozen Oceans (Yellow).png").convert("RGBA")

    elif line[4] == "5" and line[1] == "7":
      liquid = Image.open("Frozen Oceans (Purple).png").convert("RGBA")
        
    #Frozen Rivers
    elif line[4] == "6":
      liquid = Image.open("Frozen Rivers.png").convert("RGBA")

    #Dry Oceans
    elif line[4] == "7" and line[1] == "1":
      liquid = Image.open("Dry Oceans (Blue).png").convert("RGBA")

    elif line[4] == "7" and line[1] == "2":
      liquid = Image.open("Dry Oceans (Green).png").convert("RGBA")

    elif line[4] == "7" and line[1] == "3":
      liquid = Image.open("Dry Oceans (Brown).png").convert("RGBA")

    elif line[4] == "7" and line[1] == "4":
      liquid = Image.open("Dry Oceans (Iron).png").convert("RGBA")

    elif line[4] == "7" and line[1] == "5":
      liquid = Image.open("Dry Oceans (Red).png").convert("RGBA")

    elif line[4] == "7" and line[1] == "6":
      liquid = Image.open("Dry Oceans (Yellow).png").convert("RGBA")

    elif line[4] == "7" and line[1] == "7":
      liquid = Image.open("Dry Oceans (Purple).png").convert("RGBA")
        
    #Dry Rivers
    elif line[4] == "8":
      liquid = Image.open("Dry Rivers.png").convert("RGBA")
        
    elif line[4] == "9":
      liquid = Image.open("No Liquid.png").convert("RGBA")
        
    #craters
    if line[5] == "0":
      crater = Image.open("No Crater.png").convert("RGBA")

    #Large Impact      
    if line[5] == "1" and line[1] == "1":
      crater = Image.open("Large Impact (Blue).png").convert("RGBA")

    elif line[5] == "1" and line[1] == "2":
      crater = Image.open("Large Impact (Green).png").convert("RGBA")

    elif line[5] == "1" and line[1] == "3":
      crater = Image.open("Large Impact (Brown).png").convert("RGBA")

    elif line[5] == "1" and line[1] == "4":
      crater = Image.open("Large Impact (Iron).png").convert("RGBA")

    elif line[5] == "1" and line[1] == "5":
      crater = Image.open("Large Impact (Red).png").convert("RGBA")

    elif line[5] == "1" and line[1] == "6":
      crater = Image.open("Large Impact (Yellow).png").convert("RGBA")

    elif line[5] == "1" and line[1] == "7":
      crater = Image.open("Large Impact (Purple).png").convert("RGBA")
        
    #Large Impact and Volcanic Caldera    
    elif line[5] == "2" and line[1] == "1":
      crater = Image.open("Large Impact and Volcanic Caldera (Blue).png").convert("RGBA")

    elif line[5] == "2" and line[1] == "2":
      crater = Image.open("Large Impact and Volcanic Caldera (Green).png").convert("RGBA")

    elif line[5] == "2" and line[1] == "3":
      crater = Image.open("Large Impact and Volcanic Caldera (Brown).png").convert("RGBA")

    elif line[5] == "2" and line[1] == "4":
      crater = Image.open("Large Impact and Volcanic Caldera (Iron).png").convert("RGBA")

    elif line[5] == "2" and line[1] == "5":
      crater = Image.open("Large Impact and Volcanic Caldera (Red).png").convert("RGBA")

    elif line[5] == "2" and line[1] == "6":
      crater = Image.open("Large Impact and Volcanic Caldera (Yellow).png").convert("RGBA")

    elif line[5] == "2" and line[1] == "7":
      crater = Image.open("Large Impact and Volcanic Caldera (Purple).png").convert("RGBA")
        
    #Large Impact and Volcanic Caldera    
    elif line[5] == "3" and line[1] == "1":
      crater = Image.open("Volcanic Caldera (Blue).png").convert("RGBA")

    elif line[5] == "3" and line[1] == "2":
      crater = Image.open("Volcanic Caldera (Green).png").convert("RGBA")

    elif line[5] == "3" and line[1] == "3":
      crater = Image.open("Volcanic Caldera (Brown).png").convert("RGBA")

    elif line[5] == "3" and line[1] == "4":
      crater = Image.open("Volcanic Caldera (Iron).png").convert("RGBA")

    elif line[5] == "3" and line[1] == "5":
      crater = Image.open("Volcanic Caldera (Red).png").convert("RGBA")

    elif line[5] == "3" and line[1] == "6":
      crater = Image.open("Volcanic Caldera (Yellow).png").convert("RGBA")

    elif line[5] == "3" and line[1] == "7":
      crater = Image.open("Volcanic Caldera (Purple).png").convert("RGBA")
      
    elif line[5] == "4":
      crater = Image.open("No Crater.png").convert("RGBA")
      
    #magma
    if line[6] == "0":
      magma = Image.open("No Magma.png").convert("RGBA")
    
    #magma Oceans
    if line[6] == "1" and line[1] == "1":
      magma = Image.open("Magma Oceans (Blue).png").convert("RGBA")

    elif line[6] == "1" and line[1] == "2":
      magma = Image.open("Magma Oceans (Green).png").convert("RGBA")

    elif line[6] == "1" and line[1] == "3":
      magma = Image.open("Magma Oceans (Brown).png").convert("RGBA")

    elif line[6] == "1" and line[1] == "4":
      magma = Image.open("Magma Oceans (Iron).png").convert("RGBA")

    elif line[6] == "1" and line[1] == "5":
      magma = Image.open("Magma Oceans (Red).png").convert("RGBA")

    elif line[6] == "1" and line[1] == "6":
      magma = Image.open("Magma Oceans (Yellow).png").convert("RGBA")

    elif line[6] == "1" and line[1] == "7":
      magma = Image.open("Magma Oceans (Purple).png").convert("RGBA")
        
    #magma Rivers
    elif line[6] == "2":
      magma = Image.open("Magma Rivers.png").convert("RGBA")

    elif line[6] == "3":
      magma = Image.open("No Magma.png").convert("RGBA")
      
    #volcano
    if line[7] == "0":
      volcano = Image.open("No Volcano.png").convert("RGBA")
      
    if line[7] == "1" and line[1] == "1":
      volcano = Image.open("Volcano (Blue).png").convert("RGBA")

    elif line[7] == "1" and line[1] == "2":
      volcano = Image.open("Volcano (Green).png").convert("RGBA")

    elif line[7] == "1" and line[1] == "3":
      volcano = Image.open("Volcano (Brown).png").convert("RGBA")

    elif line[7] == "1" and line[1] == "4":
      volcano = Image.open("Volcano (Iron).png").convert("RGBA")

    elif line[7] == "1" and line[1] == "5":
      volcano = Image.open("Volcano (Red).png").convert("RGBA")

    elif line[7] == "1" and line[1] == "6":
      volcano = Image.open("Volcano (Yellow).png").convert("RGBA")

    elif line[7] == "1" and line[1] == "7":
      volcano = Image.open("Volcano (Purple).png").convert("RGBA")
        
    elif line[7] == "2":
      volcano = Image.open("No Volcano.png").convert("RGBA")
      
    #clouds
    if line[8] == "1":
      clouds = Image.open("Veil Clouds (Water).png").convert("RGBA")

    elif line[8] == "0":
      clouds = Image.open("No Clouds.png").convert("RGBA")
        
    elif line[8] == "2":
      clouds = Image.open("Stratocumulus Clouds (Water).png").convert("RGBA")
        
    elif line[8] == "3":
      clouds = Image.open("Cumulus Clouds (Water).png").convert("RGBA")
       
    elif line[8] == "4":
      clouds = Image.open("No Moons.png").convert("RGBA")
      
    elif line[8] == "5":
      clouds = Image.open("Cumulus Clouds (Water).png").convert("RGBA")
        
    elif line[8] == "6":
      clouds = Image.open("Cumulus Clouds (Silicate).png").convert("RGBA")
        
    elif line[8] == "7":
      clouds = Image.open("Cumulus CLouds (Ammonia).png").convert("RGBA")
        
    elif line[8] == "8":
      clouds = Image.open("Cumulonimbus Clouds (Water).png").convert("RGBA")
        
    elif line[8] == "9":
      clouds = Image.open("Cumulonimbus Clouds (Silicate).png").convert("RGBA")
      
    elif line[8] == "k":
      clouds = Image.open("Cumulonimbus Clouds (Ammonia).png").convert("RGBA")
        
      
    #moons
    if line [9] == "0":
      moons = Image.open("No Moons.png").convert("RGBA")
    
    if line[9] == "1":
      moons = Image.open("One Moon Brown.png").convert("RGBA")
        
    elif line[9] == "2":
      moons = Image.open("One Moon Green.png").convert("RGBA")
       
    elif line[9] == "3":
      moons = Image.open("One Moon Iron.png").convert("RGBA")
      
    elif line[9] == "4":
      moons = Image.open("One Moon Blue.png").convert("RGBA")
        
    elif line[9] == "5":
      moons = Image.open("One Moon Red.png").convert("RGBA")
        
    elif line[9] == "6":
      moons = Image.open("Two Moons Brown.png").convert("RGBA")
        
    elif line[9] == "7":
      moons = Image.open("Two Moons Green.png").convert("RGBA")
        
    elif line[9] == "8":
      moons = Image.open("Two Moons Iron.png").convert("RGBA")
      
    elif line[9] == "9":
      moons = Image.open("Two Moons Blue.png").convert("RGBA")
        
    elif line[9] == "k":
      moons = Image.open("Two Moons Red.png").convert("RGBA")
      
    elif line[9] == "l":
      moons = Image.open("Two Moons Green and Brown.png").convert("RGBA")
      
    elif line[9] == "m":
      moons = Image.open("Two Moons Brown and Iron.png").convert("RGBA")
      
    elif line[9] == "n":
      moons = Image.open("Two Moons Brown and Blue.png").convert("RGBA")
      
    elif line[9] == "o":
      moons = Image.open("Two Moons Brown and Red.png").convert("RGBA")
      
    elif line[9] == "p":
      moons = Image.open("Two Moons Green and Iron.png").convert("RGBA")
      
    elif line[9] == "q":
      moons = Image.open("Two Moons Green and Blue.png").convert("RGBA")
      
    elif line[9] == "r":
      moons = Image.open("Two Moons Green and Red.png").convert("RGBA")
      
    elif line[9] == "s":
      moons = Image.open("Two Moons Iron and Blue.png").convert("RGBA")
      
    elif line[9] == "t":
      moons = Image.open("Two Moons Iron and Red.png").convert("RGBA")
      
    elif line[9] == "u":
      moons = Image.open("Two Moons Blue and Red.png").convert("RGBA")
      
    elif line[9] == "v":
      moons = Image.open("No Moons.png").convert("RGBA")
    
    #rings
    if line[10] == "0":
      rings = Image.open("No Rings.png").convert("RGBA")
      
    if line[10] == "1":
      rings = Image.open("One Ring Brown.png").convert("RGBA")
        
    elif line[10] == "2":
      rings = Image.open("One Ring Brown (Vertical).png").convert("RGBA")
       
    elif line[10] == "3":
      rings = Image.open("One Ring Iron.png").convert("RGBA")
      
    elif line[10] == "4":
      rings = Image.open("One Ring Iron (Vertical).png").convert("RGBA")
        
    elif line[10] == "5":
      rings = Image.open("One Ring Green.png").convert("RGBA")
        
    elif line[10] == "6":
      rings = Image.open("One Ring Green (Vertical).png").convert("RGBA")
        
    elif line[10] == "7":
      rings = Image.open("Two Rings Brown (One Vertical).png").convert("RGBA")
        
    elif line[10] == "8":
      rings = Image.open("Two Rings Iron (One Vertical).png").convert("RGBA")
      
    elif line[10] == "9":
      rings = Image.open("Two Rings Green (One Vertical).png").convert("RGBA")
        
    elif line[10] == "k":
      rings = Image.open("Two Rings Brown and Green (One Vertical).png").convert("RGBA")
      
    elif line[10] == "l":
      rings = Image.open("Two Rings Iron and Brown (One Vertical).png").convert("RGBA")
      
    elif line[10] == "m":
      rings = Image.open("Two Rings Green and Iron (One Vertical).png").convert("RGBA")
      
    elif line[10] == "n":
      rings = Image.open("No Rings.png").convert("RGBA")
      
    elif line[10] == "o":
      rings = Image.open("Two Rings Brown (45°).png").convert("RGBA")
      
    elif line[10] == "p":
      rings = Image.open("Two Rings Iron (45°).png").convert("RGBA")
      
    elif line[10] == "q":
      rings = Image.open("Two Rings Green (45°).png").convert("RGBA")
      
    elif line[10] == "r":
      rings = Image.open("Two Rings Green and Brown (45°).png").convert("RGBA")
      
    elif line[10] == "s":
      rings = Image.open("Two Rings Brown and Iron (45°).png").convert("RGBA")
      
    elif line[10] == "t":
      rings = Image.open("Two Rings Iron and Green (45°).png").convert("RGBA")

    
    base.paste(liquid, (0,0), liquid)
    base.paste(crater, (0,0), crater)
    base.paste(magma, (0,0), magma)
    base.paste(volcano, (0,0), volcano)
    base.paste(clouds, (0,0), clouds)
    base.paste(moons, (0,0), moons)
    base.paste(rings, (0,0), rings)
    
    
    base.save("AlgoPlanet" + str(count) + ".png")
    count+=1
      
   
       
    
