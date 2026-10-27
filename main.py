"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    cost = annual_cost / SEMESTERS_PER_YEAR
    return cost


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    cost = annual_cost / MONTHS_PER_YEAR
    return cost


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    cost = annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)
    return cost


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    credit = (annual_cost / credits) / SEMESTERS_PER_YEAR
    return credit


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    cost = cost_per_credit(annual_cost, credits) / 15
    return cost



#def was_it_worth_it(user):
    user = user.upper
    if user == "Y":
        print("Glad to see it was worth your time...hopefully.")


    if user == "N":
        print("There will be better classes...maybe.")

    else:
        print("I guess we'll never know.")



# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    
    price = input("What is the total cost for one year?")
    credit = input("How many credits this semester?")

    price = float(price)
    credit = float(credit)



    while True:
        # Show your menu here.
        print("COST OF COLLEGE!")
        print("Cost per Semester: 1")
        print("Cost per Month: 2")
        print("Cost per Day: 3")
        print("Cost per Credit: 4")
        print("Cost per Class: 5")
        #print("Was it worth it?: 6")
        print("Quit: Q")

        choice = input("Choose an option: ")

        if (choice == "Q"):
            break

        elif (choice == "1"):
            semester = cost_per_semester(price)
            print(f"Cost per semester: {semester:.2f}")

        elif (choice == "2"):
            month = cost_per_month(price)
            print(f"Cost per month: {month:.2f}")

        elif (choice == "3"):
            day = cost_per_day(price)
            print(f"Cost per day: {day:.2f}")

        elif (choice == "4"):
            credit_cost = cost_per_credit(price, credit)
            print(f"Cost per credit: {credit_cost:.2f}")

        elif (choice == "5"):
            classes = cost_per_class(price, credit)
            print(f"Cost per class: {classes:.2f}")

        else:
            print("Invalid, pick a different option.")



        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
