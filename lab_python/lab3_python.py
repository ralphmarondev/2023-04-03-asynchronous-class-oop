# Ralph Maron Eda
# BSCPE-2A
# 2023-04-03
# Write a program that will compute for the students average
# The user will input the following:
# Name, Math, Science, English
# If the average is equal and above 75, status is Passed,
# else, You Failed the semester.
def is_passed(grade : float):
    return True if grade > 74 else False


def main():
    failed_subs = []
    name = input("Enter your name: ")

    math = float(input("Math: "))
    if not is_passed(math):
        failed_subs.append("Math")

    science = float(input("Science: "))
    if not is_passed(science):
        failed_subs.append("Science")

    english = float(input("English: "))
    if not is_passed(english):
        failed_subs.append("English")

    average = (math + science + english) / 3

    print(f"Average: {average}")

    if is_passed(average):
        print(f"Congratulations {name}! You passed the semester.", end="")

    if not len(failed_subs) == 0:
        print(f"But you need to re-enroll ", end="")

        if len(failed_subs) == 1:
            print(f"{failed_subs[0]} subject.")
        elif len(failed_subs) == 2:
            print(f"{failed_subs[0]}, and {failed_subs[1]} subjects.")
        else:
            print(f"{failed_subs[0]}, {failed_subs[1]}, and {failed_subs[2]} subjects.")


if __name__ == "__main__":
    main()
