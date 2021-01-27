import random
import os
j = True 
while j :
	k1 = 1
	k2 = 100
	menu = '''
1.random namber min:1 max:100
2.random namber min:1 max:1000
3.your choise

'''

	print(menu)
	ch = input(">>")
	if ch == "2":
			k2 = 1000
	if ch == "3":
			k1 = int(input("Min number: "))
			k2 = int(input("Max number: "))
	os.system('cls')
	y = True
	c = (random.randint(k1, k2))
	print ("Угадай число от 1 до 100")
	while y :
		print ("                    ")
		l = input ("Введите число : ")
		print ("                    ")
		if (int(c) == int(l)):
			print ("Получилось")
			y = False;
		else : 
			if (int(c) > int(l)):
				print ("Мало")
			if (int(c) < int(l)):
				print ("Много")
