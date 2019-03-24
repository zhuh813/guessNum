import random #載入模組(Module)"random"

start = input('決定隨機數字範圍的開始值')
end = input('決定隨機數字範圍的結束值')

#Casting
start = int(start) 
end = int(end)

r = random.randint(start, end) #利用函式"randint"產生隨機整數 Rang:1~100
count = 0
while True:
	count +=1
	print('範圍: ',start, '-', end )
	n = input('請猜數字:')

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