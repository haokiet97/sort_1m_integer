import random
import struct

with open('numbers.dat','wb') as output:
     for i in xrange(1000000):
         u = random.randint(-(2**31), 2**31-1) # number
         b = struct.pack('i', u) # bytes
         output.write(b)
