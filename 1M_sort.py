import array

outf = open('gnv-sorted.dat', 'wb')

INT_MIN, INT_MAX = -(2**31), 2**31-1
size = int(2**32 / 8)
cutoffs = range(INT_MIN, INT_MAX, size)

# read file through and only collect values in our range
for i in range(len(cutoffs)):
  inf = open('numbers.dat', 'rb')
  min, max = cutoffs[i], cutoffs[i]+size
  a = array.array('i')
  while True:
    temp = array.array('i', inf.read(500000))
    if not temp:
      break
    for j in temp:
      if j >= min and j < max:
        a.append(j)

  # use a stable sort alg(Tim Sort) to sort and append to output
  array.array('i', sorted(a)).tofile(outf)

outf.close()
inf.close()
