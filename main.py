import random
import time

outs = 0
strikes = 0
balls = 0
ining = 0
home = 0
away = 0
b1 = 0
b2 = 0
b3 = 0

print("""
|=============================|
| Welcome to Pitch Hit Steal! |
|=============================|

When prompted select the pitch you think the pitcher will throw, if you get it correct then you get a hit. if you don't get it correct you miss the ball and a strike is added. while pitching it's the same thing except you are trying to strike the batter out and not allow a hit. If the base says that is it 0 it is unoccupied, but if its 1 then there is a runner occupying the base.
""")

input("\nPress Enter To Start Game ")



while ining != 4:  #game loop
    ining += 1
    while outs != 3:  #inning loop, change                                inning once 3 outs
        print("\nInning: ", ining, "\tHome: ", home, "\tAway:", away, "\tOuts: ", outs)
        print("\tFirst Base: ", b1, "\tSecond Base: ", b2, "\tThird Base: ", b3)
        time.sleep(2.5)
        print("\nBatter steps into the box")
        pitch = random.randint(1, 3)
        print("\n\t1. Fastball\n\t2. Curveball\n\t3. Slider")
        sel = int(input("\nSelect the pitch "))

        print("\nAnd Heres the pitch")
        time.sleep(1)

        if pitch == sel:  #selection, pitch comparison
         print("HIT!")
         strikes = 0
         if b1 == 1:
           if b2 == 1:
             if b3 == 1:
               home += 1 
               print("You Got 1 run!!")
             elif b3 == 0:
               b3 = 1
           elif b2 == 0:
             b2 = 1
         elif b1 == 0:
           b1 = 1
      
        else:
          strikes += 1
          print("\nswing and a miss for Stike ", strikes)
          if strikes == 3:
                print("\nStrike Three your out!")
                outs += 1
                strikes = 0
                time.sleep(2)

    print("SWITCH SIDES")
    b1 = 0
    b2 = 0
    b3 = 0
    outs = 0
    while outs != 3:  #inning loop, change                                inning once 3 outs
        print("\nInning: ", ining, "\tHome: ", home, "\tAway:", away, "\tOuts: ", outs)
        print("\tFirst Base: ", b1, "\tSecond Base: ", b2, "\tThird Base: ", b3)
        time.sleep(1.5)
        print("\nBatter steps into the box")
        pitch = random.randint(1, 3)
        print("\n\t1. Fastball\n\t2. Curveball\n\t3. Slider")
        sel = int(input("\nSelect the pitch You want the throw"))

        print("\nAnd Heres the pitch")
        time.sleep(2)

        if pitch == sel:  #selection, pitch comparison
          print("HIT!")
          stikes = 0
          if b1 == 1:
           if b2 == 1:
             if b3 == 1:
               away += 1 
               print("you let up a run")
             elif b3 == 0:
               b3 = 1
           elif b2 == 0:
             b2 = 1
          elif b1 == 0:
           b1 = 1

        else:
          strikes += 1
          print("\nswing and a miss for Stike ", strikes)
          if strikes == 3:
                print("\nStrike Three The batter is out")
                outs += 1
                strikes = 0
                time.sleep(2) 
    print("SWITCH SIDES")
    b1 = 0
    b2 = 0
    b3 = 0
    outs = 0
if home >= away:
  print("You Won!!! \n The Final Score: ","\tHome: ", home, "\tAway:", away)
elif away >= home:
  print("You Lost :( \n The Final Score: ","\tHome: ", home, "\tAway:", away)
