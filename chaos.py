# author: kyle bogart
# date: 1-21-2019
# desc: choas, calculates a logistic map using formula Xn+1 = rXn(1 - Xn)

def logistic_map(r):
	x = [0.5]
	
	while len(x) <= 50:
		pop = (r * x[-1]) * (1 - x[-1])
		x.append(pop)
		
	return x

print(logistic_map(2.81))
