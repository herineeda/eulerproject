sum = 0
mul = 0
for i in range(1, 101):
    sum += i
    result = i*i        #1-100까지 합의 제곱

for i in range(1, 101):
    i = i**2
    mul += i            #1-100까지 제곱의 합
print(sum*sum - mul)    


