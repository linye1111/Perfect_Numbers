import time
start = time.time()
k = 3

def factors(num):
    L = list()
    factors = list()
    i = 2
    while i < num:
        if num%i == 0:
            L.append(i)
            num /= i
            i = 2
            continue
        if i == num-1:
            L.append(num)
        i += 1
    i = 0
    _len = len(L)
    while i < _len-1:
        j = i+1
        p = L[i]
        while j < _len and _len > 2:
            y = L[i]*L[j]
            if y not in L:
                L.append(y)
            if not (i == 0 and j==_len-1):
                p*=L[j]
                if p not in L:
                    L.append(p)
            j+=1
        i+=1
    for x in L:
        if x not in factors:
            factors.append(x)
    return [1]+factors


i = 3
print(6)
while True:
    if not i%9 == 1:
        i += k 
        k += 1
        continue
    L = factors(i)    
    if sum(L) == i:
        print(time.time() - start)
        print(i)
    i += k 
    k += 1
