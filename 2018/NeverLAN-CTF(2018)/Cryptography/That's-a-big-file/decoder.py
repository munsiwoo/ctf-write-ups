from base64 import decodestring as base64decode

loadfile = open("Output.txt", 'r')
readfile = loadfile.read()
# made by munsiwoo

tmp = base64decode(str(readfile).encode()).decode()
result = tmp

for x in range(36) :
	tmp = base64decode(str(result).encode()).decode()
	result = tmp

print(result)
