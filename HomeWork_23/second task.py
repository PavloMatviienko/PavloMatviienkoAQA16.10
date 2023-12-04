array1 = [1, 2, 3, 4, 5]
array2 = [3, 4, 5, 6, 7]

intersection = list(filter(lambda x: x in array1, array2))
print(f"Intersection of arrays: {intersection}")