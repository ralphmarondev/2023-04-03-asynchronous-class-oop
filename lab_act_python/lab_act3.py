# Ralph Maron Eda
# BSCPE-2A
# 2023-04-03
# 1. Write a word back program
# 2. The program will ask to enter a word
# 3. The program will store the word in a list
# 4. The program will ask if the user wants to try again.
#       The user will input Y/y if yes, and N/n if no.
# 5. If yes, refer to step 2.
# 6. If no, Display the total number of words, and all
#       the words that user entered.
def main():
    word_bank = []
    CHOICE = "Y"

    while CHOICE.upper() == "Y":
        word = input("Enter word: ")
        word_bank.append(word)

        CHOICE = input("Do you want to try again? [Y - Yes, N - No]: ")

    print(f"Total number of words: {len(word_bank)}")
    print(f"Words entered: {word_bank}")


if __name__ == "__main__":
    main()
