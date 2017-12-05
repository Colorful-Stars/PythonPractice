def selectionSort(s):
	for i in range(len(s)-1):
		k = i;
		for j in range(i, len(s)-1, 1):
			if s[j] < s[k]:
				k = j
		s[i], s[k] = s[k], s[i]
	return s

s = [4, 2, 10, 7, 23]

print(selectionSort(s))