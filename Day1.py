#PART 1
#depths = [199,200,208,210,200,207,240,269,260,263]
with open("day1.txt") as file:
    lines = file.readlines()
    depths = [int(line.rstrip()) for line in lines]

numOfIncreases = 0

for count, value in enumerate(depths):
    if count == 0:
        continue
    
    if value > depths[count-1]:
        numOfIncreases+=1

print("The number of depth increases are: " + str(numOfIncreases))

# PART 2
#depths = [199,200,208,210,200,207,240,269,260,263]

from itertools import islice

def window(seq, n=2):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

window_size = 3

newDepths = []
for i in range(len(depths) - window_size + 1):
    temp = depths[i: i + window_size]
    newDepths.append(sum(temp))

numOfIncreases = 0

for count, value in enumerate(newDepths):
    if count == 0:
        continue
    
    if value > newDepths[count-1]:
        numOfIncreases+=1

print("The number of depth increases are: " + str(numOfIncreases))