# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: <author>
# Creation Date: <date>
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.

import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')#um...normal quotations would have worked fine here me thinks.
	print()#Heh?

def chooseCave():#Or did you misspell this?
    cave = ''#The hell is this shit? INDENT THE LINE!!
	while cave != '1' and cave != '2':
		print('Which cave will you go into? (1 or 2)')
		cave = input()

	return caves

def checkCave(chosenCave):#This doesn't feel right...right? shouldn't this be (chooseCave)? 
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2) #What in the...WHat are you!?
	friendlyCave = random.randint(1, 2)#Shouldn't there be a 3 in there somewhere?

	if chosenCave == str(friendlyCave):#So...does this line reference line 26? It might be easier to define a class, and change that function to an attribute.
		print('Gives you his treasure!')
	else:
		print 'Gobbles you down in one bite!'

playAgain = 'yes' #Does this belong here?
while playAgain = 'yes' or playAgain = 'y':#Need another equal sign after playAgain, both times, to actuate the while loop.
	displayIntro()#You will also need to re-indent, or copy, delete, and paste these lines back after adding that extra equal sign and creating the while loop.
	caveNumber = choosecave()
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)') #Lines 50 and 51 feel out of place, which confuzzles me.
	playAgain = input()
	if playAgain == "no": #Wait, so if you're going to do this, wouldn't you need a break line thingy to break the while loop, to get to this line?
		print("Thanks for planing")#Also, wouldn't it be simpler to use an if-elif thing, and change this line to elif, and change line 45 to an if instead of a while loop?

