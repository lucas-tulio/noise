import os
import time
import random
import string

f = open("data.txt", "w")

size = 10000
s = ""
for i in range(0, size):
  s = s + random.choice(string.printable)

f.write(s)
f.close()

start_time = time.time()
os.system("cat data.txt | padsp tee /dev/audio > /dev/null")
end_time = time.time()
print("played during: " + str(end_time - start_time))
