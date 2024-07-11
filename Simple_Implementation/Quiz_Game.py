questions = ["Question 1: Who was the first President of the US? \n 0) George Washington \n 1) John F. Kennedy \n 2) John Locke \n 3) James Bond",
             "Question 2: When was the declaration of independence signed? \n 0) July 4,1776 \n 1) August 2, 1776 \n 2) August 10,1778 \n 3) May 24, 1864",
             "Question 3: When was the Gettysburg Address given? \n 0) July 4,1776 \n 1) January 16, 1901 \n 2) November 19, 1863 \n 3) November 19, 1862",
             "Question 4: Who invented the lightning rod? \n 0) Thomas Jefferson \n 1) James Monroe \n 2) Elon Musk  \n 3) Benjamin Franklin",
             "Question 5: Which state was not part of the Confederate States of America during the civil war? \n 0) New York \n 1) Texas \n 2) Florida \n 3) Arkansas"]
answers = [0,1,2,3,0]
def quiz():
    correct_answer_counter = 0;

    check_start = input("Would you like to start the quiz?: ")
    if check_start == 'Y' or check_start == 'y':
        print("Starting Quiz... \n")

        for i in range(len(questions)):
            print(questions[i])
            current_answer = int(input("Answer: "))
            
            if current_answer == answers[i]:
                correct_answer_counter = correct_answer_counter + 1
                
    else:
        print("Shutting down quiz...")
    
    print("You got", correct_answer_counter, "/ 5 questions correct!")
    

quiz()