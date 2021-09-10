import random
SolidGas = ["Terrestrial World","Gas Giant","Ice Giant"] 
OddsSolidGas = [5,3,2] 
SolidPlanets = ["Blue Planet", "Green Planet", "Brown Planet", "Iron Planet", "Red Planet", "Yellow Planet", "Purple Planet"] 
GasPlanets = ["Purple Planet", "Brown Planet", "Blue/Turquoise Planet", "Red Planet", "Yellow  Planet"] 
IceGiant = ["Dark Blue Planet", "Light Blue Planet", "Icy White Planet"]
Water = ["Oceans", "River","Frozen Oceans", "Frozen Rivers", "Dry Oceans", "Dry Rivers", "Waterless"] 
OddsWater = [4,6,3,5,1,2,14] 
WaterAndMethane = ["Methane Oceans", "Methane River", "Oceans", "River","Frozen Oceans", "Frozen Rivers", "Dry Oceans", "Dry Rivers", "Waterless"]
OddsWaterAndMethane = [4,6,4,6,3,5,1,2,20]
WaterBluePlanet = ["Dry Oceans", "Dry Rivers", "Waterless"]
OddsWaterBluePlanet = [1,2,7]
Clouds = ["Veil Water Clouds (White)", "Stratocumulus Water Clouds (White)","Cumulus Water Clouds (White)", "Cloudless"]
OddsClouds = [2,3,1,6] 
GasPlanetClouds = ["Cumulus Water Clouds (White)","Cumulus Silicate Clouds (Red)","Cumulus Ammonia Clouds (Orange)", "Hurricane Clouds (White)", "Hurricane Ammonia Clouds (Orange)", "Cloudless"]
OddsGasPlanetClouds = [20,15,12, 10, 5, 50] 
Moons = ["One Moon Brown", "One Moon Grey/Iron", "One Moon Red", "One Moon Green", "One Moon Yellow", "One Moon Blue", "Two Moons Yellow", "Two Moons Brown", "Two Moons Blue", "Two Moons Green", "Two Moons Red","Two Moons Grey/Iron", "Two Moons Yellow&Grey", "Two Moons Blue&Green","Two Moons Red&Grey", "Two Moons Brown&Green", "Two Moons Green&Red", "Two Moons Yellow&Blue","No Moons"]
OddsMoons = [5,5,5,5,5,5,3,3,3,3,3,3,1,1,1,1,1,1,26] 
Rings = ["One Brown Ring", "One Brown Ring Vertical","One Black/Grey Ring", "One Black/Grey Ring Vertical", "One Green Ring", "One Green Ring Vertical", "Two Brown Rings", "Two Brown Rings One Vertical", "Two Black/Grey Rings", "Two Black/Grey Rings One Vertical", "Two Green Rings", "Two Green Rings One Vertical", "Two Brown&Green Rings", "Two Brown&Green Rings One Vertical", "Two Grey & Brown Rings", "Two Grey & Brown Rings One Vertical", "Two Grey&Green Rings", "Two Grey&Green Rings One Vertical", "No Rings"]
OddsRings = [9,7,9,7,9,7,5,3,5,3,5,3,2,1,2,1,2,1,47] 
RingsWithMoon = ["One Brown Ring", "One Brown Ring Vertical","One Black/Grey Ring", "One Black/Grey Ring Vertical", "One Green Ring", "One Green Ring Vertical", "Two Brown Rings One Vertical", "Two Black/Grey Rings One Vertical", "Two Green Rings One Vertical", "Two Brown&Green Rings One Vertical", "Two Grey & Brown Rings One Vertical", "Two Grey&Green Rings One Vertical", "No Rings"]
OddsRingsWithMoon = [8,6,8,6,8,6,4,4,4,2,2,2,10] 
Crater = ["Large Impact Crater", "Large Impace Crater & Volcanic Caldera Craters","Volcanic Calddera Craters", "No Craters"]
OddsCrater = [5,3,10,12] 
Volcano = ["Volcano", "No Volcano"]
OddsVolcano = [1,14] 
Magma = ["Magma Ocean", "Magma River", "No Magma"]
OddsMagma = [2,3,38]

#Terrastrial
SolidGasDecide = random.choices(SolidGas, OddsSolidGas, k=1)
print(SolidGasDecide)
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
CheckRingsWithMoon = random.choices(RingsWithMoon, OddsRingsWithMoon, k=1)
CheckVolcano = random.choices(Volcano, OddsVolcano, k=1)
CheckCrater = random.choices(Crater, OddsCrater, k=1)
CheckMagma = random.choices(Magma, OddsMagma, k=1)

