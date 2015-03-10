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
  f = open("data.txt", "w")
  f.write(s)
  f.write("0")
  #start_time = time.time()
  os.system("cat data.txt | padsp tee /dev/audio > /dev/null")
  #print("played during: " + str(time.time() - start_time))
  f.close()
