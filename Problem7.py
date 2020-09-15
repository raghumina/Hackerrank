# Problem 7
# Print Function
# Problem Link : https://www.hackerrank.com/challenges/python-print/problem?h_r=next-challenge&h_v=zen

# Lets start
#
# The included code stub will read an integer, , from STDIN.
#
# Without using any string methods, try to print the following:
#
#
# Note that "" represents the consecutive values in between.
#
# Example
#
# Print the string .
#
# Input Format
#
# The first line contains an integer .
#
# Constraints
#
#
# Output Format
#
# Print the list of integers from  through  as a string, without spaces.
#
# Sample Input 0
#
# 3
# Sample Output 0
#
# 123
i = 0
n = int(input())
for i in range(n):
    i = i + 1
    print(i, end="")
