# Problem 12
# Lets review
# Problem link:
#
# Objective
# Today we're expanding our knowledge of Strings and combining it with what we've already learned about loops.
# Check out the Tutorial tab for learning materials and an instructional video!
#
# Task
# Given a string, , of length  that is indexed from  to , print its even-indexed and odd-indexed characters as
# space-separated strings on a single line (see the Sample below for more detail).
#
# Note:  is considered to be an even index.
#
# Input Format
#
# The first line contains an integer,  (the number of test cases).
# Each line  of the  subsequent lines contain a String, .
#
# Constraints
#
# Output Format
#
# For each String  (where ), print 's even-indexed characters, followed by a space
# , followed by 's odd-indexed characters.
#
# Sample Input
#
# 2
# Hacker
# Rank
# Sample Output
#
# Hce akr
# Rn ak

# Lets Start

#for i in range(int(input())): s=input(); print(*["".join(s[::2]),"".join(s[1::2])])
s = input()
for i in range (int(input())):
    print(*["".join(s[::2]),"".join(s[1::2])])
