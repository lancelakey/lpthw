#!/usr/bin/env python

i = 0
numbers = []

while i < 6:
  print "At the top i is %d" %i
  numbers.append(i)

  print "Numbers now: ", numbers

  i = i + 1

  print "At the bottom i is %d" %i

print "The numbers: "

for num in numbers:
  print num


