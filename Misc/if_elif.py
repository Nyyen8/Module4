"""
Program: if_elif.py
Author: Paul Elsea
Last Modified: 06/09/2020

Program to ask which level of a subscription service they want to sign up for.
"""

'''Function to accept user input for subscription level, then prints cost.'''
def offer_sub_list():
    """Initial print statement. Doesn't repeat."""
    print("Thank you for your interested in our Monthly Subscription Box!\n"
                           "Please Select from the following levels to learn more.\n"
                           "Platinum\n"
                           "Gold\n"
                           "Silver\n"
                           "Bronze\n"
                           "Free Trial\n"
                           "")

    """Main while loop that continues until user choose to terminate program"""
    while True:
        """Secondary while loop that continues until user chooses valid membership option"""
        while True:
            """if-elif statements that return various levels of service based on user input, or an error message if 
                            they choose outside of the available option."""
            choice = input()
            if (choice == "Platinum") or (choice =="platinum"):
                print("Our platinum level is our best, costing $60 a month.\n"
                      "")
                break
            elif (choice == "Gold") or (choice =="gold"):
                print("Our gold level is nearly our best, costing $50 a month.\n"
                      "")
                break
            elif (choice == "Silver") or (choice =="silver"):
                print("Our silver level is a good medium, costing $40 a month.\n"
                      "")
                break
            elif (choice == "Bronze") or (choice =="bronze"):
                print("Our bronze level is good value for money, costing $30 a month.\n"
                      "")
                break
            elif (choice == "Free Trial") or (choice == "free trial") or (choice == "Free trial"):
                print("Our free trial is a good way to try before you buy, costing nothing.\n"
                      "")
                break
            else:
                print("Sorry, I didn't understand you selection. Please try again.\n"
                      "")
                continue

        """Prompt for input that determines if program continues."""
        continue_choice = input("Would you like to look at another level? 'Y' to continue, any other key to exit.\n"
                      "")
        if (continue_choice == "y") or (continue_choice == "yes") or (continue_choice == "Yes") or (continue_choice == "Y"):
            print("Which level would you like to learn about?\n"
                  "Platinum\n"
                  "Gold\n"
                  "Silver\n"
                  "Bronze\n"
                  "Free Trial\n"
                  "")
            continue
        else:
            print("Thanks for you interest.")
            break

if __name__ == '__main__':
    offer_sub_list()
'''Main method that calls offer_sub_list()'''