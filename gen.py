import sys
from random import random, choice

names = []

for line in open("./names.txt","read"):
  names.append(line.split("\n")[0])

while True:

  number = random()

  if number < 0.1:
    n_names = 1
  elif number > 0.9:
    n_names = 3
  else:
    n_names = 2

  full_name = ""

  for i in xrange(n_names):
    full_name = full_name + choice(names) + " "

  print
  enter = raw_input("Press enter to generate name (or type \"exit\" to quit)\n")
  if enter == "exit":
    print
    sys.exit()
  else:
    print full_name

