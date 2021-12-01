cur = 1e9
total = 0
with open('data.txt') as file:
	lines = file.readlines()
	lines = [line.strip() for line in lines]
	del lines[-1:]
	for line in lines:
		if cur < int(line):
			total = total +1
		cur = int(line)
print(total)
