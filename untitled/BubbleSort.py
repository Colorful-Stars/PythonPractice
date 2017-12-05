def BubbleSort(s):
	for i in range(len(s) - 1):
		for j in range(len(s) - 1, 0, -1):
			if s[j] < s[j-1]:
				s[j], s[j-1] = s[j-1], s[j]
	return s

s = [4, 2, 10, 7, 23]

print(BubbleSort(s))
