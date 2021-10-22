import random
i = 0
while i < 512:
    SolidGas = ["Terrestrial World","Gas Giant","Ice Giant", "Lava Planet", "Dwarf Planet", "Moon Impact"] 
    OddsSolidGas = [500,300,200,2,2,2] 
    SolidPlanets = ["Blue Terrestrial Planet", "Green Terrestrial Planet", "Brown Terrestrial Planet", "Iron Terrestrial Planet", "Red Terrestrial Planet", "Yellow Terrestrial Planet", "Purple Terrestrial Planet"] #Chance 1/7
    GasPlanets = ["Purple Gas Planet", "Brown Gas Planet", "Blue/Turquoise Gas Planet", "Red Gas Planet"] #Chance 1/4
    IceGiant = ["Dark Blue Planet", "Light Blue Planet", "Icy White Planet"] #Chance 1/3
    Water = ["Oceans", "River","Frozen Oceans", "Frozen Rivers", "Dry Oceans", "Dry Rivers", "Waterless"] 
    OddsWater = [70,100,20,25,1.5,2,75] 
    WaterAndMethane = ["Methane Oceans", "Methane River", "Oceans", "River","Frozen Oceans", "Frozen Rivers", "Dry Oceans", "Dry Rivers", "Waterless"]
    OddsWaterAndMethane = [10,14,45,65,15,20,1.5,2,60] 
    WaterBluePlanet = ["Dry Oceans", "Dry Rivers", "Waterless"]
    OddsWaterBluePlanet = [1.5,2,120]
    Clouds = ["Veil Water Clouds (White)", "Stratocumulus Water Clouds (White)","Cumulus Water Clouds (White)", "Cloudless"]
    OddsClouds = [30,15,40,160] 
    GasPlanetClouds = ["Cumulus Water Clouds (White)","Cumulus Silicate Clouds (Red)","Cumulus Ammonia Clouds (Orange)", "Storm Clouds (White)", "Storm Silicate Clouds (Red)", "Storm Ammonia Clouds (Orange)", "Cloudless"]
    OddsGasPlanetClouds = [20,10,10, 2.5, 1, 1, 75] 
    Moons = ["One Moon Brown", "One Moon Grey/Iron", "One Moon Green", "One Moon Blue", "One Moon Red", "Two Moons Brown", "Two Moons Green", "Two Moons Grey/Iron", "Two Moons Blue", "Two Moons Red", "Two Moons Brown&Green", "Two Moons Brown&Grey", "Two Moons Brown&Blue", "Two Moons Brown&Red", "Two Moons Green&Grey", "Two Moons Green&Blue", "Two Moons Green&Red", "Two Moons Grey&Blue", "Two Moons Grey&Red", "Two Moons Blue&Red", "No Moons"]
    OddsMoons = [1,1,1,1,1,1,0.5,0.5,0.5,0.5,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,140] 
    Rings = ["One Brown Ring", "One Brown Ring Vertical", "One Black/Grey Ring", "One Black/Grey Ring Vertical", "One Green Ring", "One Green Ring Vertical", "Two Brown Rings One Vertical", "Two Black/Grey Rings One Vertical", "Two Green Rings One Vertical", "Two Brown&Green Rings One Vertical", "Two Grey & Brown Rings One Vertical", "Two Grey&Green Rings One Vertical", "No Rings"]
    OddsRings = [15,15,15,15,15,15,2,2,2,1,1,1,100]
    RingsWithNoMoon = ["Two Brown Rings(45°)", "Two Black/Grey Rings (45°)", "Two Green Rings (45°)", "Two Brown&Green Rings (45°)", "Two Grey&Brown Rings (45°)", "Two Grey&Green Rings (45°)", "No Rings"]
    OddsRingsWithNoMoon = [0.8,0.8,0.8,0.3,0.3,0.3,120] 
    Crater = ["Large Impact Crater", "Large Impact Crater & Volcanic Caldera Craters","Volcanic Caldera Craters", "No Craters"]
    OddsCrater = [7.5,4,20,100] 
    Volcano = ["Volcano", "No Volcano"]
    OddsVolcano = [2,150] 
    Magma = ["Magma Ocean", "Magma River", "No Magma"]
    OddsMagma = [3,7,150]
    Planet = []
    text = ''

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
    AllRings = Rings + RingsWithNoMoon
    Digits = [SolidGas,SolidPlanets,GasPlanets,IceGiant,WaterAndMethane,Crater,Magma,Volcano,AllClouds,Moons,AllRings] 
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
    text =text + Unicode + '\n'

    with open('AlgoPlanet.txt', 'r+') as f:
        if Unicode not in f.read():
            f.write(text)
            i += 1

    text2 = Unicode + '\n'

    with open('AlgoPlanet_Unicode.txt', 'r+') as f2:
        if Unicode not in f2.read():
            f2.write(text2)
    f.close
