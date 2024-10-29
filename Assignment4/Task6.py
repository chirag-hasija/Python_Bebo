# A = {1,2,3}
# B = {3,4,5}
# c = A.symmetric_difference(B)
# print(c)
A = [1, 2, 3]
B = [3, 4, 5]
C = []
for i in A:
    if i not in B:
        C.append(i)
for i in B:
    if i not in A:
        C.append(i)
print(C)
