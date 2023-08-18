#!/usr/bin/env python3


#make a loop that prints the entire "99 bootes of beer song"

#use for ____ in range(____):
#      print ( _____)
#beer_num = int(input("How many beers do you start with?"))
def main():
    beer_num = int(input("How many bottles of beer are on the wall?"))
        
    for rando in range(beer_num):
        if beer_num == -1:
            break
        print(f"{beer_num} bottles of beer on the wall!\n{beer_num} bottles of beer! Take one down, pass it around")
        beer_num = beer_num - 1
        #print(f"{beer_num} bottles of beer on the wall!")

        
main()