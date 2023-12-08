# part 2
# your answer is too high 632976
RED = 12
GREEN = 13
BLUE = 14

ids_sum = 0
idsum=[]
f = open("input.txt", "r")


games = f.read()
games = games.splitlines()
for x in games:
	red_min=0
	blue_min=0
	green_min =0
	print('x', x)
	num, samples = x.split(':')
	game = num[5:]
	# replace new line in samples
	#samples = samples.strip()
	# samples.rstrip('\n')
	# print(samples)
	print('game: ', game)
	draws = samples.split(';')
	possible = True
	print('possible to true')
	print('draws', draws)
	for draw in draws:
		print('in draws loop')
		print('____________________________________')
		colors = draw.split(',')
		col_num = {}
		for color in colors:
			print('in colors loop')
			print('----------------------')
			
			print('')
			print('color', color, 'int', int(color[:3]))
			# green
			print(type(int(color[:3])))
			if color[-1] == "n":
				#col_num['green'] = int(color[:3])
				if int(color[:3]) > green_min:
					green_min = int(color[:3])
			#red
			elif color[-1] == "d":
				# col_num['red'] = int(color[:3])
				if int(color[:3]) > red_min:
					red_min = int(color[:3])
			#blue
			elif color[-1] == "e":
				# col_num['blue'] = int(color[:3])
				if int(color[:3]) > blue_min:
					blue_min = int(color[:3])

	powers = (green_min*blue_min*red_min)
	print('game', game, 'powers', powers)
	print('red_min ', red_min, 'blue_min ', blue_min, 'green_min ', green_min)
	ids_sum += (green_min*blue_min*red_min)
	#idsum.append(int(game))

print(ids_sum)
#print(idsum)
#ames 1, 2, and 5



