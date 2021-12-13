for i in open('data.txt'):
	if i[:len(i)-1] == '':
		continue
	lst.append(i[:-1])
tlst = [''.join(s) for s in zip(*lst)]
listgamma = lst
listepsilon = lst

#za gammu
for i in range (len(tlst)):
	if len(listgamma) == 1:
		break
	if tlst[i].count('1') >= tlst[i].count('0'):
		for ii in range (len(listgamma)):
			if listgamma[ii][i] == '0':
				listgamma.remove(listgamma[ii])
				ii = 0
	else:
		for ii in range (len(listgamma)):
			if listgamma[i] == '1':
				listgamma.remove(listgamma[ii])
#za epsilon

for i in range (len(tlst)):
	if len(listepsilon) == 1:
		break
	if tlst[i].count('1') > tlst[i].count('0'):
		for ii in range (len(listepsilon)):
			if listepsilon[i] == '1':
				listepsilon.remove(listepsilon[ii])
	else:
		for ii in range (len(listepsilon)):
			if listepsilon[i] == '0':
				listepsilon.remove(listepsilon[ii])
print(listgamma)
#print(listepsilon)
#print(int(listgamma, 2) * int(listepsilon, 2))
