import time
start = time.time()
def isprime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    for i in range(2, int(num*0.5+1)):
        if num%i == 0:
            return False
    return True
L = list()
for i in range(10000):
    if isprime(i):
        L.append(i)
print(L)

for i in L:
    j = 2**i-1
    if isprime(j):
        print(time.time()-start)
        print(2**(i-1)*(j))
    i += 1
