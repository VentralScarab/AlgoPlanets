with open("Unicode.txt", "r") as file:
    
    for line in file:
        
        n=1
        
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
            Color = "Black (Lava)"
        
        if line[0] == "5":
            Color = "Turquoise/Grey (Dwarf)"
            
        if line[0] == "6":
            Color = "Brown/Red (Moon Impact)"
            
        if line[1] == "1":
            Color = "Blue (Terrestrial)"
      
        elif line[1] == "2":
            Color = "Green (Terrestrial)"
        
        elif line[1] == "3":
            Color = "Brown (Terrestrial)"
        
        elif line[1] == "4":
            Color = "Iron (Terrestrial)"
        
        elif line[1] == "5":
            Color = "Red (Terrestrial)"
        
        elif line[1] == "6":
            Color = "Yellow (Terrestrial)"
        
        elif line[1] == "7":
            Color = "Purple (Terrestrial)"
            
        if line[2] == "1":
            Color = "Turquoise/Grey (Gas)"
      
        elif line[2] == "2":
            Color = "Purple/Sand (Gas)"
        
        elif line[2] == "3":
            Color = "Brown (Gas)"
        
        elif line[2] == "4":
            Color = "Red/Grey (Gas)"
            
        if line[3] == "1":
            Color = "Dark Blue (Ice Giant)"
      
        elif line[3] == "2":
            Color = "Icy White (Ice Giant)"
        
        elif line[3] == "3":
            Color = "Light Blue (Ice Giant)"
            
        
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
            Crater = "No Craters"
      
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
        if line[0] == "5":
            Clouds = "Dwarf Clouds"
            
        if line[8] == "1":
            Clouds = "Veil Clouds"

        elif line[8] == "2":
            Clouds = "Stratocumulus Clouds"

        elif line[8] == "3":
            Clouds = "Cumulus Clouds (Water)"

        elif line[8] == "4":
            Clouds = "No Clouds"

        elif line[8] == "5":
            Clouds = "Cumulus Clouds (Water)"

        elif line[8] == "6":
            Clouds = "Cumulus Clouds (Silicate)"

        elif line[8] == "7":
            Clouds = "Cumulus Clouds (Ammonia)"

        elif line[8] == "8":
            Clouds = "Cumulonimbus Clouds (Water)"

        elif line[8] == "9":
            Clouds = "Cumulonimbus Clouds (Silicate)"

        elif line[8] == "k":
            Clouds = "Cumulonimbus Clouds (Ammonia)"

        elif line[8] == "l":
            Clouds = "No Clouds"
        
        #Moons
        if line [0] == "5":
            Moons = "Two Moons Purple and Red"
            
        if line [9] == "0":
            Moons = "No Moons"

        elif line[9] == "1":
            Moons = "One Moon Brown"

        elif line[9] == "2":
            Moons = "One Moon Green"

        elif line[9] == "3":
            Moons = "One Moon Iron"

        elif line[9] == "4":
            Moons = "One Moon Blue"

        elif line[9] == "5":
            Moons = "One Moon Red"

        elif line[9] == "6":
            Moons = "Two Moons Brown"

        elif line[9] == "7":
            Moons = "Two Moons Green"

        elif line[9] == "8":
            Moons = "Two Moons Iron"

        elif line[9] == "9":
            Moons = "Two Moons Blue"

        elif line[9] == "k":
            Moons = "Two Moons Red"

        elif line[9] == "l":
            Moons = "Two Moons Brown and Green"

        elif line[9] == "m":
            Moons = "Two Moons Brown and Iron"

        elif line[9] == "n":
            Moons = "Two Moons Brown and Blue"

        elif line[9] == "o":
            Moons = "Two Moons Brown and Red"

        elif line[9] == "p":
            Moons = "Two Moons Green and Iron"

        elif line[9] == "q":
            Moons = "Two Moons Green and Blue"

        elif line[9] == "r":
            Moons = "Two Moons Green and Red"

        elif line[9] == "s":
            Moons = "Two Moons Iron and Blue"

        elif line[9] == "t":
            Moons = "Two Moons Iron and Red"

        elif line[9] == "u":
            Moons = "Two Moons Blue and Red"

        elif line[9] == "v":
            Moons = "No Moons"
            
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
            Rings = image.open("Two Rings Brown (One Vertical).png")

        elif line[10] == "8":
            Rings = image.open("Two Rings Iron (One Vertical).png")

        elif line[10] == "9":
            Rings = image.open("Two Rings Green (One Vertical).png")

        elif line[10] == "k":
            Rings = image.open("Two Rings Brown and Green (One Vertical).png")

        elif line[10] == "l":
            Rings = image.open("Two Rings Grey and Brown (One Vertical).png")

        elif line[10] == "m":
            Rings = image.open("Two Rings Green and Grey (One Vertical).png")

        elif line[10] == "n":
            Rings = image.open("No Rings.png")

        elif line[10] == "o":
            Rings = image.open("Two Rings Brown (45°).png")

        elif line[10] == "p":
            Rings = image.open("Two Rings Iron (45°).png")

        elif line[10] == "q":
            Rings = image.open("Two Rings Green (45°).png")

        elif line[10] == "r":
            Rings = image.open("Two Rings Brown and Green (45°).png")

        elif line[10] == "s":
            Rings = image.open("Two Rings Grey and Brown (45°).png")

        elif line[10] == "t":
            Rings = image.open("Two Rings Green and Grey (45°).png")

        elif line[10] == "u":
            Rings = image.open("No Rings.png")
            
        metadata = {   
                        '"standard"': '"arc69"',
                        '"description"': '"AlgoPlanet ' + n'"'
                        '"attributes"': [
                            {'"trait_type"':'"Type"',
                            '"value"':'"'Type'"'
                            },
                            {'"trait_type"':'"Color"',
                            '"value"':'"'Color'"'
                            },
                            {'"trait_type"':'"Liquid"',
                            '"value"':'"'Liquid'"'
                            },
                            {'"trait_type"':'"Crater"',
                            '"value"':'"'Crater'"'
                            },
                            {'"trait_type"':'"Volcano"',
                            '"value"':'"'Volcano'"'
                            },
                            {'"trait_type"':'"Clouds"',
                            '"value"':'"'Clouds'"'
                            },
                            {'"trait_type"':'"Moons"',
                            '"value"':'"'Moons'"'
                            },
                            {'"trait_type"':'"Rings"',
                            '"value"':'"'Rings'"'
                            }
                        ]
                    }
            
        with open("AlgoPlanetMetadata" + n + ".json", "r+") as f:
            f.write(metadata)
            n+=1
        f.close
