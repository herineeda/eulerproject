num = 600851475143 
result = 0
i = 2

while i <= num:
    if num % i == 0:
        if result < i: #결과값이 i 보다 작으면 i를 result 값에 
            result = i
        num = num/i
    else: 
        i = i + 1
print (result)
