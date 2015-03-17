import os
import time
import random
import string
import math

buffer_size = 8192 # min rquired to play something

def write_random_data():
  s = ""
  for i in range(0, size):
    s = s + random.choice(string.printable)
  return s

def write_bytes(b):
  s = ""
  print("playing: " + b)
  for i in range(0, buffer_size // math.floor(math.sqrt(len(b)))):
    s = s + str(b)
  return s

for i in range(0, 4):
  
  s = write_bytes(random.sample(string.printable, 1)[0] + "0")
  with open("data.txt", "w") as f:
    f.write(s)
    f.write("0")
    os.system("cat data.txt | padsp tee /dev/audio > /dev/null")
