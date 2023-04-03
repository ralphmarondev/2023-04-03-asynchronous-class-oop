# Ralph Maron Eda
# BSCPE-2A
# 2023-04-03
# step 1: Write a program that adds two numbers.
# step 2: The program will ask to enter first and second number
# step 3: The program will display "The sum of n1 and n2 is Total"
# step 4: The program will ask if the user wants to try again.
#       The user will input Y/y if Yes, and N/n if no
# step 5: If year refer to step 2
# step 6: If no, the program will display "Thank you!"
def main():
    CHOICE = "Y"

    while CHOICE.upper() == "Y":
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))

        print(f"The sum of {first_number} and {second_number} is {first_number + second_number}.")

        CHOICE = input("Do you want to try again? [Y - Yes, N - No]: ")

    print("Thank you!")


if __name__ == "__main__":
    main()