if SolidGasDecide == ["Terrestrial World"]:
    print (CheckSolid)
    if CheckSolid == ["Blue Planet"]:
        print (CheckWaterBluePlanet)
        print (CheckClouds)
        print (CheckMoons)
        print (CheckCrater)
        if CheckCrater == ["No Craters"]:
            print (CheckMagma)
            if CheckMagma == ["No Magma"]:
                print (CheckVolcano)
                
    elif CheckSolid == ["Iron Planet"]:
        print (CheckWaterAndMethane)
        if CheckWaterAndMethane == ["Methane Oceans"]:
            print (CheckClouds)
            print (CheckMoons)
            
        elif CheckWaterAndMethane == ["Methane River"]:
            print (CheckClouds)
            print (CheckMoons)
            
        elif CheckWaterAndMethane == ["Oceans"]:
            print (CheckClouds)
            print (CheckMoons)
    
        elif CheckWaterAndMethane == ["River"]:
            print (CheckClouds)
            print (CheckMoons)
            
        elif CheckWaterAndMethane == ["Frozen Oceans"]:
            print (CheckClouds)
            print (CheckMoons)
            
        elif CheckWaterAndMethane == ["Frozen Rivers"]:
            print (CheckClouds)
            print (CheckMoons)
            
        elif CheckWaterAndMethane == ["Dry Oceans"]:
            print (CheckClouds)
            print (CheckMoons)
            
        elif CheckWaterAndMethane == ["Dry Rivers"]:
            print (CheckClouds)
            print (CheckMoons)
            
        else:
            print (CheckClouds)
            print (CheckCrater)
            print (CheckMoons)
            if CheckCrater == ["No Craters"]:
                print (CheckMagma)
                if CheckMagma == ["No Magma"]:
                    print (CheckVolcano)
                    
    elif CheckSolid == ["Yellow Planet"]:
        print (CheckWaterAndMethane)
        if CheckWaterAndMethane == ["Methane Oceans"]:
            print (CheckClouds)
            print (CheckMoons)
            
        elif CheckWaterAndMethane == ["Methane River"]:
            print (CheckClouds)
            print (CheckMoons)
            
        elif CheckWaterAndMethane == ["Oceans"]:
            print (CheckClouds)
            print (CheckMoons)
    
        elif CheckWaterAndMethane == ["River"]:
            print (CheckClouds)
            print (CheckMoons)
            
        elif CheckWaterAndMethane == ["Frozen Oceans"]:
            print (CheckClouds)
            print (CheckMoons)
            
        elif CheckWaterAndMethane == ["Frozen Rivers"]:
            print (CheckClouds)
            print (CheckMoons)
            
        elif CheckWaterAndMethane == ["Dry Oceans"]:
            print (CheckClouds)
            print (CheckMoons)
            
        elif CheckWaterAndMethane == ["Dry Rivers"]:
            print (CheckClouds)
            print (CheckMoons)
            
        else:
            print (CheckClouds)
            print (CheckCrater)
            print (CheckMoons)
            if CheckCrater == ["No Craters"]:
                print (CheckMagma)
                if CheckMagma == ["No Magma"]:
                    print (CheckVolcano)
                    
    elif CheckSolid == ["Purple Planet"]:
        print (CheckWaterAndMethane)
        if CheckWaterAndMethane == ["Methane Oceans"]:
            print (CheckClouds)
            print (CheckMoons)
            
        elif CheckWaterAndMethane == ["Methane River"]:
            print (CheckClouds)
            print (CheckMoons)
            
        elif CheckWaterAndMethane == ["Oceans"]:
            print (CheckClouds)
            print (CheckMoons)
    
        elif CheckWaterAndMethane == ["River"]:
            print (CheckClouds)
            print (CheckMoons)
            
        elif CheckWaterAndMethane == ["Frozen Oceans"]:
            print (CheckClouds)
            print (CheckMoons)
            
        elif CheckWaterAndMethane == ["Frozen Rivers"]:
            print (CheckClouds)
            print (CheckMoons)
            
        elif CheckWaterAndMethane == ["Dry Oceans"]:
            print (CheckClouds)
            print (CheckMoons)
            
        elif CheckWaterAndMethane == ["Dry Rivers"]:
            print (CheckClouds)
            print (CheckMoons)
            
        else:
            print (CheckClouds)
            print (CheckCrater)
            print (CheckMoons)
            if CheckCrater == ["No Craters"]:
                print (CheckMagma)
                if CheckMagma == ["No Magma"]:
                    print (CheckVolcano)
    
    else:
        print (CheckWater)
        if CheckWater == ["Oceans"]:
            print (CheckClouds)
            print (CheckMoons)
            
        elif CheckWater == ["Frozen Oceans"]:
            print (CheckClouds)
            print (CheckMoons)
       
        elif CheckWater == ["River"]:
            print (CheckClouds)
            print (CheckMoons)
        
        elif CheckWater == ["Frozen Rivers"]:
            print (CheckClouds)
            print (CheckMoons)
            
        elif CheckWater == ["Dry Oceans"]:
            print (CheckClouds)
            print (CheckMoons)
            
        elif CheckWater == ["Dry Rivers"]:
            print (CheckClouds)
            print (CheckMoons)
        
        else:
            print (CheckClouds)
            print (CheckCrater)
            print (CheckMoons)
            if CheckCrater == ["No Craters"]:
                print (CheckMagma)
                if CheckMagma == ["No Magma"]:
                    print (CheckVolcano)

#Gas
if SolidGasDecide == ["Gas Giant"]:
    print (CheckGas)
    print (CheckGasClouds)
    print (CheckMoons)
    if CheckMoons == ["No Moons"]:
        print (CheckRings)
    else:
        print (CheckRingsWithMoon)
    
    
#IceGiant
if SolidGasDecide == ["Ice Giant"]:
    print (CheckIceGiant)
    print (CheckGasClouds)
    print (CheckMoons)
    if CheckMoons == ["No Moons"]:
        print (CheckRings)
    else:
        print (CheckRingsWithMoon)

