#!/usr/bin/env python3

# Made By Jaydin Madore
# Made On Oct 19, 2022


def main():
    max = 40 
    min = 25

    # Requests the user's age.
    age_str = input("Enter your age: ")

    # Tries casting age from string to int.
    try:
        age_int = int(age_str)

    # Executed if age cannot be converted to int.
    except ValueError:
        print("You did not enter an integer.")
        main()
        
    # Executed if user_guess is not b/w 25 and 40
    if age_int < min or age_int > max:
        print(f"You can not data my grandchild")

    # Executed if the user age is b/w 25 and 40.
    
    else: 
        print("You can date my grandchild")
    

if __name__ == "__main__":
    main()
