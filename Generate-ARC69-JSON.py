with open('AlgoPlanet_Unicode.txt', 'r') as file:
    
    count=1

    for line in file:
        
        
        Type = ""
        Color = ""
        Liquid = ""
        Clouds = ""
        Crater = ""
        Magma = ""
        Volcano = ""
        Moons = ""
        Rings = ""
        
        #Type
        if line[0] == "1":
            Type = "Terrestrial Planet"
        
        elif line[0] == "2":
            Type = "Gas Planet"
        
        elif line[0] == "3":
            Type = "Ice Giant Planet"
            
        elif line[0] == "4":
            Type = "Lava Planet"
            
        elif line[0] == "5":
            Type = "Dwarf Planet"
            
        elif line[0] == "6":
            Type = "Moon Impact Planet"
        
        
        #Color
        if line[0] == "4":
            Color = "Black"
        
        if line[0] == "5":
            Color = "Blue/White"
            
        if line[0] == "6":
            Color = "Brown/Red"
            
        if line[1] == "1":
            Color = "Blue"
      
        elif line[1] == "2":
            Color = "Green"
        
        elif line[1] == "3":
            Color = "Brown"
        
        elif line[1] == "4":
            Color = "Iron"
        
        elif line[1] == "5":
            Color = "Red"
        
        elif line[1] == "6":
            Color = "Yellow"
        
        elif line[1] == "7":
            Color = "Purple"
            
        if line[2] == "1":
            Color = "Purple/Sand"
      
        elif line[2] == "2":
            Color = "Turquoise/Grey"
        
        elif line[2] == "3":
            Color = "Brown/Green"
        
        elif line[2] == "4":
            Color = "Red/Sage"
            
        if line[3] == "1":
            Color = "Dark Blue"
      
        elif line[3] == "2":
            Color = "Icy White"
        
        elif line[3] == "3":
            Color = "Light Blue"
            
        
        #Liquid
        if line [0] == "4":
            Liquid == "Lava Flows"
            
        if line[4] == "0":
            Liquid = "No Liquid"

        elif line[4] == "1":
            Liquid = "Methane Oceans"

        elif line[4] == "2":
            Liquid = "Methane Rivers"

        elif line[4] == "3":
            Liquid = "Water Oceans"

        elif line[4] == "4":
            Liquid = "Water Rivers"

        elif line[4] == "5":
            Liquid = "Frozen Oceans"

        elif line[4] == "6":
            Liquid = "Frozen Rivers"

        elif line[4] == "7":
            Liquid = "Dry Oceans"

        elif line[4] == "8":
            Liquid = "Dry Rivers"

        elif line[4] == "9":
            Liquid = "No Liquid"
      
        elif line[6] == "1":
            Liquid = "Magma Oceans"
        
        elif line[6] == "2":
            Liquid = "Magma Rivers"
            
        #Craters
        if line[0] == "6":
            Crater = "Cracks"
            
        if line[5] == "0":
            Crater = "No Crater"
      
        elif line[5] == "1":
            Crater = "Large Impact"
        
        elif line[5] == "2":
            Crater = "Large Impact and Volcanic Caldera"
        
        elif line[5] == "3":
            Crater = "Volcanic Caldera"
      
        elif line[5] == "4":
            Crater = "No Crater"
            
        #Volcano
        if line[7] == "0":
            Volcano = "No Volcano"
      
        elif line[7] == "1":
            Volcano = "Volcano"
        
        elif line[7] == "2":
            Volcano = "No Volcano"
            
        #Clouds   
        if line[8] == "1":
            Clouds = "Veil Clouds (Water)"

        elif line[8] == "2":
            Clouds = "Stratocumulus Clouds (Water)"

        elif line[8] == "3":
            Clouds = "Cumulus Clouds (Water)"

        elif line[8] == "4":
            Clouds = "No Clouds"

        elif line[8] == "5":
            Clouds = "Cumulus Clouds (Water)"

        elif line[8] == "6":
            Clouds = "Cumulus Clouds (Ammonia)"

        elif line[8] == "7":
            Clouds = "Cumulus Clouds (Silicate)"

        elif line[8] == "8":
            Clouds = "Cumulonimbus Clouds (Water)"

        elif line[8] == "9":
            Clouds = "Cumulonimbus Clouds (Ammonia)"

        elif line[8] == "k":
            Clouds = "Cumulonimbus Clouds (Silicate)"

        elif line[8] == "l":
            Clouds = "No Clouds"

        elif line[8] == "0":
            Clouds = "No Clouds"
        
        #Moons
        if line [0] == "5":
            Moons = "Three Purple, Red and Brown Moons"
            
        if line [9] == "0":
            Moons = "No Moons"

        elif line[9] == "1":
            Moons = "One Brown Moon"

        elif line[9] == "2":
            Moons = "One Green Moon"

        elif line[9] == "3":
            Moons = "One Iron Moon"

        elif line[9] == "4":
            Moons = "One Blue Moon"

        elif line[9] == "5":
            Moons = "One Red Moon"

        elif line[9] == "6":
            Moons = "Two Brown Moons"

        elif line[9] == "7":
            Moons = "Two Green Moons"

        elif line[9] == "8":
            Moons = "Two Iron Moons"

        elif line[9] == "9":
            Moons = "Two Blue Moons"

        elif line[9] == "k":
            Moons = "Two Red Moons"

        elif line[9] == "l":
            Moons = "Two Brown and Green Moons"

        elif line[9] == "m":
            Moons = "Two Brown and Iron Moons"

        elif line[9] == "n":
            Moons = "Two Brown and Blue Moons"

        elif line[9] == "o":
            Moons = "Two Brown and Red Moons"

        elif line[9] == "p":
            Moons = "Two Green and Iron Moons"

        elif line[9] == "q":
            Moons = "Two Green and Blue Moons"

        elif line[9] == "r":
            Moons = "Two Green and Red Moons"

        elif line[9] == "s":
            Moons = "Two Iron and Blue Moons"

        elif line[9] == "t":
            Moons = "Two Iron and Red Moons"

        elif line[9] == "u":
            Moons = "Two Blue and Red Moons"

        elif line[9] == "v":
            Moons = "No Moons"
            
        #Rings
        if line[10] == "0":
            Rings = "No Rings"

        elif line[10] == "1":
            Rings = "One Brown Ring"

        elif line[10] == "2":
            Rings = "One Brown Ring (Vertical)"

        elif line[10] == "3":
            Rings = "One Iron Ring"

        elif line[10] == "4":
            Rings = "One Iron Ring (Vertical)"

        elif line[10] == "5":
            Rings = "One Green Ring"

        elif line[10] == "6":
            Rings = "One Green Ring (Vertical)"

        elif line[10] == "7":
            Rings = "Two Brown Rings (One Vertical)"

        elif line[10] == "8":
            Rings = "Two Iron Rings (One Vertical)"

        elif line[10] == "9":
            Rings = "Two Green Rings (One Vertical)"

        elif line[10] == "k":
            Rings = "Two Brown and Green Rings (One Vertical)"

        elif line[10] == "l":
            Rings = "Two Iron and Brown Rings (One Vertical)"

        elif line[10] == "m":
            Rings = "Two Green and Iron Rings (One Vertical)"

        elif line[10] == "n":
            Rings = "No Rings"

        elif line[10] == "o":
            Rings = ("Two Brown Rings (45°)")

        elif line[10] == "p":
            Rings = ("Two Iron Rings (45°)")

        elif line[10] == "q":
            Rings = ("Two Green Rings (45°)")

        elif line[10] == "r":
            Rings = ("Two Brown and Green Rings (45°)")

        elif line[10] == "s":
            Rings = ("Two Grey and Brown Rings (45°)")

        elif line[10] == "t":
            Rings = ("Two Green and Grey Rings (45°)")

        elif line[10] == "u":
            Rings = ("No Rings")
        
        indent = '    '

        metadata2 = '{' + '\n' + indent + '"standard": "arc69",' + '\n' + indent + '"description": "AlgoPlanet ' + str(count) + '",' + '\n' + indent + '"attributes": [' + '\n' + indent + indent + '{"trait_type":"Type",' + '\n' + indent + indent + '"value":"' + Type +'"' + '\n' + indent + indent + '},' + '\n' + indent + indent + '{"trait_type":"Color",' + '\n' + indent + indent + '"value":"' + Color +'"' + '\n' + indent + indent + '},' + '\n' + indent + indent + '{"trait_type":"Liquid",' + '\n' + indent + indent + '"value":"' + Liquid +'"' + '\n' + indent + indent + '},' + '\n' + indent + indent + '{"trait_type":"Crater",' + '\n' + indent + indent + '"value":"' + Crater +'"' + '\n' + indent + indent + '},' + '\n' + indent + indent + '{"trait_type":"Volcano",' + '\n' + indent + indent + '"value":"' + Volcano +'"' + '\n' + indent + indent + '},' + '\n' + indent + indent + '{"trait_type":"Clouds",' + '\n' + indent + indent + '"value":"' + Clouds +'"' + '\n' + indent + indent + '},' + '\n' + indent + indent + '{"trait_type":"Moons",' + '\n' + indent + indent + '"value":"' + Moons +'"' + '\n' + indent + indent + '},' + '\n' + indent + indent + '{"trait_type":"Rings",' + '\n' + indent + indent + '"value":"' + Rings +'"' + '\n' + indent + indent + '},' + '\n' + indent + ']' + '\n' + '}'
            
        with open("AlgoPlanetMetadata" + str(count) + ".json", "w+") as f:
            f.write(metadata2)
            count+=1
    f.close
