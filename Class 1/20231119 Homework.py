def is_prime(num):
    prime = True
    if int(num) < 2:
        prime = False
    for i in range(2, int(num)):
        if (int(num) % i) == 0:
            prime = False
            break
    print(prime)

num = input("Number: ")
is_prime(num)
