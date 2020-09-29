# Problem 13
# Recursion
# Problem link : https://www.hackerrank.com/challenges/30-recursion/problem

# Objective
# Today, we're learning and practicing an algorithmic concept called Recursion.
# Check out the Tutorial tab for learning materials and an instructional video!
#
# Recursive Method for Calculating Factorial
# Task
# Write a factorial function that takes a positive integer,  as a parameter and prints the result of  ( factorial).
#
# Note: If you fail to use recursion or fail to name your recursive function factorial or Factorial
# , you will get a score of .
#
# Input Format
#
# A single integer,  (the argument to pass to factorial).
#
# Constraints
#
# Your submission must contain a recursive function named factorial.
# Output Format
#
# Print a single integer denoting .
#
# Sample Input
#
# 3
# Sample Output
#6
#

# Lets start
def factorial(N):
    if N == 1:
        return 1
    else:
        return N * factorial(N - 1)

N = int(input())
print(factorial(N))