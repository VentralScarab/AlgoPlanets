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
    
    #Rings
    
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
      
   
       
    
