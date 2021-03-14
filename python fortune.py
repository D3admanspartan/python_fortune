#!/usr/bin/python/

#Fortune Cookie Program
#The Computer generates a random positive message 
#Messages will be either inspirational or motivational quotes 
#By actual famous people,Random people or Lawton C. Mizell 

#Random Module Imported
import random 

print("Welcome!\n")
print("Here is your random positive message for the day...\n") 

positive_message = random.randint(1,8) 

if positive_message == 1: 
    print("White and Nerdy!!! - Weird Al")
elif positive_message == 2:
    print("Hey!!! Ho!!! You have been RickRolled - D3admanspartan")  
elif positive_message == 3: 
    print( "What color are a pirate's socks...Argyl - bad pirate jokes" )
elif positive_message == 4: 
    print("If you want PI go with Raspberry PI - Microcenter")
elif positive_message == 5:
    print("Magic 8 Ball says try again. - What happens with the Magic 8 Ball")
elif positive_message == 6: 
    print("There is no try, there is just do - Master Yoda")
elif positive_message == 7:
    print("I am giving her all I got - Scotty") 
elif fortune == 8:
print("Fortune cookies rarely share fortunes.")
