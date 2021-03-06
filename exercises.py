# Question 1
# Write a program that takes a string from the user and prints the first number encountered along with it's position. You can assume the number is a single digit

# First we set the variables for the user input and initialise a counter
# user_string = input("Please enter your string here: ")
# counter = 0

# Next we construct a while loop to check each index for a number
# while counter < len(user_string) and not user_string[counter].isnumeric():
#     counter += 1
#
# # The conditional statements are used to print out the output, of whether the string contains a number or not
# if counter >= len(user_string):
#     print("Sorry your string does not contain any numbers")
#
# elif counter < len(user_string):
#     print(f"Here is your number {user_string[counter]} and its index is {counter}")

# Question 2
# Building upon the previous exercise, write a program that takes a string as input from the user and prints the first number encountered along with the starting position of the number.

# # First we set the variables for the user input and initialise a counter. We need to include a second counter for the second while loop
# user_string = input("Please enter your string here: ")
# counter_str = 0
# counter_num = 0

# Next we construct a while loop to check each index for a number
# while counter_str < len(user_string) and not user_string[counter_str].isnumeric():
#     counter_str += 1
#
#     # The conditional statements are used to print out the output, of whether the string contains a number or not
#     if counter_str >= len(user_string):
#         print("Sorry your string does not contain any numbers")
#
#     elif counter_str < len(user_string) and user_string[counter_str].isnumeric():
#         # This second while loop iterates through the string starting from the first instance of the number to the last instance
#         while counter_num < len(user_string) and user_string[counter_str].isnumeric():
#             counter_num += 1
#
#         # This print statement slices the string from the start of the number, to the end of the number
#         print(f"Here is your number {user_string[counter_str:counter_num]} and its index starts at {counter_str}")


# Question 3
# Write a program that takes a string as input from the user. The string will consist of digits and your program should print out the first repdigit. A repdigit is a number where all digits in the number are the same. Examples of repdigits are 22, 77, 2222, 99999, 444444. You can also assume that each number will have differing digits unless it is a repdigit.

# First we define the user input variables and initialise a counter
user_input = (input("Please enter your number: "))
counter_1st_dig = 0
counter_last_dig = 0

# Next we construct a while loop to iterate through the number. We want the loop to stop when both conditions are met
#123445678
while counter_1st_dig < len(user_input) and user_input[counter_1st_dig] != user_input[counter_1st_dig - 1]:

    counter_1st_dig += 1
    if counter_1st_dig == len(user_input):
        print("There are no repdigits in this string")

    # this second while loop contained in this condition allows us to get the range the digits repeat
    elif counter_1st_dig < len(user_input) and user_input[counter_1st_dig] == user_input[counter_1st_dig - 1]:
        counter_last_dig = counter_1st_dig
        while counter_last_dig < len(user_input) and user_input[counter_1st_dig] == user_input[counter_last_dig]:
            counter_last_dig += 1

        print(f"Here are your repdigits {user_input[counter_1st_dig -1 :counter_last_dig]} ")

