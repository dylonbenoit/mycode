#!/usr/bin/env python3

#html.escape(s, quote=True)
#Convert the characters &, < and > 

#html.unescape(s)¶
#Convert all named and numeric character references (e.g. &gt;, &#62;, &#x3e;) in the string

#Slice and print out the trivia question and the four answers (one correct, three incorrect) from the dictionary.

#BONUS: have the user answer A, B, C, or D and see if they guess the answer correctly!

import html

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }



def main():
    #the following format coorectly displays the value in readable
   # print(html.unescape(trivia["correct_answer"]))

    print(trivia["question"])
    option1 = html.unescape(trivia["incorrect_answers"][0])
    option2 = html.unescape(trivia["incorrect_answers"][1])
    option3 = html.unescape(trivia["incorrect_answers"][2])
    option4 = html.unescape(trivia["correct_answer"])

    print(f"A. {option1}")
    print(f"B. {option2}")
    print(f"C. {option3}")
    print(f"D. {option4}")


    usr_ansr = input(": ")
    print(usr_ansr)
    if usr_ansr == "D" or usr_ansr == "d":
        print("CORRECT! GOOD JOB!")
    else:
        print(f"WRONG. The correct answer was D. {option4}]")



main()