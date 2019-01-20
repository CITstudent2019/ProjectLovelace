# input: star's luminosity, distance from star
import math 

def habitable_exoplanet(lumins, radius):
	habitability = ''
	
	inner_radius = math.sqrt(lumins / 1.1)
	outer_radius = math.sqrt(lumins / 0.54)
	
	if (radius >= inner_radius and radius <= outer_radius):
		habitability = 'just right'
	elif radius < inner_radius:
		habitability = 'too hot'
	elif radius > outer_radius:
		habitability = 'too cold'
		
	return habitability

