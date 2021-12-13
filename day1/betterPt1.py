cur = 1e9
total = 0
for i in open('data.txt'):
	if i.strip() == '':
		continue
	a = int(i.strip())
	if(a > cur):
		total += 1
	cur = a
print(total)
