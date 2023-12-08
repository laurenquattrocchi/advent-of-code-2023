# your answer is too high 2634
RED = 12
GREEN = 13
BLUE = 14

ids_sum = 0
idsum=[]
f = open("input.txt", "r")

games = f.read()
games = games.splitlines()
for x in games:
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
			if color[-1] == "n":
				#col_num['green'] = int(color[:3])
				if int(color[:3]) > GREEN:
					print('setting possible to False: Green')
					possible = False
					break
			#red
			elif color[-1] == "d":
				# col_num['red'] = int(color[:3])
				if int(color[:3]) > RED:
					possible = False
					print('setting possible to False: red')
					break
			#blue
			elif color[-1] == "e":
				# col_num['blue'] = int(color[:3])
				if int(color[:3]) > BLUE:
					possible = False
					print('setting possible to False: blue')
					break
		if not possible:
			break

	if possible:
		ids_sum += int(game)
		idsum.append(int(game))

print(ids_sum)
print(idsum)
#ames 1, 2, and 5



