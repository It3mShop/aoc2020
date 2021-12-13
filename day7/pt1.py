pos = list(map(int ,open('input.txt').readline().strip().split(',')))
top = pos[0]
for i in range(len(pos)):
	if(pos[i] > top):
		top = pos[i]
#print(top)
bestsum = 1e9

for i in range(top):
	tmpsum = 0
	for ii in range(len(pos)):
		vtmpsum = abs(i - pos[ii])
		tmpsum += (vtmpsum * (vtmpsum +1))/2
	if tmpsum < bestsum:
		bestsum = tmpsum
print(bestsum)
