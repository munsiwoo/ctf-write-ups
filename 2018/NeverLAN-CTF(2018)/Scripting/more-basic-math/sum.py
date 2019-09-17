#made by munsiwoo

f = open('some_more_numbers.txt', 'r')
result = 0

for i in range(0, 10000) :
	number = f.readline()
	result += int(number)


print(result)