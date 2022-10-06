# By Sir Mohammad Faizal

def calculate_upper_and_lowercase(sentence):
    upper = 0
    lower = 0

    for i in sentence:

        if i.isupper():   # is upper is a built-in method
            upper = upper + 1

        elif i.islower():  # is lower is a built-in method
            lower = lower + 1

    return upper, lower

to_calculate = input("Please enter any words:\n")

total_upper = calculate_upper_and_lowercase(to_calculate)[0]  # what list do here?
total_lower = calculate_upper_and_lowercase(to_calculate)[1]

print("Total uppercase letters:", total_upper)
print("Total lowercase letters:", total_lower)