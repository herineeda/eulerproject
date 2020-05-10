# 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.
# 이 때 10,001번째의 소수를 구하세요.

def isPrime(num):
    if num < 2 :
        return False
    if num == 2:
        return True
    k = 2
    while k < num:   #자기 자신보다 작은 수로 나눠서 한 번이라도 나눠지면 소수 아님. 
        if num % k == 0:
            return False
        k += 1
    return True


def doit():
    primes = []
    a = 2
    while len(primes) < 10001:
        if isPrime(a):
            primes.append(a)
        a += 1
    print(primes[-1])

check = 1
num = 2

while True:
    for i in range(2, num):
        if i > int(num / 2):
            #print(num)
            check += 1
            break
        if num % i == 0: break
    if check == 10001:
        print(num)
        break;
    num += 1