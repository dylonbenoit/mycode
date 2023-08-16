#!bin/bash/env python3

def main():

#save a users input to the variable char_name from the following questions


    char_name = input("Which character do you want to know about? (Starlord, Mystique, or Hulk?): ")
    print(char_name)
#save user input for statistic questions

    char_test = input("What statistic do you want to know about? (real name, powers, or archenemy?): ")
    print(char_test)
#use libraries to pull correct information

    marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

    #print(f"{char_name}'s {char_test} is {marvelchars.get('char_name'{'char_test'})}!")
    print(f"{char_name}'s {char_test} is {marvelchars.get(char_name).get(char_test)}")


main()
