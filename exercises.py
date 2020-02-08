# Question 1
# Write a program that takes a string from the user and prints the first number encountered along with it's position. You can assume the number is a single digit

# First we set the variables for the user input and initialise a counter
user_string = input("Please enter your string here: ")
counter = 0

#breakpoint()
while counter <= len(user_string) and not user_string[counter].isnumeric():
    counter += 1

print(counter)
if counter <= len(user_string):
    print(f"Here is your number {user_string[counter]} and its index is {counter}")

else:
    print("Your string does not contain a number")
