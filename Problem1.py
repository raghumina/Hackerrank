# HACKERRANK
# PYTHON PROBLEM AND SOLUTIONS
# link of the problem:

# PROBLEM 1.
# Python If Else

# Given an integer, , perform the following conditional actions:
#
# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5, print Not Weird
# If  is even and in the inclusive range of 6 to 20, print Weird
# If  is even and greater than 60, print Not Weird
# Input Format
#
# A single line containing a positive integer, .
#
# Constraints
#
# Output Format
#
# Print Weird if the number is weird. Otherwise, print Not Weird.
#
# Sample Input 0
#
# 3
# Sample Output 0
#
# Weird
# Explanation 0
#
#
#  is odd and odd numbers are weird, so print Weird.
#
# Sample Input 1
#
# 24
# Sample Output 1
#
# Not Weird
# Explanation 1
#
#
#  and  is even, so it is not weird.


# lets start
'''
user_input = int(input("Enter number here: "))
if user_input % 2 != 0:
    print("weird")

    while user_input in range(2, 5):
        if user_input / 2 == 0:
            print("Not, weird")
    for user_input in range(6, 20):
        if user_input / 2 == 0:
            print("Weird")
'''
input1 = int(input())
if input1 % 2 != 0:
    print("Weird")
elif input1 in range(2,5) and input1 % 2 == 0:
    print("Not Weird")
elif input1 in range(6,20) and input1 % 2 == 0:
    print("Weird")
elif input1 > 20 and input1 % 2 != 0:
    print("Weird")
elif input1 > 60 and input1 % 2 == 0:
    print("Not Weird")
else:
    print("Not Weird")
