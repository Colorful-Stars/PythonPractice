def BinarySearch(array, t):
	low = 0
	height = len(array) - 1
	while low < height:
		mid = int((low + height)/2)
		if array[mid] < t:
			low = mid + 1
		elif array[mid] > t:
			height = mid - 1
		else:
			return array[mid]
	return -1
#前提是有序序列
if __name__ == '__main__':
	print(BinarySearch([1, 2, 3, 4, 10, 22, 35, 40], 4))