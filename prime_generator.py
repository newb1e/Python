

def gen_next_prime():
    #pass
    n = 0
    while True:
        n += 1
        if (check_prime(n)):
            yield n

def check_prime(n):
    if n <= 3:
        return n > 1
    elif n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n%i == 0 or n%(i+2) == 0:
            return False
        i = i+6
    return True

g = gen_next_prime()

while True:
    key_input = input("press 'y' to get next prime ('n' to exit): ")

    if key_input == "y":
        print(next(g))
    elif key_input == "n":
        break
    else:
        print("Error! Invalid Input!")
