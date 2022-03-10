from numpy import array


def check_row(arr, i):
    flag = -1
    num = -1
    if arr[i, 0] == arr[i, 1]:
        num = arr[i, 0]
        flag = 2
    if arr[i, 0] == arr[i, 2]:
        num = arr[i, 0]
        flag = 1
    if arr[i, 1] == arr[i, 2]:
        num = arr[i, 1]
        flag = 0
    return num, flag


def check_column(arr, j):
    flag = -1
    num = -1
    if arr[0, j] == arr[1, j]:
        num = arr[0, j]
        flag = 2
    if arr[0, j] == arr[2, j]:
        num = arr[0, j]
        flag = 1
    if arr[1, j] == arr[2, j]:
        num = arr[1, j]
        flag = 0
    return num, flag


def check_main(arr):
    flag = -1
    num = -1
    if arr[0, 0] == arr[1, 1]:
        flag = 2
        num = arr[0, 0]
    if arr[1, 1] == arr[2, 2]:
        flag = 0
        num = arr[1, 1]
    if arr[0, 0] == arr[2, 2]:
        flag = 1
        num = arr[0, 0]
    return num, flag


def check_fu(arr):
    # flag代表行数
    flag = -1
    num = -1
    if arr[0, 2] == arr[1, 1]:
        flag = 2
        num = arr[0, 2]
    if arr[0, 2] == arr[2, 0]:
        flag = 1
        num = arr[0, 2]
    if arr[1, 1] == arr[2, 0]:
        flag = 0
        num = arr[1, 1]
    return num, flag


mat = array([[6, 4, 2], [5, 6, 2], [4, 6, 6]])
print(mat[0,0])
p1 = p2 = (-1, -1)
i = 0
while i <= 2:
    num, j = check_row(mat, i)
    if num != -1:
        if i == 0 and num == mat[i+1, j]:
            p1 = (0, j)
            p2 = (1, j)
            break
        if i == 2 and num == mat[i-1, j]:
            p1 = (1, j)
            p2 = (2, j)
            break
        if i == 1 and num == mat[i-1, j]:
            p1 = (0, j)
            p2 = (1, j)
            break
        if i == 1 and num == mat[i+1, j]:
            p1 = (1, j)
            p2 = (2, j)
            break
    i += 1

j = 0
while j <= 2:
    num, i = check_column(mat, j)
    if num != -1:
        if j == 0 and num == mat[i, j+1]:
            p1 = (i, 0)
            p2 = (i, 1)
            break
        if j == 2 and num == mat[i, j - 1]:
            p1 = (i, 1)
            p2 = (i, 2)
            break
        if j == 1 and num == mat[i, j-1]:
            p1 = (i, 0)
            p2 = (i, 1)
            break
        if j == 1 and num == mat[i, j+1]:
            p1 = (i, 1)
            p2 = (i, 2)
            break
    j += 1

num, i = check_main(mat)
if num != -1:
    if i == 0:
        if mat[0, 1] == num:
            p1 = (0, 0)
            p2 = (0, 1)
        if mat[1, 0] == num:
            p1 = (0, 0)
            p2 = (1, 0)
    if i == 2:
        if mat[2, 1] == num:
            p1 = (2, 1)
            p2 = (2, 2)
        if mat[1, 2] == num:
            p1 = (1, 2)
            p2 = (2, 2)
    if i == 1:
        if mat[0, 1] == num:
            p1 = (0, 1)
            p2 = (1, 1)
        if mat[1, 0] == num:
            p1 = (1, 0)
            p2 = (1, 1)
        if mat[1, 2] == num:
            p1 = (1, 1)
            p2 = (1, 2)
        if mat[2, 1] == num:
            p1 = (1, 1)
            p2 = (2, 1)

num, i = check_fu(mat)
if num != -1:
    if i == 0:
        if mat[0, 1] == num:
            p1 = (0, 1)
            p2 = (0, 2)
        if mat[1, 2] == num:
            p1 = (0, 2)
            p2 = (1, 2)
    if i == 2:
        if mat[2, 1] == num:
            p1 = (2, 0)
            p2 = (2, 1)
        if mat[1, 0] == num:
            p1 = (1, 0)
            p2 = (2, 0)
    if i == 1:
        if mat[0, 1] == num:
            p1 = (0, 0)
            p2 = (1, 1)
        if mat[1, 0] == num:
            p1 = (1, 0)
            p2 = (1, 1)
        if mat[1, 2] == num:
            p1 = (1, 1)
            p2 = (1, 2)
        if mat[2, 1] == num:
            p1 = (1, 1)
            p2 = (2, 1)

print(p1, p2)