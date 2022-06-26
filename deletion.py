"""
    Deleting a element in an array
    Delete 3:
    Elements: 1, 2, 3, 4  
    Idx:      0, 1, 2, 3
    Final:    1, 2, 5, 3, 4

    Algorithm:    
        idx = 0 
        Loop i from 0, length-1
            if list[i]=element
                idx = i
                break
        Loop i from idx to length-2
            list[i] = list[i+1]
        list.pop()
"""
# Using inbuilt function
x = [1,2,3,4]
x.remove(3)
print(x)

# Using Algorithm
y = [1,2,3,4]
ele = 3
idx = 0

for i in range(0, len(y)):
    if y[i]==ele:
        idx = i
        break
for i in range(idx, len(y)-1):
    y[i] = y[i+1]
y.pop()
print(y)