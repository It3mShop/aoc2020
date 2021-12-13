lst =[]
for i in open('data.txt'):
	if i[:len(i)-1] == '':
		continue
	lst.append(i[:-1])
tlst = [''.join(s) for s in zip(*lst)]

binstr = ''
for line in tlst:
	if line.count('1') > line.count('0'):
		binstr += '1'
	else:
		binstr += '0'
print(binstr)
gamma = int(binstr, 2)
epsilon = int(''.join('1' if x == '0' else '0' for x in binstr), 2)
print(gamma, epsilon)
print (gamma * epsilon)
