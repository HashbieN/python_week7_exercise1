# Simple Python
# Hashbie Nazray Nazarinie bin Mohammad     20DDT20F2028

# Write a Python function that accepts a string.
# Calculates the number of uppercase letters and lowercase letters.

some_string = str(input("Type something:\n"))

# takes SOME_STRING and calculates u/c and l/c letters

# create a FOR loop

# declare variables

upper = 0   # upper is an int

for count in some_string:

    if count >= 'A' and count <= 'Z':
        upper = upper + 1

print ("Number of upper case letters:" + str(upper))

# Started   : 1555
# Ended     :