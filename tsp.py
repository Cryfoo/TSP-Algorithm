dist3 = [
    [0, 26, 29, 11, 8, 25, 49, 4, 33, 42, 50, 27, 11, 33, 5, 4, 8, 21, 30, 49],
    [26, 0, 24, 19, 21, 3, 25, 12, 36, 7, 46, 8, 18, 9, 42, 50, 12, 16, 38, 39],
    [29, 24, 0, 17, 43, 25, 42, 46, 31, 49, 9, 9, 13, 30, 33, 28, 9, 5, 21, 42],
    [11, 19, 17, 0, 49, 7, 21, 49, 17, 18, 29, 10, 41, 12, 4, 35, 49, 7, 44, 38],
    [8, 21, 43, 49, 0, 12, 30, 29, 35, 50, 37, 45, 3, 40, 47, 32, 9, 34, 22, 42],
    [25, 3, 25, 7, 12, 0, 36, 12, 6, 36, 14, 2, 42, 18, 39, 19, 15, 37, 28, 5],
    [49, 25, 42, 21, 30, 36, 0, 12, 17, 24, 22, 20, 16, 29, 46, 30, 34, 5, 38, 9],
    [4, 12, 46, 49, 29, 12, 12, 0, 26, 19, 41, 28, 40, 36, 30, 12, 4, 38, 46, 27],
    [33, 36, 31, 17, 35, 6, 17, 26, 0, 27, 24, 44, 33, 46, 23, 22, 30, 35, 36, 19],
    [42, 7, 49, 18, 50, 36, 24, 19, 27, 0, 3, 6, 32, 27, 18, 43, 33, 45, 26, 31],
    [50, 46, 9, 29, 37, 14, 22, 41, 24, 3, 0, 44, 43, 47, 26, 28, 20, 12, 6, 24],
    [27, 8, 9, 10, 45, 2, 20, 28, 44, 6, 44, 0, 6, 3, 33, 25, 9, 12, 5, 46],
    [11, 18, 13, 41, 3, 42, 16, 40, 33, 32, 43, 6, 0, 36, 47, 17, 31, 21, 3, 38],
    [33, 9, 30, 12, 40, 18, 29, 36, 46, 27, 47, 3, 36, 0, 1, 5, 23, 32, 49, 20],
    [5, 42, 33, 4, 47, 39, 46, 30, 23, 18, 26, 33, 47, 1, 0, 2, 7, 48, 5, 43],
    [4, 50, 28, 35, 32, 19, 30, 12, 22, 43, 28, 25, 17, 5, 2, 0, 18, 28, 35, 50],
    [8, 12, 9, 49, 9, 15, 34, 4, 30, 33, 20, 9, 31, 23, 7, 18, 0, 27, 44, 23],
    [21, 16, 5, 7, 34, 37, 5, 38, 35, 45, 12, 12, 21, 32, 48, 28, 27, 0, 5, 30],
    [30, 38, 21, 44, 22, 28, 38, 46, 36, 26, 6, 5, 3, 49, 5, 35, 44, 5, 0, 49],
    [49, 39, 42, 38, 42, 5, 9, 27, 19, 31, 24, 46, 38, 20, 43, 50, 23, 30, 49, 0],
    ]

# dist3 = [
#      [0, 5, 9, 8, 10, 9, 2, 9, 9, 2], 
#      [5, 0, 7, 9, 3, 7, 7, 5, 2, 2], 
#      [9, 7, 0, 4, 9, 7, 6, 8, 8, 10], 
#      [8, 9, 4, 0, 10, 2, 3, 2, 9, 3], 
#      [10, 3, 9, 10, 0, 5, 5, 6, 6, 1], 
#      [9, 7, 7, 2, 5, 0, 10, 9, 4, 1], 
#      [2, 7, 6, 3, 5, 10, 0, 5, 3, 8], 
#      [9, 5, 8, 2, 6, 9, 5, 0, 8, 7], 
#      [9, 2, 8, 9, 6, 4, 3, 8, 0, 4], 
#      [2, 2, 10, 3, 1, 1, 8, 7, 4, 0], 
#     ]

# dist3 = [
# 	 [0, 2, 3, 1, 5, i],
# 	 [2, 0, 3, 2, 1, 2],
# 	 [3, 3, 0, 1, 4, 3],
# 	 [1, 2, 1, 0, 5, 1],
# 	 [5, 1, 4, 5, 0, 5],
# 	 [i, 2, 3, 1, 5, i]
# 	]

# NN sample solution
path = [1]
value = 0
counter = len(dist3) - 1
index = 0
i = float('inf')

while counter > 0:
	temp1 = i
	temp2 = index
	for j in range(0, len(dist3[temp2])):
		if dist3[temp2][j] != 0 and dist3[temp2][j] < temp1 and (j+1) not in path:
			temp1 = dist3[temp2][j]
			index = j
	value += temp1
	path.append(index + 1)
	counter -= 1

place = path.pop()
path.append(place)
path.append(1)
value += dist3[place-1][0]
print "One solution using NN algorithm"
print path
print "value = " + str(value)

# optimal solution
newPath = [1]
newVal = 0

def tsp(curr, path, value, newPath, newVal, ans):
    if len(newPath) == (len(path)-1):
        place = newPath.pop()
        newPath.append(place)
        newVal += dist3[place-1][0]
        if newVal < ans['value']:
            temp = []
            for i in newPath:
                temp.append(i)
            temp.append(1)
            ans['path'] = temp
            ans['value'] = newVal
            print ans
        newVal -= dist3[place-1][0]
        return ans
    else:
        for j in range(0, len(dist3[curr])):
            if dist3[curr][j] != 0 and (j+1) not in newPath:
                newVal += dist3[curr][j]
                if newVal < value:
                    newPath.append(j+1)
                    ans = tsp(j, path, value, newPath, newVal, ans)
                    newPath.pop()
                newVal -= dist3[curr][j]
        return ans

ans = {'path': [], 'value': value}
ans = tsp(0, path, value, newPath, newVal, ans)

print "Optimal solution using branch and bound"
print ans['path']
print "value = " + str(ans['value'])