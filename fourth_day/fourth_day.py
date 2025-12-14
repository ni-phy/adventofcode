import csv 

def lines(path):
    with open(path, 'r', newline='') as f:
        for line in csv.reader(f):
            yield line
            
paper_rolls = lines('input.txt')
arr = [[j for j in i[0]] for i in paper_rolls]
n = len(arr)
m = len(arr[0])

def rep(arr):
    res = 0
    for i in range(0,n):
        for j in range(0,n):
            if arr[i][j] != '@':
                continue;

            surround = [(i-1, j-1), (i-1,j), (i-1, j+1), (i,j-1), (i,j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]
            num = 0
            for x, y in surround:
                if (0<=x<n and 0<=y<m) and arr[x][y]=='@':
                    num+=1
            
            if num<4:
                arr[i][j] = 'X'
                res+=1
    return res

sol = 0
prev_res = rep(arr)

while prev_res != 0:
    sol += prev_res
    prev_res = rep(arr)

    print(sol)
