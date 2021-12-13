depth = 0
forward = 0
aim = 0
for i in open('data.txt'):
	tmp = i.strip()
	if tmp == '':
		continue
	if 'down' in i:
		aim +=  int(tmp[4::1].strip())
		#depth += int(tmp[4::1].strip())

	if 'up' in i:
		aim -=  int(tmp[2::1].strip())
		#depth -= int(tmp[2::1].strip())

	if 'forward' in i:
		forward += int(tmp[7::1].strip())
		depth += aim * int(tmp[7::1].strip())

total = depth * forward
print("aim here:")
print(aim)
print("total here:")
print(total)
