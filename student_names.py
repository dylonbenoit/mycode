#!/usr/bin/env python3
""" Alta3 Research | Lists Challenge """

def main():

    wordbank = ["indentation", "spaces"] 

    tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']


    wordbank.append(4)
    
    print(wordbank)


    num = int(input("Pick a number between 0 and 20: "))

    student_name = tlgstudents[num]

    #print(student_name)
    print(f"Your unfortunate victim is {student_name}!")



    print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

    name = random.choice(tlgstudents)
    print(f"{student_name}")

main()
