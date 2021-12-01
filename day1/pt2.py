cur = 1e9
total = 0
with open('data.txt') as file:
	lines = file.readlines()
	lines = [int(line.strip()) for line in lines if line.strip() != '']

	for x in range (len(lines) -2):
		s = lines[x] + lines[x+1] + lines[x +2]
		if s > cur:
			total += 1
		cur = s
print(total)
