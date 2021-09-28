import random
i = 0
while i < 512:
    SolidGas = ["Terrestrial World","Gas Giant","Ice Giant", "Lava Planet", "Dwarf Planet", "Algo Planet", "Moon Impact"] 
    OddsSolidGas = [500,300,200,2,2,2,2] 
    SolidPlanets = ["Blue Terrestrial Planet", "Green Terrestrial Planet", "Brown Terrestrial Planet", "Iron Terrestrial Planet", "Red Terrestrial Planet", "Yellow Terrestrial Planet", "Purple Terrestrial Planet"] #Chance 1/7
    GasPlanets = ["Purple Gas Planet", "Brown Gas Planet", "Blue/Turquoise Gas Planet", "Red Gas Planet"] #Chance 1/4
    IceGiant = ["Dark Blue Planet", "Light Blue Planet", "Icy White Planet"] #Chance 1/3
    Water = ["Oceans", "River","Frozen Oceans", "Frozen Rivers", "Dry Oceans", "Dry Rivers", "Waterless"] 
    OddsWater = [17,25,9,11.5,2.25,3,32.25] 
    WaterAndMethane = ["Methane Oceans", "Methane River", "Oceans", "River","Frozen Oceans", "Frozen Rivers", "Dry Oceans", "Dry Rivers", "Waterless"]
    OddsWaterAndMethane = [8.5,11,17,25,9,11.5,2.25,3,12.75] 
    WaterBluePlanet = ["Dry Oceans", "Dry Rivers", "Waterless"]
    OddsWaterBluePlanet = [2.25,3,94.75]
    Clouds = ["Veil Water Clouds (White)", "Stratocumulus Water Clouds (White)","Cumulus Water Clouds (White)", "Cloudless"]
    OddsClouds = [20,10,35,55] 
    GasPlanetClouds = ["Cumulus Water Clouds (White)","Cumulus Silicate Clouds (Red)","Cumulus Ammonia Clouds (Orange)", "Storm Clouds (White)", "Storm Ammonia Clouds (Orange)", "Storm Silicate Clouds (Red)", "Cloudless"]
    OddsGasPlanetClouds = [35,20,10, 5, 2.5, 3, 27.5] 
    Moons = ["One Moon Brown", "One Moon Brown (Craters)", "One Moon Grey/Iron", "One Moon Grey/Iron (Craters)", "One Moon Red", "One Moon Red (Craters)","One Moon Green", "One Moon Green (Craters)", "One Moon Yellow", "One Moon Yellow (Craters)", "One Moon Blue", "One Moon Blue (Craters)", "Two Moons Yellow", "Two Moons Yellow (Craters)", "Two Moons Brown", "Two Moons Brown (Craters)", "Two Moons Blue", "Two Moons Blue (Craters)", "Two Moons Green", "Two Moons Green (Craters)", "Two Moons Red", "Two Moons Red (Craters)", "Two Moons Grey/Iron", "Two Moons Grey/Iron (Craters)", "Two Moons Yellow&Grey", "Two Moons Blue&Green","Two Moons Red&Grey", "Two Moons Brown&Green", "Two Moons Green&Red", "Two Moons Yellow&Blue", "Two Moons Yellow&Grey (Grey with Craters)", "Two Moons Blue&Green (Green with Craters)","Two Moons Red&Grey (Grey with Craters)", "Two Moons Brown&Green (Green with Craters)", "Two Moons Green&Red (Red with Craters)", "Two Moons Yellow&Blue (Blue with Craters)", "Two Moons Yellow&Grey (Yellow with Craters)", "Two Moons Blue&Green (Blue with Craters)","Two Moons Red&Grey (Red with Craters)", "Two Moons Brown&Green (Brown with Craters)", "Two Moons Green&Red (Green with Craters)", "Two Moons Yellow&Blue (Yellow with Craters)", "Two Moons Yellow&Grey (Craters)", "Two Moons Blue&Green(Craters)","Two Moons Red&Grey (Craters)", "Two Moons Brown&Green (Craters)", "Two Moons Green&Red (Craters)", "Two Moons Yellow&Blue (Craters)", "No Moons"]
    OddsMoons = [4,4,4,4,4,4,4,4,4,4,4,4,2.6,2.6,2.6,2.6,2.6,2.6,2.6,2.6,2.6,2.6,2.6,2.6,1.8,1.8,1.8,1.8,1.8,1.8,1,1,1,1,1,1,1,1,1,1,1,1,0.5,0.5,0.5,0.5,0.5,0.5,95] 
    Rings = ["One Brown Ring", "One Brown Ring Vertical", "One Black/Grey Ring", "One Black/Grey Ring Vertical", "One Green Ring", "One Green Ring Vertical", "Two Brown Rings One Vertical", "Two Black/Grey Rings One Vertical", "Two Green Rings One Vertical", "Two Brown&Green Rings One Vertical", "Two Grey & Brown Rings One Vertical", "Two Grey&Green Rings One Vertical", "No Rings"]
    OddsRings = [20,20,20,20,20,20,18,18,18,14,14,14,44]
    RingsWithNoMoon = ["Two Brown Rings(45°)", "Two Black/Grey Rings (45°)", "Two Green Rings (45°)", "Two Brown&Green Rings (45°)", "Two Grey&Brown Rings (45°)", "Two Grey&Green Rings (45°)", "No Rings"]
    OddsRingsWithNoMoon = [33,33,33,12,12,12,15] 
    Crater = ["Large Impact Crater", "Large Impact Crater & Volcanic Caldera Craters","Volcanic Caldera Craters", "No Craters"]
    OddsCrater = [31,9,52,8] 
    Volcano = ["Volcano", "No Volcano"]
    OddsVolcano = [13,5] 
    Magma = ["Magma Ocean", "Magma River", "No Magma"]
    OddsMagma = [50,75,25]
    Planet = []
    text = '# \n'

    #Terrastrial
    SolidGasDecide = random.choices(SolidGas, OddsSolidGas, k=1)
    Planet.append(SolidGasDecide)
    CheckSolid = random.choices(SolidPlanets)
    CheckGas = random.choices(GasPlanets)
    CheckIceGiant = random.choices(IceGiant)
    CheckWater = random.choices(Water, OddsWater, k=1)
    CheckWaterAndMethane = random.choices(WaterAndMethane, OddsWaterAndMethane, k=1)
    CheckWaterBluePlanet = random.choices(WaterBluePlanet, OddsWaterBluePlanet, k=1)
    CheckClouds = random.choices(Clouds, OddsClouds, k=1)
    CheckGasClouds = random.choices(GasPlanetClouds, OddsGasPlanetClouds, k=1)
    CheckMoons = random.choices(Moons, OddsMoons, k=1)
    CheckRings = random.choices(Rings, OddsRings, k=1)
    CheckRingsWithNoMoon = random.choices(RingsWithNoMoon, OddsRingsWithNoMoon, k=1)
    CheckVolcano = random.choices(Volcano, OddsVolcano, k=1)
    CheckCrater = random.choices(Crater, OddsCrater, k=1)
    CheckMagma = random.choices(Magma, OddsMagma, k=1)

    if SolidGasDecide == ["Terrestrial World"]:
        Planet.append(CheckSolid)
        if CheckSolid == ["Blue Terrestrial Planet"]:
            Planet.append(CheckWaterBluePlanet)
            if CheckWaterBluePlanet == ["Dry Oceans"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            elif CheckWaterBluePlanet == ["Dry Rivers"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
            
            else:
                Planet.append(CheckCrater)
                if CheckCrater == ["No Craters"]:
                    Planet.append(CheckMagma)
                    if CheckMagma == ["No Magma"]:
                        Planet.append(CheckVolcano)
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
        
        elif CheckSolid == ["Iron Terrestrial Planet"]:
            Planet.append(CheckWaterAndMethane)
            if CheckWaterAndMethane == ["Methane Oceans"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            elif CheckWaterAndMethane == ["Methane River"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            elif CheckWaterAndMethane == ["Oceans"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
        
            elif CheckWaterAndMethane == ["River"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            elif CheckWaterAndMethane == ["Frozen Oceans"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            elif CheckWaterAndMethane == ["Frozen Rivers"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            elif CheckWaterAndMethane == ["Dry Oceans"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            elif CheckWaterAndMethane == ["Dry Rivers"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            else:
                Planet.append(CheckCrater)
                if CheckCrater == ["No Craters"]:
                    Planet.append(CheckMagma)
                    if CheckMagma == ["No Magma"]:
                        Planet.append(CheckVolcano)
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                        
        elif CheckSolid == ["Yellow Terrestrial Planet"]:
            Planet.append(CheckWaterAndMethane)
            if CheckWaterAndMethane == ["Methane Oceans"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            elif CheckWaterAndMethane == ["Methane River"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            elif CheckWaterAndMethane == ["Oceans"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
        
            elif CheckWaterAndMethane == ["River"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            elif CheckWaterAndMethane == ["Frozen Oceans"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            elif CheckWaterAndMethane == ["Frozen Rivers"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            elif CheckWaterAndMethane == ["Dry Oceans"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            elif CheckWaterAndMethane == ["Dry Rivers"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            else:
                Planet.append(CheckCrater)
                if CheckCrater == ["No Craters"]:
                    Planet.append(CheckMagma)
                    if CheckMagma == ["No Magma"]:
                        Planet.append(CheckVolcano)
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                        
        elif CheckSolid == ["Purple Terrestrial Planet"]:
            Planet.append(CheckWaterAndMethane)
            if CheckWaterAndMethane == ["Methane Oceans"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            elif CheckWaterAndMethane == ["Methane River"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            elif CheckWaterAndMethane == ["Oceans"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
        
            elif CheckWaterAndMethane == ["River"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            elif CheckWaterAndMethane == ["Frozen Oceans"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            elif CheckWaterAndMethane == ["Frozen Rivers"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            elif CheckWaterAndMethane == ["Dry Oceans"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            elif CheckWaterAndMethane == ["Dry Rivers"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            else:
                Planet.append(CheckCrater)
                if CheckCrater == ["No Craters"]:
                    Planet.append(CheckMagma)
                    if CheckMagma == ["No Magma"]:
                        Planet.append(CheckVolcano)
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
            
        else:
            Planet.append(CheckWater)
            if CheckWater == ["Oceans"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            elif CheckWater == ["Frozen Oceans"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
           
            elif CheckWater == ["River"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
            
            elif CheckWater == ["Frozen Rivers"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            elif CheckWater == ["Dry Oceans"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
                
            elif CheckWater == ["Dry Rivers"]:
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)
            
            else:
                Planet.append(CheckCrater)
                if CheckCrater == ["No Craters"]:
                    Planet.append(CheckMagma)
                    if CheckMagma == ["No Magma"]:
                        Planet.append(CheckVolcano)
                Planet.append(CheckClouds)
                Planet.append(CheckMoons)

    #Gas
    if SolidGasDecide == ["Gas Giant"]:
        Planet.append(CheckGas)
        Planet.append(CheckGasClouds)
        Planet.append(CheckMoons)
        if CheckMoons == ["No Moons"]:
            CheckRings
            if CheckRings == ["No Rings"]:
                Planet.append(CheckRingsWithNoMoon)
            else:
                Planet.append(CheckRings)
        else:
            Planet.append(CheckRings)
        
        
    #IceGiant
    if SolidGasDecide == ["Ice Giant"]:
        Planet.append(CheckIceGiant)
        Planet.append(CheckGasClouds)
        Planet.append(CheckMoons)
        if CheckMoons == ["No Moons"]:
            CheckRings
            if CheckRings == ["No Rings"]:
                Planet.append(CheckRingsWithNoMoon)
            else:
                Planet.append(CheckRings)
        else:
            Planet.append(CheckRings)

    for Element in Planet:
        text = text + ('\n').join(Element) + "\n"

    #Unicode

    Convert = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    AllClouds = Clouds + GasPlanetClouds
    Digits = [SolidGas,SolidPlanets,GasPlanets,IceGiant,WaterAndMethane,Crater,Magma,Volcano,AllClouds,Moons,RingsWithNoMoon] 
    Unicode = ''
    for Digit in Digits:
        found = False
        for List in Planet:
            for Element in List:
                if Element in Digit:
                    code =  (Digit.index(Element)) + 1
                    if code > 9:
                        code = Convert[code]
                    found = True
        if found == False:
            code = 0       
        Unicode = Unicode + str(code)
    test = '20300000416'
    text = text + '\n' + Unicode + '\n#\n'

    with open('AlgoPlanet.txt', 'r+') as f:
        if test not in f.read():
            f.write(text)
    f.close
    i += 1
