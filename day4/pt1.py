#draw = list(map(int, str(('drawnNum.txt').split(','))))
f = open('drawnNum.txt')
drawn = list(map(int, f.read().strip().split(',')))
cnt = 0
for line in open('boards.txt'):
	if line.strip() == '':
		continue
	boards = [[[
	print(boardline)
print(drawn)
