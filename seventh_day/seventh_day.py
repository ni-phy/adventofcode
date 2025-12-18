import csv 
from functools import cache

def lines(path):
    with open(path, 'r', newline='') as f:
        for line in csv.reader(f):
            if line:
                yield line[0]

def find_s(st):
    i = 0
    while st[i] != 'S':
        i+=1
    return i

def find_next(ind, st):
    # print(ind, st[ind]=='')
    if st[ind] == '.':
        return [ind]
    else:
        return [ind-1,ind+1]

@cache
def bfs(point, ind):
    if ind == len(matrix) - 1:
        return 1

    new = find_next(point, matrix[ind+1])
    if len(new)==1:
        return bfs(new[0], ind+1)
    else:
        return bfs(new[0], ind+1)  + bfs(new[1], ind+1)

if __name__ == "__main__":

    ## This is basically bfs
    data = lines('input.txt')
    
    start = find_s(next(data))

    stack = [start]
    sol = 0

    for line in data:
        to_test = len(stack)
        new_beams = set()
        
        if sol<6:
            print(line)
        for _ in range(to_test):
            coming_beam = stack.pop(0)
            next = find_next(coming_beam, line)
            sol += len(next) - 1
            for n in next:
                if n not in new_beams:
                    stack.append(n)
                    new_beams.add(n)
     
    print(sol)

    ## Then use bfs for the second problem

    data = lines('input.txt')
    
    matrix = [i for i in data]
    start = find_s(matrix[0])

    print(bfs(start, 1))
