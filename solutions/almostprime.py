num = int(input())
almost_prime=0
def factorsnum(number):
    factors = []
    for i in range(1, number+1):
        if number % i == 0:
            factors.append(i)
    return factors

