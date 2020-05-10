num1 = 1 
num2 = 2
num3 = 0
fibsum = 2

while num3 <= 4000000: 
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    if num3 % 2 == 0:
        fibsum = fibsum + num3 

print(fibsum)