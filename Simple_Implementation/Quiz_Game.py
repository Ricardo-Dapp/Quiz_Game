
questions = [["Question 1: Who was the first President of the US? \n 0) George Washington \n 1) John F. Kennedy \n 2) John Locke \n 3) James Bond", '0'],
             ["Question 2: When was the declaration of independence signed? "," 0) July 4,1776 \n 1) August 2, 1776 \n 2) August 10,1778 \n 3) May 24, 1864", '1']]
def quiz():
    correct_answer_counter = 0;
    

    check_start = input("Would you like to start the quiz?: ")
    if check_start == 'Y' or check_start == 'y':
        print("Starting Quiz... \n")
        for i in questions:
            print(i)
            current_answer = input("Answer: ")
            if current_answer == i[1]:
                correct_answer_counter = correct_answer_counter + 1
                print("Correct answers: ", correct_answer_counter)
    else:
        print("Shutting down quiz...")
    

def display_questions():
    print()

def show_score():
    print()

quiz()