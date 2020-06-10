"""
Program: test_validation_with_try.py
Author: Paul Elsea
Last Modified: 06/10/2020

Program to get user name, age, and three scores. Scores
are averaged and all input is checked. Results are printed.
"""
def average():
    score1 = get_score()
    score2 = get_score()
    score3 = get_score()
    return (score1+score2+score3)/3
'''Function to call get_score func to collect three scores, then returns their average'''


def valid_name_check(input_string):
    result = input_string.replace(" ", "").isalpha()
    return result
'''Function to verify that input name uses only alphabetic characters'''

def get_name():
    while True:
        name = input("Please enter your name: ")
        valid_result = valid_name_check(name)

        if valid_result == False:
            print("Please enter only first, or first and last names using only alphabetic characters and one space")
            continue
        else:
            break
    return name
'''Function to accept user input for name, and call the valid_name_check func to check the input'''

def get_age():
    while True:
        try:
            age = int(input("Please enter your age: "))
        except ValueError:
            print("Invalid age. Please use only numbers")
            continue

        if age <= 0:
            print("Please enter an age of 1 or above")
            continue
        else:
            break
    return age
'''Function to accept user input for age and check it for a minimum amount'''

def get_score():
    while True:
        try:
            user_score = int(input("Please enter score: "))
        except ValueError:
            print("Invalid score. Please use only numbers between 1 and 100")
            continue

        if user_score < 0:
            raise ValueError
            # print("Please enter an age of 0 or above")
            continue
        if user_score > 100:
            print("Please enter an age of 100 or below")
            continue
        else:
            break
    return user_score
'''Function to accept user input for a test score, then verify it is between 0 and 100'''


if __name__ == '__main__':
    user_input_name = get_name()
    user_age = get_age()
    ave_score = average()
    print(user_input_name + ', ' + str(user_age) +
          ' years old had an average score of ' +
          str(round(ave_score, 2)))
'''Main method that calls get_name(), get_age(), and average(). All results are saved as variables this are
then printed with additional text'''