#Import Libraries
import numpy as np
import time
import sys


#------------------------------------------------------------------------------

#Print one letter at a time
def delay_print(sentence):
    for character in sentence:
       sys.stdout.write(character)
       sys.stdout.flush() 
       time.sleep(0.05)    


#------------------------------------------------------------------------------

#Creating the class Character
class Character:
    def __init__ (self, name, hp, attack, defense, luck, special, nemesis):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.luck = luck
        self.special = special
        self.nemesis = nemesis
        self.level = (self.hp + self.attack + self.defense + self.luck)
 
    
 
#------------------------------------------------------------------------------

#Creating the professions and creating a character class

def profession (answer):
    if "1" in answer:
        print("\nYou have chosen the Engineer path.")  
        
    elif "2" in answer:
        print("\nYou have chosen the Environmental path.")
  
    elif "3" in answer:
        print("\nYou have chosen the Land-Rights path.")
    
    elif "4" in answer:
        print("\nYou have chosen the Finance path.")
        
    elif "5" in answer:
        print("\nYou have chosen the Legal path.")
        
    else:
        print("\nYou have chosen the Management path.")      

        

#------------------------------------------------------------------------------

#Creating a function for printing character stats
def print_stats (character):
    print(f"\nName: {character.name}")
    print(f"Health: {character.hp}")
    print(f"Attack: {character.attack}")
    print(f"Defense: {character.defense}")
    print(f"Luck: {character.luck}")
    print(f"Special: {character.special}")
    #print(f"Nemesis: {character.nemesis}")
    print(f"Level: {character.level}")
    
    
    
 #-----------------------------------------------------------------------------   

#Creating a function to calculate the damage
def damage_calc (attacker, defender):
    #Decide on the attack to use
    #Player Option
    if attacker == player:
        #Ask the player to select the move
        delay_print("\nWhat move will you make?")
        time.sleep(0.5)
        
        #Seletcting the option
        print("\n1. By the book", "\n2. Final play")
        answer = input()
        
        #Standard damage calculation
        if "1" in answer:
            attack = (attacker.attack * np.random.randint(5, (1 + attacker.luck)))
            defense = (defender.defense* np.random.randint(5, (1 + defender.luck)))
            damage = int(round(0.5 * np.random.randint(5, (1 + attacker.luck)) * attack/defense, 0))
            delay_print(f"\n{attacker.name} dealt " + str(damage) + f" damage to {defender.name}.\n")
            
            #Defender life left after the attack
            defender.hp = (defender.hp - damage)
            if defender.hp > 0:
                delay_print(f"\n{defender.name} has {defender.hp} health left.\n")
            else:
                delay_print(f"{defender.name} was overcome by your skill, this is your victory!!!") 
            
        
        #Speciality damage calculation
        else:
            defender.hp = -1000
            delay_print(f"\nYou used your special \"{player.special}\". You won the battle but Financial Close has been delayed by " + str(np.random.randint(2,4)) + " months.")
    
    
    else:
        #Automate the nemesis attack
        outcome = str(np.random.randint(0,5))
        
        #Speciality damage calculation
        if "0" in outcome:
            defender.hp = -1000
            delay_print(f"\n{nemesis.name} used their special \"{nemesis.special}\". You lost the battle and Financial Close has been moved forward by " + str(np.random.randint(2,4)) + " months")
            
        #Standard damage calculation
        else:    
            attack = (attacker.attack * np.random.randint(5, (1 + attacker.luck)))
            defense = (defender.defense* np.random.randint(5, (1 + defender.luck)))
            damage = int(round(0.5 * np.random.randint(5, (1 + attacker.luck)) * attack/defense, 0))
            delay_print(f"\n{attacker.name} dealt " + str(damage) + f" damage to {defender.name}.\n")
            
            #Defender life left after the attack
            defender.hp = (defender.hp - damage)
            if defender.hp > 0:
                delay_print(f"\n{defender.name} has {defender.hp} health left.\n")
            else:
                delay_print(f"\n{defender.name} was overcome by your skill, this is your victory!!!") 
         
     #Return defender.hp to ensure that while loop is progressed correctly
    return defender.hp   
            

    
#------------------------------------------------------------------------------    

#Creating the character combat function
def character_combat(player, nemesis):
           #First attack
       if (player.hp > 0) and (nemesis.hp > 0):
           damage_calc(player, nemesis)
           
           #Second attack
           if (player.hp > 0) and (nemesis.hp > 0):
               damage_calc(nemesis, player)
               
               #Third attack
               if (player.hp > 0) and (nemesis.hp > 0):
                   damage_calc(player, nemesis) 
                   
                   #Fourth attack
                   if (player.hp > 0) and (nemesis.hp > 0):
                       damage_calc(nemesis, player) 

                       #Fith attack
                       if (player.hp > 0) and (nemesis.hp > 0):
                           damage_calc(player, nemesis) 
    
                           #Sixth attack
                           if (player.hp > 0) and (nemesis.hp > 0):
                               damage_calc(nemesis, player)
           
                               #Seventh attack
                               if (player.hp > 0) and (nemesis.hp > 0):
                                   damage_calc(player,nemesis)
               
                                   #Eighth attack
                                   if (player.hp > 0) and (nemesis.hp > 0):
                                       damage_calc(nemesis, player)
                   
                                       #Nineth attack
                                       if (player.hp > 0) and (nemesis.hp > 0):
                                           damage_calc(player, nemesis) 

                                           #Tenth attack
                                           if (player.hp > 0) and (nemesis.hp > 0):
                                              damage_calc(nemesis, player)



