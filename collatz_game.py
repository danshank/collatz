from primes import make_n_primes
from primes import prime_decomp


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

def route_decomp(route, prime_list):
	decomp = []
	for stop in route:
		decomp.append(prime_decomp(stop, prime_list))
	return decomp

prime_list = make_n_primes(1000)
path = collatz_game(700)
path_decomp = route_decomp(path, prime_list)
print path
print path_decomp