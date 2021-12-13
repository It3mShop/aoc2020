lst = ['item', 'item', 'item', 'item', 'item', 'item', 'item', 'item', 'item', 'item', ]
for item in lst:
	if item[1] == 't':
		lst.remove(item)
		item -= 1
print(lst)
