import random
def entry():
 print("ROCK PAPER & SCISSORS")
 print("You will have 3 Chances to Win the Game")
 print("----------------------------------------")
 print("let's Start")
 print("""
 (1)--ROCK
 (2)--PAPER
 (3)--SCISSOR    
 """)


def rockpaper():
        userInput1 = int(input("Enter (1/2/3) from the above:"))
        while userInput1 > 3 or userInput1 < 1:
            print("Invalid-Input")
            userInput1 = int(input("Enter Again:"))
        if userInput1 == 1:
            choice = "Rock"
        elif userInput1 == 2:
            choice = "Paper"
        elif userInput1 == 3:      
            choice = "Scissors" 
        print("=====================================")     
        print("You choice is: ",choice)
        print("Now it's Computer Turn")

        compChoice = random.randint(1,3)
        if compChoice == 1:
         comp_choice_name = "Rock"
        elif compChoice == 2:
         comp_choice_name = "Paper"
        elif compChoice == 3:
         comp_choice_name = "Scissors"
        print("The Computer Choice is: ",comp_choice_name) 
        print("=====================================")
        print("---------->",choice ,"V/s", comp_choice_name,"<----------")
        print("=====================================")

        result = None
        if((userInput1 == 1 and compChoice == 2) or
          (userInput1 == 2 and compChoice ==1 )):
          result = "Paper"
        elif((userInput1 == 1 and compChoice == 3) or
            (userInput1 == 3 and compChoice == 1)):
           result = "Rock"
        elif((userInput1 == 2 and compChoice == 3) or
            (userInput1 == 3 and compChoice == 2)):
          result = "Scissors"
        elif userInput1 == compChoice:
            print("IT'S A DRAW")  
    
        if result == choice:
         print("You Win")
        elif result != choice:
         print("You Lose!")
 



def main_menu():
    entry()
    rockpaper()
    end1 = input("Do you like to Play Again [Y/N]:").lower()
    while end1 != "y" and end1 != "n":
        print("Invalid-Input")
        end1 = input("Enter Again [Y/N]:").lower()
    if "y" in end1:
        entry()
        rockpaper()
    elif "n" in end1:
        print("End Program")
        exit()        
main_menu()
