"""
    Inserting a element in an array
    Insert 5 at idx = 2:
    Elements: 1, 2, 3, 4  
    Idx:      0, 1, 2, 3
    Final:    1, 2, 5, 3, 4

    Algorithm:    

        Loop i from length-1 to idx:
            list[i+1] = list[i]
        list[idx] = element
"""
#Using inbuilt function (insert)

x = [1,2,3,4]
l = len(x)
ele = 5
idx = 2

x.insert(idx, ele)
print(x)

# Algorithm implementation

for i in range(l-2,idx-1,-1):
    temp = x[i+1]
    x[i+1] = x[i]
x[idx] = ele
x.append(temp)
print(x)


"""Train Model"""
