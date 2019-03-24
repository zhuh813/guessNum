import random #載入模組(Module)"random"

r = random.randint(1, 100) #利用函式"randint"產生隨機整數 Rang:1~100

while True:
	num = input('輸入數字(0-100):')
	num = int(n) #Casting
	if num == r:
		print('猜對了')
		break
	else:
		print('猜錯了')
		if num > r:
			print('比答案大')
		else:
			print('比答案小')