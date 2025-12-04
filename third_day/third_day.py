import csv 

def lines(path):
    with open(path, 'r', newline='') as f:
        for line in csv.reader(f):
            yield line[0]


def find_max(num):

    idx, temp_ind = 0, 0 ##use idk to start from 
    dig = -1

    for char in num:
        if int(char)>dig:
            dig = int(char)
            idx = temp_ind
        
        ## can't be larger than 9 so break
        if dig == 9:
            break;
        
        temp_ind+=1
    
    return idx, dig
    
            

def find_two_digs(filename):
    gen = lines(filename)
    res = 0
    for num in gen:
        idx, first_dig = find_max(num[:-1])
        idx, sec_dig = find_max(num[idx+1:])
        res+= first_dig*10 + sec_dig
    return res

def find_n_digs(filename, n):
    gen = lines(filename)
    res = 0
    for num in gen:
        digs_added = 0
        volt = 0
        idx = 0
        while digs_added<n:
            ##find up to what index we can pick to maintain n digs
            lim = len(num) - (n - digs_added)+1 
            new_idx, dig = find_max(num[idx: lim])

            ##we can only pick from after the last dig
            idx += new_idx+1
            volt = volt*10 + dig
            digs_added+=1

        res+=volt  
        
    return res



if __name__ == "__main__":
    print('The total voltage is: ', find_n_digs('input.txt', 2))
    print('The total voltage is: ', find_n_digs('input.txt', 12))
    