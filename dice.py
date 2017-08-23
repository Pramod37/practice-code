from random import randint
dice_roll = "YES"
while dice_roll == "YES" or dice_roll == "y":
    print"the dice is rolling.."
    print (randint(0,6))
    dice_roll = raw_input("do you want to roll again(y/n)?")