#------------------------------------------------------------------------------  
    
#Creating the instructions and opening story dialogue

#Printing the instructions and starting the game
delay_print("\nUse the number pad to select your choices\n")
time.sleep(2)

print("\n----------------------------the story begins---------------------------------")
time.sleep(1)

#Opening line
delay_print ("\nYou must be lost traveller, only the mad come here. This is the land of the IPP after all...\n")
time.sleep(1)

#Exit or continue option
delay_print ("\nWill you continue the journey?")
time.sleep(0.5)
print("\n1. Please no, I cannot go through another design freeze",
"\n2. Respect my authority, I am a Pro!")

answer_1 = input()
if "1" in answer_1:
    delay_print("\nAlas, this path is not meant for everyone.")
    play_game = False

else:
    delay_print("\nVery well, I acknowledge your skill. Let's see how you fare...")
    print("\n")
    play_game = True   
    
    
    
 #-----------------------------------------------------------------------------  
 
 #Starting the battle
while play_game is True:

    #Picking your profession:
    delay_print("\nWhat is your chosen profession")
    time.sleep(0.5)
    print("\n1. Engineer",
          "\n2. Environmental",
          "\n3. Land-Rights",
          "\n4. Finance",
          "\n5. Legal",
          "\n6. Management")    
    
    answer = input()
    
    profession(answer)
    
    #Player lists
    player_name = ["Engineer", "Environmental", "Land-Rights", "Finance", "Legal", "Management"]
    player_special = ["Thats not what the data says", "The maps reveal all", "We have a lease agreement", 
                      "The numbers don't lie", "That's standard FIDIC", "That's not what we signed up for"]
    player_nemesis = ["LTA", "Birds", "Landowners", "Lenders", "EPC", "IPPO"]
    
    #Creating a player using the class Character
    player = Character(name = player_name[int(answer)-1],
    hp = np.random.randint(5,11), 
    attack = np.random.randint(5,11), 
    defense = np.random.randint(5,11), 
    luck = np.random.randint(5,11), 
    special = player_special[int(answer)-1], 
    nemesis = player_nemesis[int(answer)-1])

    #Nemesis lists
    nemesis_name = ["LTA", "Birds", "Landowners", "Lenders", "EPC", "IPPO"]
    nemesis_special = ["Generation losses should be 1.5% higher", "Safe zone just increased to 10km", 
                       "I want to renegotiate", "That's project finance 101", "That's market standard", 
                       "We don't see why that should be a problem"]

    nemesis_nemesis = ["Engineer", "Environmental", "Land-Rights", "Finance", "Legal", "Management"]

    
    #Creating a nemesis using the class Character
    nemesis = Character(name = nemesis_name[int(answer)-1],
    hp = np.random.randint(5,11), 
    attack = np.random.randint(5,11), 
    defense = np.random.randint(5,11), 
    luck = np.random.randint(5,11), 
    special = nemesis_special[int(answer)-1], 
    nemesis = nemesis_nemesis[int(answer)-1])

    
    
    print("\n----------------------------------------------------------------------------")
    #Printing the character stats
    delay_print("\nYour stats are:\n")
    print_stats (player)
    time.sleep(1.5)

    #Printing the nemesis stats
    delay_print("\nYour nemesis stats are:\n")
    print_stats (nemesis)
    time.sleep(1.5)
    print("\n")
    
    print(f"\n--------------------------{player.name} VS {nemesis.name}-------------------------------")
    
    #Deciding who goes first
    #Player makes the first move
    if player.luck >= nemesis.luck:
       delay_print(f"\n{player.name} makes the first move...\n")
       
       #player combat order
       character_combat(player, nemesis)
    
    
    
    #Nemesis makes the first move
    else:
        delay_print(f"\n{nemesis.name} makes the first move...\n") 
        
        #Nemesis combat order
        character_combat(nemesis, player)
    
    
    #Ending the battle
    play_game = False

#------------------------------------------------------------------------------    

#Ending credits
print("\n")
print("\n-----------------------------------------------------------------------------")

#Determining outcome
#Player did not play
if "1" in answer_1:
    delay_print("\nBest to go back to the kiddy pool, these waters are deep.")
#Player wins
elif player.hp > nemesis.hp:
    delay_print("You have overcome this challenge but there are still many more to overcome before Financial Close - Keep on Keepin On!")

#Nemesis wins
else:
    delay_print("You may have lost this challenge but tomorrow is another day - Keep On Keeping On!")

print("\n")
print("\n--------------------------------The End--------------------------------------")