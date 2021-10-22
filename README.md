# AlgoPlanets

AlgoPlanets is a NFT collection of randomly generated pixel-art planets with different attributes. Each piece of the collection is generated using a self-written python script.

Each attribute has a different probability of getting picked. Attributes are partly based on astronomy and partly not. Based on the randomly drawn attributes, the planet is categorized as Common, Rare, Super Rare, Ultra Rare und Secret Rare. A detailed list of all attributes and there possibilities can be seen on our website: www.algoplanets.com. 
Every planet will be a unique NFT (actually 1/1) and will have a resolution of 80x80. 

## How To Use

In the [Randomly-Generated-Planet.py](https://github.com/VentralScarab/AlgoPlanets/blob/main/Randomly-Generated-Planet.py) a list of 512 unique Planets is generated. Two .txt-files are generated, one stating all the Traits listed below each other and another with a Unicode, which is given to each generated AlgoPlanet. The Unicode will be used to check if an AlgoPlanet has already been generated and is also used later in the process to generate the images of each NFT and the .json metadata file. 

### Disclaimer

If you want to use this script for your own project I would recommend simplifying the script. You can safe yourself a lot of time and work if you first up finish all the different layers (images). Then you can use the images to directly randomly generate the NFT by adding weights to them. Depending on the size of your project you can also forego the Unicode-part, if the probabilities of each attribute are "rare enough". I ended up with so many different scripts as it was a work-in-progress and I was doing everything simultaneously.

Feel free to hit me up on Twitter or Discord if you got questions!

*Not the "prettiest" scripts but they will do the job*
