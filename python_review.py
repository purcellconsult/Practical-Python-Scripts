###########################################
# Python code that demos what was taught
# in the lesson.
#
# Includes code that works with operators,
# control flow, iteration, functions, and
# a list.
#
#
# By Doug A Purcell
#
############################################

# A sample of how to use operators in python

x, y = 10, 100  # declares two variables

addition = x + y  # the sum of x and y which is 110

subtraction = y - x  # 100 - 10 which is 90

multiply = x * y  # 100 x 10 which is 1000

division = y / x  # 100 / 10 which is 10.0

# display the results to the console using print()

print(f"addition = {addition}, subtraction = {subtraction}, multiply = {multiply}, division = {division}")

# if statement
# ------------

weather = 70.0  # in degrees F
if weather >= 70:
    print("Go for a jog!")
else:
    print("no to a jog, it's too cold")

# iteration
# ----------
# prints even numbers from 1... 100
# end = ' ' displays the output horizontally

for x in range(1, 101):
    x = x + 10
    print(x, end=' ')


# function
# ---------

def triple_numbers(stop=101):
    for num in range(1, stop):
        print(num * 3)


triple_numbers()  # call or execute the function by typing its name
