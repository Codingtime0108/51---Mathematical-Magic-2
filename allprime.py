#program to calculate all prime numbers that have two digits
for num in range(2, 101):
    if num>1:
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            if 10 <= num <= 99:
                print(num,"is a prime number")