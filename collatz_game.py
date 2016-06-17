#from prime_generator import make_n_primes

def collatz_game(n):
	count = 0
	route = [n]
	while n != 1 and count < 1000:
		if n % 2 == 0:
			n = n / 2
			route.append(n)
		else:
			n = 3 * n + 1
			route.append(n)
		count = count + 1
		if count == 1000:
			print "terminating game early"
	return route