"""
Root CTF - calculate
made by munsiwoo
"""

def a(num, size):
    r = num + size
    r += 915
    return r

def b(num, size):
    r = num - size
    r -= 372
    return r

def c(num, size):
    r = num ^ size
    r ^= 826
    return r

def d(num, size):
    size %= 32
    r = num >> (32 - size)
    b = (num << size) - (r << 32)
    return b + r

def enc(argv):
    argv = a(ord(argv), 100)
    argv = b(argv, 100)
    argv = c(argv, 100)
    argv = d(argv, 100)
    return argv

def main() :
    flag = [5040, 4944, 5088, 4992, 7232, 4848, 7584, 7344, 4288, 7408, 7360, 7584, 4608, 4880, 4320, 7328, 7360, 
    4608, 4896, 4320, 7472, 7328, 7360, 4608, 4752, 4368, 4848, 4608, 4848, 4368, 4944, 7200]

    alpha1 = "abcdefghijklmnopqrstuvwxyz"
    alpha2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special = "!@#$%^&*()-_+=[]{}\;:\'\"<>,./"
    number = "0123456789"
    chars = alpha1+alpha2+special+number
    table = {}

    for x in chars :
        table[str(enc(x))] = str(x)

    for x in flag :
        print(table[str(x)], end="")

    print()

if __name__ == "__main__" :
    main()