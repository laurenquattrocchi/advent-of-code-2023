#12,38,15,77 = 142
# part 1
f = open("input.txt", "r")
total =0
nums = []
for x in f:
  # print([*x])
  print(x)
  start = 0
  # minus 2 b/c last char is \n character
  end = len(x)-2
  num = ''
  digits=['0','1','2','3','4','5','6','7','8','9']
  for i in x:
  	if i in digits:
  		num += i
  		break
  for i in range(len(x)-1,-1, -1):
  	if x[i] in digits:
  		num += x[i]
  		break
  # while start<=end:
  # 	if x[start] in digits:
  # 		num += x[start]
  # 	if x[end] in digits:
  # 		num += x[end]
  # 	if len(num)>= 2:
  # 		break
  # 	start+=1
  # 	end -=1
  # if len(num) == 1:
  # 	num = num+num
  print(num)
  total += int(num)

print(total)