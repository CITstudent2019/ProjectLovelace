# author: kyle bogart
# date: 1-21-2019
# desc: choas, calculates a logistic map using formula Xn+1 = rXn(1 - Xn)

# 0 < r < 4
def logistic_map(r):
	# each value in x is the population size each year
	# 1 is 100% of the maximum possible population, .5 is 50%, etc.
	x = [0.5]
	
	while len(x) <= 50:
		pop = (r * x[-1]) * (1 - x[-1])
		x.append(pop)
		
	return x

print(logistic_map(2.81))
