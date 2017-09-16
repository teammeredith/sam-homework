# Tell the user what they need to do
print("Enter some single digits with commas inbetween")
# Get the input from the user
string = input()
# Turn the string into a list of numbers
numbers = string.split(',')
# Sort the numbers from lowest to highest
numbers.sort()
# Print the lowest number
print("The lowest number using those digits is", ''.join(numbers))
# Sort the numbers from highest to lowest
numbers.sort(reverse=True)
# Print the highest number
print("The highest number using those digits is", ''.join(numbers))


