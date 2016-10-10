import math
import random
import blist
import bisect
import time

def mallows(q,n):
#This function generates a permutation according to Mallows(q, n)
    permutation = blist.blist([1])
    denom = math.log(q)
    m2 = math.floor(2/(1-q))
    m3 = math.floor(3/(1-q))
    p = 1-q**m2
    threshold = math.floor(10*math.log(0.1)/denom)
    def apa(i):
        offset = 0
        u = random.random()
        while (i > threshold and u > p):
            offset += m2
            i-=m2
            u = random.random()
        while (i<= threshold and i >m3 and u > (p/(1-q**i))):
            offset += m2
            i-=m2
            u = random.random()
        j = m2 if i>m3 else i
        h = math.floor(math.log(1-random.random()*(1-q**j))/denom)
        return (offset + h)
    if n > m3:
        for t in range(2,m3):
            permutation.insert(math.floor(math.log(1-random.random()*(1-q**t))/denom),t)
        for t in range(m3,n+1):
            permutation.insert(apa(t),t)
    else:
        for t in range(2,n+1):
            permutation.insert(math.floor(math.log(1-random.random()*(1-q**t))/denom),t)
    return(list(permutation)[::-1])

def lis(permutation):
# This function returns the length of LIS of a permutation.
    ps = permutation[0:1]
    for i in range(1,n):
        po = bisect.bisect(ps, permutation[i])
        if po< len(ps):
            ps[po]= permutation[i]
        else:
            ps.append(permutation[i])
    return len(ps)

q = float(input('Enter q:'))
n = int(input('Enter n:'))
cn = int(input('Sample#:'))

start_time=time.time()

s =[]
for i in range(cn):
    s.append(lis(mallows(q, n)))

print(time.time()-start_time)

f= open('q'+ str(q*1000000)[:6] +'e'+str(math.log(n,10)+0.1)[0]+'.txt','w')
for item in s:
    f.write("%s\n" % item)
f.close()
