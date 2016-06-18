from math import sqrt
from prime_generator import make_n_primes

def prime_decomp(n, primes):
	if primes[-1] < sqrt(n):
		print "Caution, some primes may be missing from this decomposition"
	factors = []
	current = 1
	remainder = n
	for prime in primes:
		if current == n:
#			print "All done decomposing"
			break
		while remainder % prime == 0:
			factors.append(prime)
			current = current * prime
			remainder = remainder / prime
#		else:
#			None
#	if factors == []:
#		print "This number might be prime, no factors found"
#		return factors
	if current != n:
#		print "Some duplicate factors, prime factors only multiply up to %d, address this issue later" % current
		print "Something went wrong, compare %d to the product the factors" % current
#	else:
#		print "All factors are independent"
	#print "%d has the following prime factorization" % n
	return factors

primes = make_n_primes(100)
#for n in range(2, 10):
#	print n
#	decomp = prime_decomp(n, primes)
#	print decomp

print prime_decomp(72, primes)