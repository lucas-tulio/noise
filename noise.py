import os
import time
import random
import string

f = open("data.txt", "w")

size = 5000

def write_random_data():
  s = ""
  for i in range(0, size):
    s = s + random.choice(string.printable)
  return s

def write_bytes(b):
  s = ""
  print("byte to write: " + str(b))
  for i in range(0, size):
    s = s + str(b)
  return s

s = write_bytes(0b100101)
f.write(s)
f.close()

start_time = time.time()
os.system("cat data.txt | padsp tee /dev/audio > /dev/null")
end_time = time.time()
print("played during: " + str(end_time - start_time))
