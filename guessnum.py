import random
r = random.randint(1, 100)

while True:
	num = input('請猜數字：')
	num = int(num)  #Casting
	if num == r:
		print('恭喜！猜中了！')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	