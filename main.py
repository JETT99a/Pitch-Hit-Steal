# Version 0.9 Beta
# Added Beta pitching Interface  

import random
import time

outs = 0
strikes = 0 
balls = 0
ining = 0
home = 0
away = 0
base1 = 0
base2 = 0
base3 = 1

print("""
|=============================|
| Welcome to Pitch Hit Steal! |
|=============================|

""")

input("\nPress Enter To Start Game ")

print("\nTop of the 1st")

while ining != 4:                #game loop
 
 while outs != 3:                #inning loop, change                                inning once 3 outs
   time.sleep(1.5)
   print("\nOuts:",outs,"\tBatter steps into the box")
   pitch = random.randint(1,3)
   print("\n\t1. Fastball\n\t2. Curveball\n\t3. Slider")
   sel = int(input("\nSelect the pitch "))
  
   print("\nAnd Heres the pitch")
   time.sleep(1)

   if pitch == sel:               #selection, pitch comparison
    if random.randint(1,2) == 1:   #location selector
     print("\nInfeild Hit! Single")
     strikes = 0
    else:
      print("\nOutfeild Hit! Double") #hits to the outfeild = double
      strikes = 0
   else:
    strikes += 1
    print("\nswing and a miss for Stike ",strikes)
    
    if strikes == 3:
      print ("\nStrike Three your out!")
      outs += 1
      strikes = 0
      time.sleep(2)
 
 print("\nSWITCH SIDES")
 
 outs = 0
 base1 = 0
 base2 = 0
 base3 = 0

 while outs != 3:
   print("You Are Now The Pitcher")
   time.sleep(1.5)
   print("\nOuts:",outs,"\tBatter steps into the box")
   cpu_hitter = random.randint(1,3)
   print("\n\t1. Fastball\n\t2. Curveball\n\t3. Slider")
   sel = int(input("\nSelect the pitch you want to throw "))
  
   print("\nAnd Heres the pitch")
   time.sleep(1)

   if cpu_hitter == sel:               #selection, pitch comparison
    if random.randint(1,2) == 1:   #location selector
     print("\nInfeild Hit! Single")
     strikes = 0
    else:
      print("\nOutfeild Hit! Double") #hits to the outfeild = double
      strikes = 0
   else:
    strikes += 1
    print("\nswing and a miss for Stike ",strikes)
    
    if strikes == 3:
      print ("\nStrike Three the batter is out")
      outs += 1
      strikes = 0
      time.sleep(2)

