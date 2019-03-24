import random #載入模組(Module)"random"

r = random.randint(1, 100) #利用函式"randint"產生隨機整數 Rang:1~100
count = 0
while True:
	count +=1
	n = input('輸入數字(0-100): ')
	n = int(n) #Casting
	if n == r:
		print('猜對了')
		print('這次你猜的第', count, '次' )
		break
	else:
		print('猜錯了')
		if n > r:
			print('比答案大')
		else:
			print('比答案小')

	print('這次你猜的第', count, '次' )