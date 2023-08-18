#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

#ne_animals = farms[1]["agriculture"]
#print(ne_animals)
#for animal in ne_animals:
    #print(animal, end="\n")

def main():
    valid_input = {"a":"NE Farm", "b": "W Farm", "c": "SE Farm"}
    usr_input = input("Would you like to know more about \nA.The Northeast farm\nB. The West Farm\nC. the SouthEast Farm\n:")
    while usr_input.lower() not in valid_input:
        usr_input = input("Please enter A B or C\n: ")
    choice = valid_input.get(usr_input)
    print(choice)
    #for farm in farms:
        print(farms["choice"]["agriculture"])
        print(f"The {choice} raises {farms[]}")
    #for farm in farms:
    #if choice in farm:
        print()
        #print("-", farm["name"])
        #choice= input("Pick a farm!\n")


main()