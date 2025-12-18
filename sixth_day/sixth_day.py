import csv 

def lines(path):
    with open(path, 'r', newline='') as f:
        for line in csv.reader(f):
            if line:
                yield line[0]

def st_to_list(st):
    res = []
    ind = 0

    while ind<len(st):
        num = 0
        if st[ind].isdigit(): 
            while ind<len(st) and st[ind].isdigit():
                num = num*10 + int(st[ind])
                ind+=1
            res.append(num)
        ind+=1
    return res

def ops_list(st):
    res = []
    ind = 0

    while ind<len(st):
        if st[ind]=='*':
            res.append('*')
        elif st[ind]=='+':
            res.append('+')
        ind+=1
    return res


def fun_choose(st):
    if st[0].isdigit():
        return st_to_list(st)
    else:
        return ops_list(st)

def get_first(num):
    if num<=9:
        return str(num), None
    else:
        return str(num[0]), int(str(num)[1:])

if __name__ == "__main__":
    data = lines('input.txt')
    stack = []

    for lst in data:
        stack.append(fun_choose(lst))

    ops = stack.pop()

    stack_copy = stack.copy()

    res = stack.pop()

    while stack:
        cur_nums = stack.pop()
        for i in range(len(cur_nums)):
            if ops[i] == '+':
                res[i] = res[i] + cur_nums[i]
            elif ops[i] == '*':
                res[i] = res[i] * cur_nums[i]
    
    print(sum(res))

