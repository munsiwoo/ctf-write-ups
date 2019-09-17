from hashlib import sha1


shashasha = '05d3693c0781227771b97a9e3cf972d44c2d4439'
# hash = sha1([0-9][a-z0-9][a-z0-9][A-Z][a-z0-9])

table = '0123456789'
table += 'abcdefghijklmnopqrstuvwxyz'
table += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


for a in table[:10] :
	for b in table[:36] :
		for c in table[:36] :
			for d in table[36:] :
				compare = str(sha1((a+b+c+d).encode()).hexdigest())
				#print(compare+" : "+str(a+b+c+d+e+f+g))
				if(compare == shashasha) :
					print(a+b+c+d)
					break




"""
print(hashlib.sha1(b"0bcA").hexdigest())
print(hashlib.sha1(a.encode()).hexdigest())
print(hashlib.sha1(b"1bcB").hexdigest())
print(hashlib.sha1(b"2bcC").hexdigest())
print(hashlib.sha1(b"3bcD").hexdigest())
print(hashlib.sha1(b"3baD").hexdigest())
print(hashlib.sha1(b"3b3D").hexdigest())
print(hashlib.sha1(b"4bcE").hexdigest())
print(hashlib.sha1(b"5bcF").hexdigest())
"""