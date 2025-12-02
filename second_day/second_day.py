import csv

def read_range(path):
    with open(path, 'r', newline='') as f:
        line = csv.reader(f)
        for l in line:  
            l.sort(key=len)
            i = 0
            for s in l:
                while s[i]!='-':
                    i+=1
                low = int(s[:i])
                high = int(s[i+1:])
                yield low, high

def find_duplicates(low, high):
    sol = 0
    for n in range(low, high+1):
        s = str(n)
        if s[:len(s)//2] == s[len(s)//2:]:
            sol+=n
    return sol

def find_multiples(low, high):
    sol = 0
    for n in range(low, high+1):
        s = str(n)
        for i in range(len(s)//2, 0, -1):
            if s[:i] * (len(s) // i) == s:
                sol+=n
                break;
    return sol

def count(path, fn):
    f = read_range(path)
    sol = 0
    for l, h in f:
        sol += fn(l,h)
    return sol

if __name__ == "__main__":
    print('Sum is:', count('input.txt', find_duplicates))
    print('Sum is:', count('input.txt', find_multiples))