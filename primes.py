from math import sqrt


def make_n_primes(n):
	"""creates a list of the first n primes"""
	primes = []
	num = 2
	prime_stat = "maybe"
	while len(primes) < n:
		for i in primes:
			if num % i == 0:
				num = num + 1
				prime_stat = "no"
				break
			else:
				None
		if prime_stat == "no":
			prime_stat = "maybe"
		else:
			primes.append(num)
			num = num + 1
			prime_stat = "maybe"
	return primes

def prime_decomp(n, primes):
	"""decomposes a number n into its prime factors"""
	if primes[-1] < sqrt(n):
		print "Caution, some primes may be missing from this decomposition"
	factors = []
	for prime in primes:
		while n % prime == 0:
			factors.append(prime)
			n = n / prime
		if n == 1:
			break
	return factors
