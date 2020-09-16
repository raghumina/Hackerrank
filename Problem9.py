# Problem 9
# Problem name = Prime XOR
# Link of the problem: https://www.hackerrank.com/challenges/prime-xor/problem
#
# Lets start
# Penny has an array of  integers, .
# She wants to find the number of unique multisets she can form using elements from
# the array such that the bitwise XOR of all the elements of the multiset is a prime number.
# Recall that a multiset is a set which can contain duplicate elements.
#
# Given  queries where each query consists of an array of integers,
# can you help Penny find and print the number of valid multisets for each array?
# As these values can be quite large, modulo each answer by  before printing it on a new line.
#
# Input Format
#
# The first line contains a single integer, , denoting the number of queries.
# The  subsequent lines describe each query in the following format:
#
# The first line contains a single integer, , denoting the number of integers in the array.
# The second line contains  space-separated integers describing the respective values of .
# Constraints
#
# Output Format
#
# On a new line for each query, print a single integer denoting the number of unique multisets
# Penny can construct using numbers from the array such that the bitwise XOR of all the multiset's elements is prime.
# As this value is quite large, your answer must be modulo .
#
# Sample Input
#
# 1
# 3
# 3511 3671 4153
# Sample Output
#
# 4
# Explanation
#
# The valid multisets are:
#
#  is prime.
#  is prime.
#  is prime.
# , which is prime.
# Because there are four valid multisets, we print the value of  on a new line.
