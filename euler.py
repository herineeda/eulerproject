sum = 0 
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0: 
        sum = sum + i  #sum이라는 변수를 통해 3의 배수와 5의 배수들을 다 더함.
    elif i % 3 == 0 and i % 5 == 0: 
        sum = sum - 1 #3의 배수와 5의 배수인 15의 배수는 1번씩 빼게 하여 중복되는 값들을 1번씩 빼줌.

print(sum)

#3의배수와 5의 배수를 모두 구해서 다 더하고 공배수 빼주는 원리
