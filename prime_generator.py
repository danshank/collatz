def make_n_primes(n):
	primes = []
	num = 2
	prime_stat = "maybe"
	while len(primes) < n:
		print "Now evaluating %d" % num
		for i in primes:
			if num % i == 0:
				print "%d has a prime factor of %d and is not a prime" % (num, i)
				num = num + 1
				prime_stat = "no"
				break
			else:
				None
		if prime_stat == "no":
			prime_stat = "maybe"
		else:
			print "Adding %d to the list of primes" % num
			primes.append(num)
			num = num + 1
			prime_stat = "maybe"
	return primes