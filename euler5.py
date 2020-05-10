n = 20
li = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20] #2-10까지는 자동으로 나눠떨어짐

while True: 
    for i in li:
        if n % i != 0: 
            break
    if i == 20:
        print(n)
        break

    n += 20

# a = 0

# while True:
#     a += 1
#     if a % 1 == 0 and a % 2 == 0 and a % 3 == 0 and a % 4 == 0 and a % 5 == 0 and a % 7 == 0 and a % 8 == 0 and a % 9 == 0 and a % 10 == 0 and a % 11 == 0 and a % 12 == 0 and a % 13 == 0 and a % 14 == 0 and a % 15 == 0 and a % 16 == 0 and a % 17 == 0 and a % 18 == 0 and a % 19 == 0 and a %20 ==0:
#         break

# print(a)
