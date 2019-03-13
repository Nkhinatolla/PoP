import math

def main():
	#      0      0.1444 0.8444
	line_new = '{:<10} {:<10} {:<10}'.format('Degree', 'Sin', 'Cos')
	# 2.450000
	print(line_new)
	for deg in range(0, 361, 10):
		sin = '%.4f' % math.sin(math.radians(deg))
		cos = '%.4f' % math.cos(math.radians(deg))
		line_new = '{:<10} {:<10} {:<10}'.format(deg, sin, cos)
		print(line_new)
main()
