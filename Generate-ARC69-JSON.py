with open("Unicode.txt", "r") as file:
    
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
