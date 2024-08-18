numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
a = len(numbers) + 1
for i in numbers:
    for j in range (2, a):
        if i == j:
            primes.append(i)
        elif i % j == 0:
            not_primes.append(i)
            break
print('Primes: ', primes)
print('Not Primes: ', not_primes)
