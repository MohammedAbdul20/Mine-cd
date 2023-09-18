def bubble_sort(array):
  n = len(array)
  for i in range(n):
    for j in range(0, n-i-1):
      if array[j] > array[j+1]:
        array[j], array[j+1] = array[j+1], array[j]

array = [6, 5, 3, 1, 8, 7, 2, 4]
bubble_sort(array)
print(array)
