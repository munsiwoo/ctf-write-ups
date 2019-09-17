import re
# made by munsiwoo

f = open('even_more_numbers_with_some_mild_inconveniences.txt', 'r')
result = 0

readall = f.read()
numlist = re.findall('\d+', readall)

for x in range(0, len(numlist)) :
	result += int(numlist[x])

print(result)
