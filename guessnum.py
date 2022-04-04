import random
r = random.randint(1, 100)
count = 0   # 猜幾次的計數

while True:
	count += 1   # 這是一個快寫法等同於 count = count + 1
	num = input('請猜數字：')
	num = int(num)  #Casting
	if num == r:
		print('恭喜！猜中了！')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')
	