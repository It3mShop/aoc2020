lst = []
for i in open('data.txt'):
	if i.strip() == '':
		continue
	lst.append(i.strip())
lstgam = lst
lsteps = lst
l = len(lst[0])
print(l)
#for i in lst:
#	lsteps.append(i)
for i in range(12):
	if len(lstgam) == 1:
		break
	zcnt = 0
	ocnt = 0

	for line in lstgam:
		if line[i] == '1':
			ocnt += 1
		if line[i] == '0':
			zcnt += 1
	tbd = []
	for line in lstgam:
		if ocnt >= zcnt:
			if line[i] == '0':
				tbd.append(line)
		else:
			if line[i] == '1':
				tbd.append(line)
	for i in tbd:
		lstgam.remove(i)

for i in range(12):
	if len(lsteps) == 1:
		break
	zcnt = 0
	ocnt = 0

	for line in lsteps:
		if line[i] == '1':
			ocnt += 1
		if line[i] == '0':
			zcnt += 1
	tbd = []
	for line in lsteps:
		if ocnt < zcnt:
			if line[i] == '0':
				tbd.append(line)
		else:
			if line[i] == '1':
				tbd.append(line)
	for i in tbd:
		lsteps.remove(i)
				
print(lstgam)
print(lsteps)
print(int(lstgam[0], 2) * int(lsteps[0], 2))
