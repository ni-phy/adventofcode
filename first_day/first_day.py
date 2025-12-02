import csv 

def lines(path):
    with open(path, 'r', newline='') as f:
        for line in csv.reader(f):
            s = line[0]
            sign = 1
            if s[0] == 'L':
                sign = -1
            steps = int(s[1:]) 
            yield steps*sign


def landing_zero(filename, pos):
    gen = lines(filename)
    score = 0
    for step in gen:
        if step > 0:
            pos += step % 100
        else:
            pos -= abs(step) % 100
        
        if pos < 0:
            pos += 100
        elif pos >= 100:
            pos -= 100
        
        if pos == 0:
            score += 1
    return score

def passing_zero(filename, pos):
    gen = lines(filename)
    score = 0
    for step in gen:
        old_pos = pos
        if step > 0:
            pos += (step % 100)
        else:
            pos -= (abs(step) % 100)

        if pos < 0:
            pos += 100
            if not old_pos==0: 
                score+=1
        elif pos >= 100:
            pos -= 100
            if not old_pos==0: 
                score+=1
        elif pos==0 and old_pos!=0:
            score+=1
        
        score += abs(step) // 100
        
    return score

if __name__ == "__main__":
    print("Landing on 0:", landing_zero("input.txt", 50))
    print("Passing 0:", passing_zero("input.txt", 50))