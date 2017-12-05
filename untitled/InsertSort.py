def InsertSort(s):
	for i in range(1, len(s)):
		n = s[i]
		j = i - 1
		while j > 0 and s[j] >= n:
			s[j] = s[j - 1]
			j -= 1
		s[j] = n	
	return s

s = [4, 2, 10, 7, 23]
#i = 1/***2,4,10,7,23
#i = 2/***
print(InsertSort(s))