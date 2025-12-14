import csv 

def lines(path):
    with open(path, 'r', newline='') as f:
        for line in csv.reader(f):
            if line:
                yield line[0]
            else:
                yield line


def st_to_int(s):
    i = 0
    res = 0
    while i<len(s) and s[i].isdigit():
        res = res*10 + int(s[i])
        i+=1
    return i, res

def compact(ranges):
    ranges.sort(key = lambda a: a[0])
    ranges.sort()
    compact_ranges = [ranges[0]]

    for l, h in ranges[1:]:
        if compact_ranges[-1][1]>=l:
            compact_ranges[-1][1] = max(h, compact_ranges[-1][1])
        else:
            compact_ranges.append([l,h])
    return compact_ranges

def check(avail):
    sol = 0
    for ingred in avail:
        for l, h in ranges:
            if l<=ingred<=h:
                sol+=1
                break;
    return sol

def count_ids(ranges):
    sol = 0
    for l, h in ranges:
        sol += h-l+1
    return sol


if __name__ == "__main__":

    ranges = []
    avail = []

    data = lines('input.txt')

    ranges_done = False

    for rng in data:
    
        if rng==[]:
            ranges_done = True
            continue;
        
        if not ranges_done:
            ind, first_num = st_to_int(rng)
            _, sec_num = st_to_int(rng[ind+1:])

            ranges.append([first_num, sec_num])

        if ranges_done:
            avail.append(int(rng))

    ranges = compact(ranges)

    print("The number of available fresh ingredients is:  ", check(avail))
    print("The number of available fresh IDs is: ", count_ids(ranges))