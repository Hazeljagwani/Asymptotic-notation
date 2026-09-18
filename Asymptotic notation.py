# 01-big-o-notation.py
# Topic: Big-O - each growth patternhas an official name
# Formula, Loop, Double Loop. Today each gets its Big-O name

n = 10

guess = input("Double Loop at n = 10 checks n x n pairs. How many? ")

input("Formula: one calcution, done. Press ENTER to run ")
steps = 1
print(" steps =", steps, " -> O(1) constant time -> steps never change")

input("Loop: one step per item. Press ENTER to run")
steps = 0
for i in range(n):
    steps += 1
print(" steps =", steps, " -> O(1) linear time -> steps grow with n")

input("Double Loop: Checks every pair. Pres ENTER to run ")
steps = 0 
for i in range(n):
    for j in range(n):
        steps += 1
print(" steps =", steps, " your guess: ", guess, " -> O(n^2) quadratic time")

input("Two more notifications. Press ENTER ")
print("Big Omega Omega -> best case lower bound")
print("Big Theta Theta -> exact bound (worst = best)")