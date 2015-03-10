import os
import time
import random
import string

size = 5000

def write_random_data():
  s = ""
  for i in range(0, size):
    s = s + random.choice(string.printable)
  return s

def write_bytes(b):
  s = ""
  print("playing: " + str(bin(b)[2:]).rjust(8, '0') + " (" + str(b) + ")")
  for i in range(0, size):
    s = s + str(b)
  return s

for i in range(0, 255):
  s = write_bytes(i)
  f = open("data.txt", "w")
  f.write(s)
  os.system("cat data.txt | padsp tee /dev/audio > /dev/null")
  f.close()
