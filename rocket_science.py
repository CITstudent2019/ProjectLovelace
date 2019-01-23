# Rocket Science
# author: kyle (SnoopLaserSnake)
# 01/06/19
# desc: calculates rocket fuel needed to leave a planet

# Saturn V
m = 250000 # mass of rocket w/o fuel [kg]
Ve = 2550 # escape velocity [m/s]
e = 2.7182818284590452353602874713527 # euler's number 

# returns rocket fuel needed to escape a given planet
# v is the escape velocity of a planet
def rocket_fuel(v):
	m_fuel = 0.0 
	exp = v / Ve
	m_fuel = m * (e**exp - 1)
	
	return m_fuel


print(str(rocket_fuel(Ve)) + " kg")
