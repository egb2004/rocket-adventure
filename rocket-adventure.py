import time

#an inventory, which has the map
inventory = ["map"]
backpackInventoryMax = 8
canFixRocket = False
rocketFixed = False
x = True

#start the player in the Grassy Field
currentPlace = 'Grassy Field'

#a dictionary linking a place to other places
places = {

            'Grassy Field' : { 
                  'north' : 'Crater',
                  'west' : 'Storage Facility'
                },

            'Crater' : {
                  'north' : 'River',
                  'south' : 'Grassy Field', 
                  'east' : 'Forest',
                  'west' : 'Deserted Town',
                  'item' : 'rocks'
                },
                
            'Forest' : {
                  'north' : 'Lab Center',
                  'west' : 'Crater',
                  'item' : 'tools'
                },
            'River' : {
                  'north' : 'Rocket',
                  'south' : 'Crater',
                  'east' : 'Lab Center',
                  'west' : 'Mines',
                  'item' : 'gemstones'
                },
            'Storage Facility' : {
                  'north' : 'Deserted Town',
                  'east' : 'Grassy Field',
                  'item' : 'battery'
                },
            'Deserted Town' : {
                  'north' : 'Mines',
                  'south' : 'Storage Facility',
                  'east' : 'Crater',
                  'item' : 'backpack'
                },
            'Mines' : {
                  'south' : 'Deserted Town',
                  'east' : 'River',
                  'item' : 'titanium'
                },
            'Lab Center' : { 
                  'south' : 'Forest',
                  'west' : 'River',
                  'item' : 'fuel'
                },
            'Rocket' : {
                  'south' : 'River'
                },
            'Launch Zone' : {
                  'south' : 'Rocket'
                }
         }

def showInstructions():
  #print a main menu and the commands
  print('''
Adventure Game
========
Commands:
  go [north, south, east, west]
  get [item]
''')

def showStatus():
  #print the player's current status
  print('======================================================')
  print('''Map:
----------------------------------------------------
|                        Rocket                    |
|                          |                       |  
|  Mines —--------------- River —----- Lab Center  |
|    |                     |               |       |    
|  Deserted Town —------- Crater —------ Forest    |
|    |                     |                       |
|  Storage Facility —-- Grassy Field               | 
----------------------------------------------------
''')
  print('You are in the ' + currentPlace)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in places[currentPlace]:
    print('You see ' + places[currentPlace]['item'])
    helpfulHints()
        
  print("======================================================")

#Checks to see if you have the backpack to carry more items
def canCarry(inventory):
    def haveBackpack():
        for i in range(len(inventory)):
            if inventory[i] == 'backpack':
                return True
    print(inventory)
    #checks to see if player has backpack in inventory
    if haveBackpack():
        print("You have the backpack!")
        if len(inventory) <= backpackInventoryMax:
            return True
        else:
            return False
    else:
        if len(inventory) == 0:
            return True
        else:
            return False
#Checks to see if you have all the parts in order to fix the rocket.
def checkallParts():
    count = 0
    for i in range(len(inventory)):
        if inventory[i] == 'tools':
            count += 1
        if inventory[i] == 'battery':
            count += 1
        if inventory[i] == 'titanium':
            count += 1
        if inventory[i] == 'fuel':
            count += 1
    if count == 4:
        return True
        print("You have all the items necessary to fix the Rocket!")
    else:
        return False 
        print("You do not have all the necessary items to fix the Rocket!")
# Tells user which items are needed to fix the rocket
def helpfulHints():
    if places[currentPlace]['item'] == 'tools':
        print("Those tools might help us repair the ship!")
    if places[currentPlace]['item'] == 'battery':
        print("That battery might help power the ship!")
    if places[currentPlace]['item'] == 'titanium':
        print("That titanium might help us repair the ship!")
    if places[currentPlace]['item'] == 'fuel':
        print("That fuel might help us lift off!")
    if places[currentPlace]['item'] == 'gemstones':
        print("Ooooooo... Look how shiny those gems are!")
    if places[currentPlace]['item'] == 'rocks':
        print("There sure are a lot of rocks here...")
    if places[currentPlace]['item'] == 'backpack':
        print("A backpack would be helpful in order to carry more items...")

#prints game storyline
print("Oh no! You have been stranded on an abandoned planet...")
time.sleep(1.5)
print("Find all the the necessary parts to repair your Rocket Ship and fly home!")
time.sleep(2)
print("Here is a map:")
time.sleep(.5)

showInstructions()

#loop until launch of rocket
while x == True:
  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':  
    move = input('>')
    
  move = move.lower().split()

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in places[currentPlace]:
      #set the current place to the new place
      currentPlace = places[currentPlace][move[1]]
    #there is no path (link) to the new place
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  elif move[0] == 'get' :
    #if the place contains an item, and the item is the one they want to get
    if "item" in places[currentPlace] and move[1] in places[currentPlace]['item']:
        if places[currentPlace]['item'] == 'backpack':
            inventory += [move[1]]
            del places[currentPlace]['item']
            print("You picked up the backpack! You can carry more items now.")
        else:
            #checks to see it you can carry the item
            if canCarry(inventory) == True:
                #add the item to their inventory
                inventory += [move[1]]
                #display a helpful message
                print(move[1] + ' got!')
                #delete the item from the place
                del places[currentPlace]['item']
            elif canCarry(inventory) == False:
                print("You can't carry this item!")
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  #let's player see inventory
  elif move[0] == 'inventory' :
      print(inventory)
  #checks to see if you are at the rocket and have all the parts
  if currentPlace == 'Rocket': 
    if checkallParts() == True:
        print("You now have all the items to fix the rocket. Let's get off this planet!")
        canFixRocket = True
    else:
        print("You do not have all the items to fix the rocket!")
    
    if canFixRocket == True:
        time.sleep(1.5)
        print("Gathering parts...")
        time.sleep(1.2)
        print("Assembling rocket...")
        time.sleep(1.2)
        print("Running diagnostics check...")
        time.sleep(1.2)
        currentPlace = 'Launch Zone'
        rocketFixed = True
            
    if rocketFixed:
        print("The Rocket is all fixed! Ready to launch?")
            
    else:
        print("You can't launch yet!")
  #let's player launch the rocket
  elif move[0] == 'launch' or 'y':
    if rocketFixed == True:
        print("Firing up the Rocket...")
        time.sleep(1.5)
        print("Launching in...")
        time.sleep(1.2)
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        print("Blast off!")
        x = False


