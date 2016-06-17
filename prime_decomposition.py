from math import sqrt
from prime_generator import make_n_primes

def prime_decomp(n, primes):
	if primes[-1] < sqrt(n):
		print "Caution, some primes may be missing from this decomposition"
	factors = []
	current = 1
	for prime in primes:
		if n % prime == 0:
			factors.append(prime)
			current = current * prime
		else:
			None
	if factors == []:
		print "This number might be prime, no factors found"
		return factors
	elif current != n:
		print "Some duplicate factors, prime factors only multiply up to %d, address this issue later" % current
	else:
		print "All factors are independent"
	#print "%d has the following prime factorization" % n
	return factors

primes = make_n_primes(1000)
factor_list = prime_decomp(598, primes)
print factor_list